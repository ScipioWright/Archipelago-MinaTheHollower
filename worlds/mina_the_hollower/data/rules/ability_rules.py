import dataclasses
from typing import override, ChainMap

from BaseClasses import CollectionState
from NetUtils import JSONMessagePart
from rule_builder.options import OptionFilter
from rule_builder.rules import Rule, Has, True_
from ..items import Abilities, PlayerUpgrades, additive_movement_items, base_movement_items, all_movement_items, \
    all_power_items, upgrade_powers, trinket_powers, Trinkets, Sidearms, PermanentUpgrades

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
        return Has(Abilities.BURROW.value, options=[OptionFilter(AbilityRando, Abilities.BURROW.value, operator="contains")], filtered_resolution=True).resolve(world)

@dataclasses.dataclass(kw_only=True)
class CanCarry(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):

    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return Has(Abilities.CARRY.value, options=[OptionFilter(AbilityRando, Abilities.CARRY.value, operator="contains")], filtered_resolution=True).resolve(world)

@dataclasses.dataclass(kw_only=True)
class CanClimb(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):

    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return Has(Abilities.CLIMB.value, options=[OptionFilter(AbilityRando, Abilities.CLIMB.value, operator="contains")], filtered_resolution=True).resolve(world)

@dataclasses.dataclass(kw_only=True)
class CanSwim(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):

    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return Has(Abilities.SWIM.value, options=[OptionFilter(AbilityRando, Abilities.SWIM.value, operator="contains")], filtered_resolution=True).resolve(world)

@dataclasses.dataclass(kw_only=True)
class CanBounce(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):

    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return Has(Abilities.BOUNCE.value, options=[OptionFilter(AbilityRando, Abilities.BOUNCE.value, operator="contains")], filtered_resolution=True).resolve(world)

@dataclasses.dataclass(kw_only=True)
class HasVialsCount(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):
    count: int
    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return (Has(PermanentUpgrades.HEALING_VIAL_POUCH.value) & Has(PlayerUpgrades.HEALING_VIAL.value, count=self.count)).resolve(world)

def HasBeastiumTransform():
    return Has(PlayerUpgrades.TRINKET_BAG.value, count=5) & (Has(Trinkets.RECKLESS_BEASTIUM.value) &
            Has(Trinkets.WARDING_BEASTIUM.value) &
            Has(Trinkets.BURNING_BEASTIUM.value) &
            Has(Trinkets.DRAINING_BEASTIUM.value) &
            Has(Trinkets.STARVING_BEASTIUM.value) &
            Has(Trinkets.VOLATILE_BEASTIUM.value))


def HasFishingRod():
    return Has(Sidearms.FISHING_ROD.value)

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
            best_distance = 1
            # Total additive bonuses
            additive_bonus = sum(
                movement_item.distance
                for movement_item in additive_movement_items
                if state.has(movement_item.type.value, self.player)
            )
            # Check each owned base movement type
            for movement_item in base_movement_items:
                if state.has(movement_item.type.value, self.player):
                    best_distance = max(
                        best_distance,
                        movement_item.distance + additive_bonus
                    )

            return best_distance >= self.distance

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            return  {item.type.value : {item.type.item_id} for item in all_movement_items}

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            # this method can be overridden to display custom explanations
            return [
                {"type": "color", "color": "green" if state and self(state) else "salmon", "text": str(self)},
            ]
        @override
        def __str__(self) -> str:
            return "Jump x tiles"


@dataclasses.dataclass(kw_only=True)
class PowerLevelThreshold(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):
    power: int

    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return self.Resolved(power=self.power, player=world.player, caching_enabled=False)

    class Resolved(Rule.Resolved):
        power: int
        ability_rando = False

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            total_power = 0

            for item in upgrade_powers:

                if item.requiredType is None or state.has(item.requiredType.value, self.player):
                    total_power += state.count(item.type.value, self.player) * item.power

            trinket_slots = state.count(PlayerUpgrades.TRINKET_BAG.value, self.player)

            valid_trinket_powers = [
                item.power
                for item in trinket_powers
                if item.requiredType is None or state.has(item.requiredType.value, self.player)
            ]
            best_trinkets = sorted(valid_trinket_powers, reverse=True)[:trinket_slots]
            total_power += sum(best_trinkets)

            return total_power >= self.power

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            return {item.type.value: {id(self)} for item in all_power_items}

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            # this method can be overridden to display custom explanations
            return [
                {"type": "color", "color": "green" if state and self(state) else "salmon", "text": str(self)},
            ]
        @override
        def __str__(self) -> str:
            return f"Power Level of {self.power} Required"