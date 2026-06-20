import dataclasses
from typing import override, ChainMap

from BaseClasses import CollectionState
from NetUtils import JSONMessagePart
from rule_builder.options import OptionFilter
from rule_builder.rules import Rule, Has, True_

from ...constants import MINA_THE_HOLLOWER
from ...options import AbilityRando
from ...world_base import MinaTheHollowerBase

def HasReachingSideArm():
    return True_()


def CanJumpOneTile():
    return True_()

@dataclasses.dataclass(kw_only=True)
class CanBurrow(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):

    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return Has("Burrow", options=[OptionFilter(AbilityRando, AbilityRando.option_true) ], filtered_resolution=True).resolve(world)

@dataclasses.dataclass(kw_only=True)
class CanCarry(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):

    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return Has("Carry", options=[OptionFilter(AbilityRando, AbilityRando.option_true) ], filtered_resolution=True).resolve(world)

@dataclasses.dataclass(kw_only=True)
class CanClimb(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):

    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return Has("Climb", options=[OptionFilter(AbilityRando, AbilityRando.option_true) ], filtered_resolution=True).resolve(world)

@dataclasses.dataclass(kw_only=True)
class CanSwim(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):

    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return Has("Swim", options=[OptionFilter(AbilityRando, AbilityRando.option_true)], filtered_resolution=True).resolve(world)

@dataclasses.dataclass(kw_only=True)
class CanBounce(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):

    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return Has("Bounce", options=[OptionFilter(AbilityRando, AbilityRando.option_true) ], filtered_resolution=True).resolve(world)

@dataclasses.dataclass(kw_only=True)
class HasVialsCount(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):
    count: int
    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return (Has("HealingVialFirst") & Has("Vial Pouch", count=self.count)).resolve(world)

@dataclasses.dataclass
class MovementItem:
    distance: int
    additive: bool

simple_movement_items: dict[str, MovementItem] = {
    "FWisp" : MovementItem(1, True),
    "DoubleJump": MovementItem(1, True),
    "CrashPad": MovementItem(1, True),
}

base_movements: dict[str, MovementItem] = {
    "Bicycle": MovementItem(5, True),
}

all_movement_items = {
    **simple_movement_items,
    **base_movements,
}
def HasFishingRod():
    return True_()

@dataclasses.dataclass(kw_only=True)
class CanJumpTiles(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):
    distance: int
    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return self.Resolved(distance=self.distance, player=world.player, caching_enabled=False)

    class Resolved(Rule.Resolved):
        distance: int
        ability_rando = False

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            # Always have basic jump
            best_distance = 1 if self.ability_rando else 2

            # Total additive bonuses
            additive_bonus = sum(
                item.distance
                for name, item in simple_movement_items.items()
                if state.has(name, self.player)
            )

            # Check each owned base movement type
            for name, movement in base_movements.items():
                if state.has(name, self.player):
                    best_distance = max(
                        best_distance,
                        movement.distance + additive_bonus
                    )
            return True #best_distance >= self.distance

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            return  {key : {id(self)} for key in all_movement_items.keys()}

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            # this method can be overridden to display custom explanations
            return [
                {"type": "color", "color": "green" if state and self(state) else "salmon", "text": str(self)},
            ]
        @override
        def __str__(self) -> str:
            return "Jump x tiles"