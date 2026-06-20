"""CLI + library: render edges.csv into areas/_generated/<area>_edges.py.

Usage:
    python -m worlds.mina_the_hollower.tools.generate_edges path/to/edges.csv
"""
from __future__ import annotations

import argparse
import pathlib
import sys

try:  # standalone-first so the tooling never needs to boot the Archipelago stack
    import edge_schema as es
except ModuleNotFoundError:  # running via `python -m worlds.mina_the_hollower.tools...`
    from worlds.mina_the_hollower.tools import edge_schema as es

BANNER = (
    "# AUTO-GENERATED -- DO NOT EDIT.\n"
    "# Regenerate from the spreadsheet export with:\n"
    "#   python -m worlds.mina_the_hollower.tools.generate_edges <edges.csv>\n"
    "# The spreadsheet is the source of truth, not this file.\n"
)

IMPORTS = (
    "from rule_builder.rules import Has, True_, CanReachLocation\n"
    "from ... import RegionConnection, Transition, DirectionType, TransitionType\n"
    "from ...rules.ability_rules import (\n"
    "    CanBurrow, CanCarry, CanClimb, CanSwim, CanBounce,\n"
    "    HasVialsCount, CanJumpOneTile, CanJumpTiles, HasReachingSideArm,\n"
    ")\n"
    "from ...rules.state_rules import (\n"
    "   HasLadder, HasCompletedBoneGenerator, HasAccessToTorch, HasDoneColtraneGenerator,\n"
    "   AnyThreeAstralPlatforms, CompletedAllGenerators, InFinale\n"
    ")\n"
)

GENERATED_INIT = (
    "# AUTO-GENERATED package of edge data. DO NOT EDIT.\n"
    "# Regenerate with python -m worlds.mina_the_hollower.tools.generate_edges\n"
)


def _rule_suffix(rule: str) -> str:
    rule = rule.strip()
    return f", {rule}" if rule else ""


def _comment(notes: str) -> str:
    notes = notes.strip().replace("\n", " ")
    return f"  # {notes}" if notes else ""


def render_area_module(area: str, edges: "list[es.Edge]") -> str:
    area_edges = [e for e in edges if e.area == area]
    regions = sorted(es.derived_regions(edges, area))
    connections = sorted((e for e in area_edges if e.is_internal),
                         key=lambda e: e.resolved_name)
    transitions = sorted((e for e in area_edges if not e.is_internal),
                         key=lambda e: e.resolved_name)

    out: list[str] = [BANNER, IMPORTS, ""]

    out.append("regions: set[str] = {")
    for r in regions:
        out.append(f"    {r!r},")
    out.append("}\n")

    out.append("connections: dict[str, RegionConnection] = {")
    for e in connections:
        out.append(
            f"    {e.resolved_name!r}: RegionConnection("
            f"{e.from_region!r}, {e.to_region!r}{_rule_suffix(e.rule)}),"
            f"{_comment(e.notes)}"
        )
    out.append("}\n")

    out.append("transitions: dict[str, Transition] = {")
    for e in transitions:
        out.append(
            f"    {e.resolved_name!r}: Transition("
            f"{e.from_region!r}, {e.to_region!r}, "
            f"DirectionType.{e.direction}, TransitionType.{e.transition_type}"
            f"{_rule_suffix(e.rule)}),{_comment(e.notes)}"
        )
    out.append("}")

    return "\n".join(out) + "\n"


def write_modules(edges: "list[es.Edge]", out_dir: pathlib.Path) -> "list[pathlib.Path]":
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[pathlib.Path] = []

    init_path = out_dir / "__init__.py"
    init_path.write_text(GENERATED_INIT, encoding="utf-8")
    written.append(init_path)

    for area in sorted({e.area for e in edges}):
        path = out_dir / f"{area}_edges.py"
        path.write_text(render_area_module(area, edges), encoding="utf-8")
        written.append(path)

    return written


def main(argv: "list[str] | None" = None) -> int:
    parser = argparse.ArgumentParser(description="Generate Mina edge modules")
    parser.add_argument("csv", type=pathlib.Path)
    args = parser.parse_args(argv)

    edges = es.read_edges_csv(args.csv)
    out_dir = (pathlib.Path(__file__).resolve().parents[1]
               / "data" / "locations" / "_generated")
    written = write_modules(edges, out_dir)
    print(f"Wrote {len(written)} files to {out_dir}:")
    for p in written:
        print(f"  - {p.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
