import dataclasses
from typing import override

from BaseClasses import CollectionState
from NetUtils import JSONMessagePart
from rule_builder.options import OptionFilter
from rule_builder.rules import Rule, Has, True_, False_
from .ability_rules import CanJumpTiles, CanSwim, CanCarry, CanBurrow
from .. import ShortCutItem
from ..items import Kear, SingleKears, AreaKears, Trinkets, AstralPlatforms, Sidearms, PlayerUpgrades, PermanentUpgrades
from ..items.kears import kear_area_lookup
from ...constants import MINA_THE_HOLLOWER
from ...world_base import MinaTheHollowerBase

@dataclasses.dataclass(kw_only=True)
class HasKear(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):
    kear: str
    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        if world.options.kear_rando.value == 0:
            return Has(Kear.UNIVERSAL_KEAR.value, 42).resolve(world)
        elif world.options.kear_rando.value == 1:
            return Has(self.kear).resolve(world)
        else:
            area_kear = kear_area_lookup.get(self.kear)
            if area_kear is not None:
                return Has(area_kear.value).resolve(world)
            else:
                return False_().resolve(world)

@dataclasses.dataclass(kw_only=True)
class HasSparks(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):
    count: int
    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return self.Resolved(count=self.count, player=world.player, caching_enabled=False)

    class Resolved(Rule.Resolved):
        count:int
        @override
        def _evaluate(self, state: CollectionState) -> bool:
            sparks = 1 if state.has(Trinkets.SPARK_CATCHER.value, self.player) else 0
            sparks += state.count(PlayerUpgrades.SPARK_CONTAINER.value, self.player)
            return sparks >= self.count

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            return {
                Trinkets.SPARK_CATCHER.value: {id(self)},
                PlayerUpgrades.SPARK_CONTAINER.value: {id(self)},
            }

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            # this method can be overridden to display custom explanations
            return [
                {"type": "color", "color": "green" if state and self(state) else "salmon", "text": str(self)},
            ]
        @override
        def __str__(self) -> str:
            return f"Has Spark Count"


@dataclasses.dataclass(kw_only=True)
class HasAllKears(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):
    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return self.Resolved(kear_rando=world.options.kear_rando.value, player=world.player, caching_enabled=False)

    class Resolved(Rule.Resolved):
        kear_rando:int
        @override
        def _evaluate(self, state: CollectionState) -> bool:
            if self.kear_rando == 0:
                return state.has(Kear.UNIVERSAL_KEAR.value, self.player,50)
            elif self.kear_rando == 1:
                for item in SingleKears:
                    if not state.has(item.value, self.player):
                        return False
            else:
                for item in AreaKears:
                    if not state.has(item.value, self.player):
                        return False
            return True

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            return {item.value: {id(self)} for item in [*Kear, *AreaKears, *SingleKears]}

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            # this method can be overridden to display custom explanations
            return [
                {"type": "color", "color": "green" if state and self(state) else "salmon", "text": str(self)},
            ]
        @override
        def __str__(self) -> str:
            return f"Has All Kears"


@dataclasses.dataclass(kw_only=True)
class HasTrinketCount(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):
    count: int

    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return self.Resolved(count=self.count, player=world.player, caching_enabled=False)

    class Resolved(Rule.Resolved):
        count: int
        ability_rando = False

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            trinket_count = 0
            for trinket in Trinkets:
                if state.has(trinket.value, self.player):
                    trinket_count += 1

            return trinket_count >= self.count

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            return {item.value: {id(self)} for item in Trinkets}

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            # this method can be overridden to display custom explanations
            return [
                {"type": "color", "color": "green" if state and self(state) else "salmon", "text": str(self)},
            ]
        @override
        def __str__(self) -> str:
            return f"Has {self.count} Trinkets"


@dataclasses.dataclass(kw_only=True)
class StartedInOssex(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):
    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        if world.options.ossex_start.value == 1:
            return True_().resolve(world)
        return False_().resolve(world)

def HasRepairedSolemnGenerator():
    return Has("Repair Solemn Generator")
def HasRepairedSwampyGenerator():
    return Has("Repair Swampy Generator")
def HasRepairedWindyGenerator():
    return Has("Repair Windy Generator")
def HasRepairedShorelineGenerator():
    return Has("Repair Shoreline Generator")
def HasRepairedFrozenGenerator():
    return Has("Repair Frozen Generator")
def HasRepairedStarryGenerator():
    return Has("Repair Starry Generator")

def AnyThreeAstralPlatforms():
    green = Has(AstralPlatforms.GREEN_ASTRAL_PLATFORMS.value)
    red = Has(AstralPlatforms.RED_ASTRAL_PLATFORMS.value)
    blue = Has(AstralPlatforms.BLUE_ASTRAL_PLATFORMS.value)
    yellow = Has(AstralPlatforms.YELLOW_ASTRAL_PLATFORMS.value)

    return (
        (green & red & blue) |
        (green & red & yellow) |
        (green & blue & yellow) |
        (red & blue & yellow)
    )

def HasRepairedAllGenerators():
    return HasRepairedSolemnGenerator() & HasRepairedSwampyGenerator() & HasRepairedWindyGenerator() & HasRepairedShorelineGenerator() & HasRepairedFrozenGenerator() & HasRepairedStarryGenerator()

def HasRepairedOneGenerator():
    return HasRepairedSolemnGenerator() | HasRepairedSwampyGenerator() | HasRepairedWindyGenerator() | HasRepairedShorelineGenerator() | HasRepairedFrozenGenerator() | HasRepairedStarryGenerator()



#depricated
def InFinale():
    return HasRepairedAllGenerators()

#figure out when screen rando exists
def HasAccessToTorch():
    return CanCarry()

#figure out when screen rando exists
def HasLadder():
    return Has(SingleKears.PINKY_KEAR.value) & Has(SingleKears.PINKY_BACK_KEAR.value) & (CanSwim() | CanJumpTiles(distance=3)) & CanCarry()

sidearm_rules: list[ShortCutItem] = [
    ShortCutItem(Sidearms.HOLLOWERS_ROCKS, True_()),
    ShortCutItem(Sidearms.GYRO_DAGGER, True_()),
    ShortCutItem(Sidearms.VOLT_HATCHET, True_()),
    ShortCutItem(Sidearms.IRON_STEED, Has(PlayerUpgrades.SPARK_CONTAINER.value, 2) | ((Has(PermanentUpgrades.SEPTEMBURG_TICKET.value) & Has(PermanentUpgrades.TRAIN_PASS.value)) & CanBurrow())),
    ShortCutItem(Sidearms.FOG_THROWER, CanBurrow()),
    ShortCutItem(Sidearms.DEFLECTOR_PARASOL, CanBurrow()),
    ShortCutItem(Sidearms.MIST_JAR, CanBurrow()),
    ShortCutItem(Sidearms.DRIVER_DRILL, CanBurrow()),
    ShortCutItem(Sidearms.RECALL_DISC, True_()),
    ShortCutItem(Sidearms.BOUNDING_BOMBS, True_()),
    ShortCutItem(Sidearms.BECKONING_COLLAR, True_()),
    ShortCutItem(Sidearms.GNAWING_GHOSTS, True_()),
]
