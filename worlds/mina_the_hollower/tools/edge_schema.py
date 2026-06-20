"""Pure-stdlib schema for the Mina the Hollower edge graph.

Shared by validate_edges and generate_edges. Imports no Archipelago runtime
code: rule expressions are validated structurally (AST), not executed.
"""
from __future__ import annotations

import ast
import csv
from dataclasses import dataclass
from pathlib import Path

COLUMNS = ["area", "name", "from_region", "to_region",
           "transition_type", "direction", "rule", "notes"]

TRANSITION_TYPES = {
    "INTERNAL", "SCREENS", "AREA_SCREENS", "DOORS", "MIRRORS", "STAIRS",
    "GEYSER_UP", "GEYSER_DOWN", "BURROW", "DO_NOT_RANDOMIZE_ENTRANCE",
}

DIRECTIONS = {"NORTH", "EAST", "SOUTH", "WEST", "ASTRAL", "OVERWORLD"}

# Transition types that participate in entrance matching, and the directions
# that can actually be paired for each (mirrors matching_transition_types in
# data/__init__.py). Types not listed here are never shuffled-matched, so a
# direction/type pairing check does not apply to them.
MATCHABLE_DIRECTIONS = {
    "SCREENS": {"NORTH", "EAST", "SOUTH", "WEST"},
    "AREA_SCREENS": {"NORTH", "EAST", "SOUTH", "WEST"},
    "DOORS": {"NORTH", "EAST", "SOUTH", "WEST"},
    "STAIRS": {"NORTH", "EAST", "SOUTH", "WEST"},
    "MIRRORS": {"ASTRAL", "OVERWORLD"},
}

# Rule-expression call names permitted in the `rule` column. These map to
# helpers in data/rules/ability_rules.py plus rule_builder primitives.
RULE_ALLOWED_CALLS = {
    "Has", "True_", "CanReachLocation",
    "CanBurrow", "CanCarry", "CanClimb", "CanSwim", "CanBounce",
    "HasVialsCount", "CanJumpOneTile", "CanJumpTiles", "HasReachingSideArm", "HasCompletedBoneGenerator",
    "HasLadder", "HasAccessToTorch", "HasDoneColtraneGenerator, AnyThreeAstralPlatforms, CompletedAllGenerators",
    "InFinale",
}


@dataclass
class Edge:
    area: str
    name: str
    from_region: str
    to_region: str
    transition_type: str
    direction: str
    rule: str
    notes: str

    @property
    def is_internal(self) -> bool:
        return self.transition_type == "INTERNAL"

    @property
    def resolved_name(self) -> str:
        return self.name.strip() or auto_name(self.from_region, self.to_region)


def auto_name(from_region: str, to_region: str) -> str:
    return f"{from_region}_{to_region}"


def validate_rule_expression(expr: str) -> list[str]:
    """Return a list of human-readable problems with a rule cell.

    Empty string is valid (resolves to True_() in generated code). Otherwise the
    expression must parse and may only use: the allowed call names in
    RULE_ALLOWED_CALLS, the bitwise operators & | ~, calls with literal/keyword
    arguments, and literal constants. Any bare identifier (a helper not called)
    or unknown call name is rejected.
    """
    expr = expr.strip()
    if not expr:
        return []
    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError as exc:
        return [f"syntax error: {exc.msg}"]

    errors: list[str] = []

    def check(node: ast.AST) -> None:
        if isinstance(node, ast.Expression):
            check(node.body)
        elif isinstance(node, ast.BinOp) and isinstance(node.op, (ast.BitAnd, ast.BitOr)):
            check(node.left)
            check(node.right)
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Invert):
            check(node.operand)
        elif isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                errors.append("only direct helper calls are allowed")
            elif node.func.id not in RULE_ALLOWED_CALLS:
                errors.append(f"unknown rule helper: {node.func.id}")
            for arg in node.args:
                check_value(arg)
            for kw in node.keywords:
                check_value(kw.value)
        else:
            errors.append(f"disallowed expression element: {type(node).__name__}")

    def check_value(node: ast.AST) -> None:
        # Argument values may be literals or nested allowed expressions.
        if isinstance(node, ast.Constant):
            return
        check(node)

    check(tree)
    return errors


def validate_rows(edges: list[Edge], known_areas: set[str]) -> list[str]:
    """Return all structural/referential problems across the edge list.

    Each problem is prefixed with the 1-based row index for locatability.
    """
    errors: list[str] = []
    seen_names: dict[str, int] = {}

    for i, e in enumerate(edges, start=1):
        def err(msg: str) -> None:
            errors.append(f"row {i} ({e.from_region!r} -> {e.to_region!r}): {msg}")

        if e.area not in known_areas:
            err(f"unknown area: {e.area!r}")
        if not e.from_region.strip():
            err("from_region is blank")
        if not e.to_region.strip():
            err("to_region is blank")
        if e.transition_type not in TRANSITION_TYPES:
            err(f"unknown transition_type: {e.transition_type!r}")

        if e.is_internal:
            if e.direction.strip():
                err("INTERNAL rows must have a blank direction")
        else:
            if not e.name.strip():
                err("typed transition is missing a name")
            if not e.direction.strip():
                err("typed transition is missing a direction")
            elif e.direction not in DIRECTIONS:
                err(f"unknown direction: {e.direction!r}")
            elif e.transition_type in MATCHABLE_DIRECTIONS and \
                    e.direction not in MATCHABLE_DIRECTIONS[e.transition_type]:
                err(f"{e.transition_type} cannot pair direction {e.direction}")

        for problem in validate_rule_expression(e.rule):
            err(f"rule: {problem}")

        key = e.resolved_name
        if key in seen_names:
            err(f"duplicate edge name {key!r} (also row {seen_names[key]})")
        else:
            seen_names[key] = i

    return errors


def derived_regions(edges: list[Edge], area: str) -> set[str]:
    """Regions owned by `area`: every from_region of that area's rows."""
    return {e.from_region for e in edges if e.area == area}


def unresolved_to_regions(edges: list[Edge]) -> list[str]:
    """to_region values that never appear as a from_region anywhere in the edge
    list. On a combined CSV these are either edges into not-yet-migrated areas
    (expected) or typos/truncated names (bugs). Returned sorted for reporting."""
    froms = {e.from_region for e in edges}
    return sorted({e.to_region for e in edges
                   if e.to_region.strip() and e.to_region not in froms})


def read_edges_csv(path: "Path | str") -> list[Edge]:
    """Load an edges.csv into Edge objects. Whitespace is stripped from every
    cell; missing trailing columns are treated as blank."""
    edges: list[Edge] = []
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None:
            return edges
        missing = [c for c in COLUMNS if c not in reader.fieldnames]
        if missing:
            raise ValueError(f"edges CSV missing columns: {missing}")
        for raw in reader:
            edges.append(Edge(**{c: (raw.get(c) or "").strip() for c in COLUMNS}))
    return edges
