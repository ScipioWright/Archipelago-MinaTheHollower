import dataclasses
from typing import override

from rule_builder.options import OptionFilter
from rule_builder.rules import Rule, Has, True_
from .ability_rules import CanJumpTiles, CanSwim, CanCarry
from ...constants import MINA_THE_HOLLOWER
from ...world_base import MinaTheHollowerBase


@dataclasses.dataclass(kw_only=True)
class HasCompletedOneSparkGenerator(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):
    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return True_[MinaTheHollowerBase]().resolve(world)

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
    green = Has("Green Astral Platforms")
    red = Has("Red Astral Platforms")
    blue = Has("Blue Astral Platforms")
    yellow = Has("Yellow Astral Platforms")

    return (
        (green & red & blue) |
        (green & red & yellow) |
        (green & blue & yellow) |
        (red & blue & yellow)
    )

def HasRepairedAllGenerators():
    return HasRepairedSolemnGenerator() & HasRepairedSwampyGenerator() & HasRepairedWindyGenerator() & HasRepairedShorelineGenerator() & HasRepairedFrozenGenerator() & HasRepairedStarryGenerator()

#depricated
def InFinale():
    return True_()

#figure out when screen rando exists
def HasAccessToTorch():
    return True_()

#figure out when screen rando exists
def HasLadder():
    return Has("Pinky Kear") & Has("Pinky Back Kear") & (CanSwim() | CanJumpTiles(distance=3)) & CanCarry()
