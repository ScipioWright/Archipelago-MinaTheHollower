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

def HasCompletedBoneGenerator():
    return True_()
def AnyThreeAstralPlatforms():
    return True_()
def HasDoneColtraneGenerator():
    return True_()
def CompletedAllGenerators():
    return True_()
def InFinale():
    return True_()

def HasAccessToTorch():
    return True_()

def HasLadder():
    return Has("Pinky Kear") & Has("Pinky Back Kear") & (CanSwim() | CanJumpTiles(distance=3)) & CanCarry()
