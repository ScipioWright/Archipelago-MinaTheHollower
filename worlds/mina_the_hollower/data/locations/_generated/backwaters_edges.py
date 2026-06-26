# AUTO-GENERATED -- DO NOT EDIT.
# Regenerate from the spreadsheet export with:
#   python -m worlds.mina_the_hollower.tools.generate_edges <edges.csv>
# The spreadsheet is the source of truth, not this file.

from rule_builder.rules import Has, True_, CanReachLocation
from ... import RegionConnection, Transition, DirectionType, TransitionType
from ...rules.ability_rules import (
    CanBurrow, CanCarry, CanClimb, CanSwim, CanBounce, PowerLevelThreshold,
    HasVialsCount, CanJumpTiles, HasReachingSideArm, HasFishingRod, CanSpring, 
)
from ...rules.state_rules import (
   HasLadder, HasRepairedShorelineGenerator, HasAccessToTorch, StartedInOssex, 
   AnyThreeAstralPlatforms, HasRepairedAllGenerators, HasKear, HasSparks,
   HasRepairedSolemnGenerator, HasRepairedSwampyGenerator, HasRepairedWindyGenerator,
   HasRepairedShorelineGenerator, HasRepairedFrozenGenerator, HasRepairedStarryGenerator,
   HasRepairedOneGenerator,
)
from ...items.game_items import (
   PermanentUpgrades, PlayerUpgrades, Trinkets
)
from ...items.kears import (
   SingleKears,
)
from ...items.blockers import (
   AstralPlatforms,
)


regions: set[str] = {
    'Backwaters Bayou Falls East',
    'Backwaters Bayou Falls West',
    'Backwaters Fishing Hole',
    'Backwaters Lower Swamp',
    'Backwaters Lower Swamp Bayou Entrance',
    'Backwaters Lower Swamp Fishing',
    'Backwaters Lower Swamp Shanty Band',
    'Backwaters Lower Swamp Station',
    'Backwaters Lower Swamp Station Entrance',
    "Backwaters Lucky's Lair",
    'Backwaters Pinky Back Pond Board',
    'Backwaters Pinky Back Pond Lawn',
    'Backwaters Pinky Front Lawn East',
    'Backwaters Pinky Front Lawn West',
    'Backwaters Pinky Outside',
    'Backwaters Pinky Shop',
    'Backwaters Pinky Shop Back',
    'Backwaters Thalessian Lillies',
    'Backwaters Thalessian Way Lower',
    'Backwaters Thalessian Way Upper',
    'Backwaters Upper Lantern Cave',
    'Backwaters Upper Lantern Pad',
    'Backwaters Upper Swamp Back',
    'Backwaters Upper Swamp East',
    'Backwaters Upper Swamp Entrance',
    'Backwaters Upper Swamp Entrance Exit',
    'Backwaters Upper Swamp Fenced',
    'Backwaters Upper Swamp Lily',
    'Backwaters Upper Swamp Secret Room',
    'Backwaters Upper Swamp Waterfall',
}

connections: dict[str, RegionConnection] = {
    'Backwaters Bayou Falls East_Backwaters Bayou Falls West': RegionConnection('Backwaters Bayou Falls East', 'Backwaters Bayou Falls West', CanJumpTiles(distance=3) | CanSwim()),
    'Backwaters Bayou Falls West_Backwaters Bayou Falls East': RegionConnection('Backwaters Bayou Falls West', 'Backwaters Bayou Falls East', CanJumpTiles(distance=2) | CanSwim()),
    'Backwaters Lower Swamp Bayou Entrance_Backwaters Lower Swamp Shanty Band': RegionConnection('Backwaters Lower Swamp Bayou Entrance', 'Backwaters Lower Swamp Shanty Band', True_()),
    'Backwaters Lower Swamp Fishing_Backwaters Lower Swamp': RegionConnection('Backwaters Lower Swamp Fishing', 'Backwaters Lower Swamp', CanJumpTiles(distance=7) | HasKear(kear=SingleKears.BACKWATERS_FISHING_KEAR.value)),
    'Backwaters Lower Swamp Shanty Band_Backwaters Lower Swamp': RegionConnection('Backwaters Lower Swamp Shanty Band', 'Backwaters Lower Swamp', CanSwim()),
    'Backwaters Lower Swamp Shanty Band_Backwaters Lower Swamp Bayou Entrance': RegionConnection('Backwaters Lower Swamp Shanty Band', 'Backwaters Lower Swamp Bayou Entrance', CanJumpTiles(distance=4) | CanSwim()),
    'Backwaters Lower Swamp Station Entrance_Backwaters Lower Swamp': RegionConnection('Backwaters Lower Swamp Station Entrance', 'Backwaters Lower Swamp', CanJumpTiles(distance=2) | CanSwim()),
    'Backwaters Lower Swamp Station Entrance_Backwaters Lower Swamp Bayou Entrance': RegionConnection('Backwaters Lower Swamp Station Entrance', 'Backwaters Lower Swamp Bayou Entrance', CanBurrow() | CanSwim()),
    'Backwaters Lower Swamp_Backwaters Lower Swamp Bayou Entrance': RegionConnection('Backwaters Lower Swamp', 'Backwaters Lower Swamp Bayou Entrance', CanSwim()),
    'Backwaters Lower Swamp_Backwaters Lower Swamp Fishing': RegionConnection('Backwaters Lower Swamp', 'Backwaters Lower Swamp Fishing', CanJumpTiles(distance=7) | HasKear(kear=SingleKears.BACKWATERS_FISHING_KEAR.value)),
    'Backwaters Lower Swamp_Backwaters Lower Swamp Shanty Band': RegionConnection('Backwaters Lower Swamp', 'Backwaters Lower Swamp Shanty Band', CanSwim()),
    'Backwaters Lower Swamp_Backwaters Lower Swamp Station Entrance': RegionConnection('Backwaters Lower Swamp', 'Backwaters Lower Swamp Station Entrance', CanJumpTiles(distance=2) | CanSwim()),
    'Backwaters Pinky Back Pond Board_Backwaters Pinky Back Pond Lawn': RegionConnection('Backwaters Pinky Back Pond Board', 'Backwaters Pinky Back Pond Lawn', CanJumpTiles(distance=3) | CanSwim()),
    'Backwaters Pinky Back Pond Lawn_Backwaters Pinky Back Pond Board': RegionConnection('Backwaters Pinky Back Pond Lawn', 'Backwaters Pinky Back Pond Board', CanJumpTiles(distance=3) | CanSwim()),
    'Backwaters Pinky Front Lawn East_Backwaters Pinky Front Lawn West': RegionConnection('Backwaters Pinky Front Lawn East', 'Backwaters Pinky Front Lawn West', CanBurrow()),
    'Backwaters Pinky Front Lawn West_Backwaters Pinky Front Lawn East': RegionConnection('Backwaters Pinky Front Lawn West', 'Backwaters Pinky Front Lawn East', CanBurrow()),
    'Backwaters Pinky Shop Back_Backwaters Pinky Shop': RegionConnection('Backwaters Pinky Shop Back', 'Backwaters Pinky Shop', True_()),
    'Backwaters Thalessian Way Lower_Backwaters Thalessian Way Upper': RegionConnection('Backwaters Thalessian Way Lower', 'Backwaters Thalessian Way Upper', HasFishingRod() & HasReachingSideArm()),
    'Backwaters Thalessian Way Upper_Backwaters Thalessian Way Lower': RegionConnection('Backwaters Thalessian Way Upper', 'Backwaters Thalessian Way Lower', True_()),
    'Backwaters Upper Lantern Pad_Backwaters Upper Swamp East': RegionConnection('Backwaters Upper Lantern Pad', 'Backwaters Upper Swamp East', CanJumpTiles(distance=3) | CanSwim()),
    'Backwaters Upper Lantern Pad_Backwaters Upper Swamp Entrance Exit': RegionConnection('Backwaters Upper Lantern Pad', 'Backwaters Upper Swamp Entrance Exit', CanBurrow()),
    'Backwaters Upper Swamp Back_Backwaters Upper Swamp Entrance': RegionConnection('Backwaters Upper Swamp Back', 'Backwaters Upper Swamp Entrance', CanJumpTiles(distance=2)),
    'Backwaters Upper Swamp Back_Backwaters Upper Swamp Fenced': RegionConnection('Backwaters Upper Swamp Back', 'Backwaters Upper Swamp Fenced', CanJumpTiles(distance=4) | CanSwim()),
    'Backwaters Upper Swamp East_Backwaters Upper Lantern Pad': RegionConnection('Backwaters Upper Swamp East', 'Backwaters Upper Lantern Pad', CanJumpTiles(distance=3) | CanSwim()),
    'Backwaters Upper Swamp East_Backwaters Upper Swamp Lily': RegionConnection('Backwaters Upper Swamp East', 'Backwaters Upper Swamp Lily', CanJumpTiles(distance=2) | CanSwim()),
    'Backwaters Upper Swamp Entrance Exit_Backwaters Upper Swamp Entrance': RegionConnection('Backwaters Upper Swamp Entrance Exit', 'Backwaters Upper Swamp Entrance', True_()),
    'Backwaters Upper Swamp Entrance_Backwaters Upper Swamp Waterfall': RegionConnection('Backwaters Upper Swamp Entrance', 'Backwaters Upper Swamp Waterfall', True_()),
    'Backwaters Upper Swamp Fenced_Backwaters Upper Lantern Pad': RegionConnection('Backwaters Upper Swamp Fenced', 'Backwaters Upper Lantern Pad', CanJumpTiles(distance=4) | CanSwim()),
    'Backwaters Upper Swamp Fenced_Backwaters Upper Swamp Back': RegionConnection('Backwaters Upper Swamp Fenced', 'Backwaters Upper Swamp Back', CanJumpTiles(distance=4) | CanSwim()),
    'Backwaters Upper Swamp Lily_Backwaters Upper Lantern Pad': RegionConnection('Backwaters Upper Swamp Lily', 'Backwaters Upper Lantern Pad', CanSwim()),
    'Backwaters Upper Swamp Lily_Backwaters Upper Swamp East': RegionConnection('Backwaters Upper Swamp Lily', 'Backwaters Upper Swamp East', CanJumpTiles(distance=2) | CanSwim()),
    'Backwaters Upper Swamp Waterfall_Backwaters Upper Swamp Back': RegionConnection('Backwaters Upper Swamp Waterfall', 'Backwaters Upper Swamp Back', CanJumpTiles(distance=2)),
}

transitions: dict[str, Transition] = {
    'Backwaters Bayou Falls East East Transition': Transition('Backwaters Bayou Falls East', 'Backwaters Lower Swamp Bayou Entrance', DirectionType.EAST, TransitionType.SCREENS, True_()),
    'Backwaters Bayou Falls West Area Transition': Transition('Backwaters Bayou Falls West', "Nox's Bayou Boat Station Path", DirectionType.WEST, TransitionType.AREA_SCREENS, True_()),
    'Backwaters Fishing Hole East Transition': Transition('Backwaters Fishing Hole', 'Backwaters Thalessian Way Lower', DirectionType.EAST, TransitionType.SCREENS, True_()),
    'Backwaters Fishing Hole West Transition': Transition('Backwaters Fishing Hole', 'Backwaters Lower Swamp Fishing', DirectionType.WEST, TransitionType.SCREENS, True_()),
    'Backwaters Lower Swamp Bayou Entrance Lucky Burrow': Transition('Backwaters Lower Swamp Bayou Entrance', "Backwaters Lucky's Lair", DirectionType.NORTH, TransitionType.BURROW, CanBurrow()),
    'Backwaters Lower Swamp Bayou Entrance West Transition': Transition('Backwaters Lower Swamp Bayou Entrance', 'Backwaters Bayou Falls East', DirectionType.WEST, TransitionType.SCREENS, True_()),
    'Backwaters Lower Swamp Fishing East Transition': Transition('Backwaters Lower Swamp Fishing', 'Backwaters Fishing Hole', DirectionType.EAST, TransitionType.SCREENS, True_()),
    'Backwaters Lower Swamp North Transition': Transition('Backwaters Lower Swamp', 'Backwaters Upper Swamp Lily', DirectionType.NORTH, TransitionType.SCREENS, True_()),
    'Backwaters Lower Swamp Shanty Band Secret North Transition': Transition('Backwaters Lower Swamp Shanty Band', 'Backwaters Upper Swamp Back', DirectionType.NORTH, TransitionType.SCREENS, CanSwim()),
    'Backwaters Lower Swamp Station Entrance East Transition': Transition('Backwaters Lower Swamp Station Entrance', 'Backwaters Lower Swamp Station', DirectionType.EAST, TransitionType.SCREENS, True_()),
    'Backwaters Lower Swamp Station South Area Transition': Transition('Backwaters Lower Swamp Station', "Loner's Landing Bay", DirectionType.SOUTH, TransitionType.AREA_SCREENS, True_()),
    'Backwaters Lower Swamp Station Train': Transition('Backwaters Lower Swamp Station', 'Ossex Train Caboose', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has(PermanentUpgrades.TRAIN_PASS.value) & Has(PermanentUpgrades.BAYOU_TICKET.value)),
    "Backwaters Lucky's Lair Burrow Exit": Transition("Backwaters Lucky's Lair", 'Backwaters Lower Swamp Bayou Entrance', DirectionType.SOUTH, TransitionType.BURROW, CanBurrow()),
    "Backwaters Lucky's Lair Pipe": Transition("Backwaters Lucky's Lair", "Nox's Bayou Bog Pipe Room", DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_()),
    'Backwaters Pinky Back Pond Board South Transition': Transition('Backwaters Pinky Back Pond Board', 'Backwaters Pinky Front Lawn West', DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    'Backwaters Pinky Back Pond Lawn West Shop Entrance': Transition('Backwaters Pinky Back Pond Lawn', 'Backwaters Pinky Shop Back', DirectionType.WEST, TransitionType.SCREENS, HasKear(kear=SingleKears.PINKY_BACK_KEAR.value)),
    'Backwaters Pinky Front Lawn East West Transition': Transition('Backwaters Pinky Front Lawn East', 'Backwaters Pinky Outside', DirectionType.WEST, TransitionType.SCREENS, True_()),
    'Backwaters Pinky Front Lawn West North Transition': Transition('Backwaters Pinky Front Lawn West', 'Backwaters Pinky Back Pond Board', DirectionType.NORTH, TransitionType.SCREENS, True_()),
    'Backwaters Pinky Outside East Transition': Transition('Backwaters Pinky Outside', 'Backwaters Pinky Front Lawn East', DirectionType.EAST, TransitionType.SCREENS, True_()),
    'Backwaters Pinky Outside Shop Door': Transition('Backwaters Pinky Outside', 'Backwaters Pinky Shop', DirectionType.NORTH, TransitionType.DOORS, True_()),
    'Backwaters Pinky Outside West Locked Transition': Transition('Backwaters Pinky Outside', 'Backwaters Upper Swamp Lily', DirectionType.WEST, TransitionType.SCREENS, HasKear(kear=SingleKears.PINKY_KEAR.value)),
    'Backwaters Pinky Shop Back East Exit': Transition('Backwaters Pinky Shop Back', 'Backwaters Pinky Back Pond Lawn', DirectionType.EAST, TransitionType.SCREENS, HasKear(kear=SingleKears.PINKY_BACK_KEAR.value)),
    'Backwaters Pinky Shop Exit': Transition('Backwaters Pinky Shop', 'Backwaters Pinky Outside', DirectionType.SOUTH, TransitionType.DOORS, True_()),
    'Backwaters Thalessian Lillies West Transition': Transition('Backwaters Thalessian Lillies', 'Backwaters Thalessian Way Upper', DirectionType.WEST, TransitionType.SCREENS, True_()),
    'Backwaters Thalessian Way Lower West Transition': Transition('Backwaters Thalessian Way Lower', 'Backwaters Fishing Hole', DirectionType.WEST, TransitionType.SCREENS, True_()),
    'Backwaters Thalessian Way Upper East Transition': Transition('Backwaters Thalessian Way Upper', 'Backwaters Thalessian Lillies', DirectionType.EAST, TransitionType.SCREENS, True_()),
    'Backwaters Upper Lantern Cave_Backwaters Upper Lantern Pad': Transition('Backwaters Upper Lantern Cave', 'Backwaters Upper Lantern Pad', DirectionType.SOUTH, TransitionType.DOORS, True_()),
    'Backwaters Upper Lantern Pad_Backwaters Upper Lantern Cave': Transition('Backwaters Upper Lantern Pad', 'Backwaters Upper Lantern Cave', DirectionType.NORTH, TransitionType.DOORS, HasSparks(count=2) & HasLadder()),
    'Backwaters Upper Swamp Back East Transition': Transition('Backwaters Upper Swamp Back', 'Backwaters Upper Swamp Secret Room', DirectionType.EAST, TransitionType.SCREENS, True_()),
    'Backwaters Upper Swamp Entrance North Area Transition': Transition('Backwaters Upper Swamp Entrance', 'Western Wilds Western Pond', DirectionType.NORTH, TransitionType.AREA_SCREENS, True_()),
    'Backwaters Upper Swamp Lily East Locked Transition': Transition('Backwaters Upper Swamp Lily', 'Backwaters Pinky Outside', DirectionType.EAST, TransitionType.SCREENS, HasKear(kear=SingleKears.PINKY_KEAR.value)),
    'Backwaters Upper Swamp Lily South Transition': Transition('Backwaters Upper Swamp Lily', 'Backwaters Lower Swamp', DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    'Backwaters Upper Swamp Secret Room West Transition': Transition('Backwaters Upper Swamp Secret Room', 'Backwaters Upper Swamp Back', DirectionType.WEST, TransitionType.SCREENS, True_()),
}
