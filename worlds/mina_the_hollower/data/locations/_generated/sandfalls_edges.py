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
    'Sandfalls Bone Junction',
    'Sandfalls Bone Junction Plank',
    'Sandfalls Bone Junction Sands',
    'Sandfalls Bone Junction Stair',
    'Sandfalls Miners Den',
    'Sandfalls Miners Den Entrance',
    'Sandfalls Miners Den Outskirt',
    'Sandfalls Miners Den Path',
    'Sandfalls Mining Outlook',
    'Sandfalls Pachinko',
    'Sandfalls Payload Passage',
    'Sandfalls Payload Passage Bottom',
    'Sandfalls Payload Passage Chest',
    'Sandfalls Ring Dive Parlor',
    'Sandfalls Sandwater Junction',
    'Sandfalls Sandwater Junction Top',
    'Sandfalls Sandy Station',
    'Sandfalls Shifty Seclusion',
    'Sandfalls Sifted Sands',
    'Sandfalls Sifted Sands Funnel',
    'Sandfalls Sifted Sands Hidden Cave',
    'Sandfalls Sifted Sands Hidden Left Bomb',
    'Sandfalls Spike Squares',
}

connections: dict[str, RegionConnection] = {
    'Sandfalls Bone Junction Sands_Sandfalls Sifted Sands': RegionConnection('Sandfalls Bone Junction Sands', 'Sandfalls Sifted Sands', True_()),
    'Sandfalls Bone Junction Stair_Sandfalls Bone Junction': RegionConnection('Sandfalls Bone Junction Stair', 'Sandfalls Bone Junction', CanBurrow() & HasRepairedShorelineGenerator() & CanCarry()),
    'Sandfalls Bone Junction_Sandfalls Bone Junction Stair': RegionConnection('Sandfalls Bone Junction', 'Sandfalls Bone Junction Stair', CanBurrow() & HasRepairedShorelineGenerator() & CanCarry()),
    'Sandfalls Payload Passage Bottom_Sandfalls Payload Passage Chest': RegionConnection('Sandfalls Payload Passage Bottom', 'Sandfalls Payload Passage Chest', CanJumpTiles(distance=2)),
    'Sandfalls Payload Passage Chest_Sandfalls Payload Passage Bottom': RegionConnection('Sandfalls Payload Passage Chest', 'Sandfalls Payload Passage Bottom', CanJumpTiles(distance=5)),
    'Sandfalls Sifted Sands Funnel_Sandfalls Sifted Sands': RegionConnection('Sandfalls Sifted Sands Funnel', 'Sandfalls Sifted Sands', CanClimb()),
    'Sandfalls Sifted Sands Hidden Left Bomb_Sandfalls Sifted Sands': RegionConnection('Sandfalls Sifted Sands Hidden Left Bomb', 'Sandfalls Sifted Sands', CanCarry()),
    'Sandfalls Sifted Sands_Sandfalls Sifted Sands Funnel': RegionConnection('Sandfalls Sifted Sands', 'Sandfalls Sifted Sands Funnel', True_()),
}

transitions: dict[str, Transition] = {
    'Sandfalls Bone Junction Burrow East': Transition('Sandfalls Bone Junction', 'Bone Beach Bone Rush Mine', DirectionType.EAST, TransitionType.BURROW, CanBurrow() & HasRepairedShorelineGenerator() & CanCarry()),
    'Sandfalls Bone Junction East Transition': Transition('Sandfalls Bone Junction', 'Bone Beach Shoreline Generator', DirectionType.EAST, TransitionType.SCREENS, True_()),
    'Sandfalls Bone Junction North Transition': Transition('Sandfalls Bone Junction Stair', 'Sandfalls Bone Junction Plank', DirectionType.NORTH, TransitionType.SCREENS, True_()),
    'Sandfalls Bone Junction Plank South Transition': Transition('Sandfalls Bone Junction Plank', 'Sandfalls Bone Junction Stair', DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    'Sandfalls Bone Junction Plank West Area Transition': Transition('Sandfalls Bone Junction Plank', "Mourner's Mile Spike Hell Sandfall", DirectionType.WEST, TransitionType.AREA_SCREENS, True_()),
    'Sandfalls Bone Junction Sands East Transition': Transition('Sandfalls Bone Junction Sands', 'Sandfalls Bone Junction', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_()),
    'Sandfalls Bone Junction West Transition': Transition('Sandfalls Bone Junction', 'Sandfalls Bone Junction Sands', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_()),
    'Sandfalls Miners Den Entrance East Transition': Transition('Sandfalls Miners Den Entrance', 'Sandfalls Miners Den Path', DirectionType.EAST, TransitionType.SCREENS, True_()),
    'Sandfalls Miners Den Entrance Exit': Transition('Sandfalls Miners Den Entrance', 'Sandfalls Sifted Sands', DirectionType.NORTH, TransitionType.STAIRS, CanClimb()),
    'Sandfalls Miners Den North Transition': Transition('Sandfalls Miners Den', 'Sandfalls Miners Den Path', DirectionType.NORTH, TransitionType.SCREENS, True_()),
    'Sandfalls Miners Den Outskirt North Transition': Transition('Sandfalls Miners Den Outskirt', 'Sandfalls Miners Den', DirectionType.NORTH, TransitionType.SCREENS, True_()),
    'Sandfalls Miners Den Outskirt Stairs': Transition('Sandfalls Miners Den Outskirt', 'Bone Beach Bone Rush Mine', DirectionType.NORTH, TransitionType.STAIRS, True_()),
    'Sandfalls Miners Den Path South Transition': Transition('Sandfalls Miners Den Path', 'Sandfalls Miners Den', DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    'Sandfalls Miners Den Path West Transition': Transition('Sandfalls Miners Den Path', 'Sandfalls Miners Den Entrance', DirectionType.WEST, TransitionType.SCREENS, True_()),
    'Sandfalls Miners Den South Transition': Transition('Sandfalls Miners Den', 'Sandfalls Miners Den Outskirt', DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    'Sandfalls Mining Outlook': Transition('Sandfalls Mining Outlook', 'Southern Outskirts Four Flowers Sandfall', DirectionType.WEST, TransitionType.AREA_SCREENS, True_()),
    'Sandfalls Mining Outlook Cave Stairs': Transition('Sandfalls Mining Outlook', 'Southern Outskirts Mining Passage Exit', DirectionType.NORTH, TransitionType.STAIRS, True_()),
    'Sandfalls Mining Outlook_Sandfalls Sifted Sands': Transition('Sandfalls Mining Outlook', 'Sandfalls Sifted Sands', DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    'Sandfalls Pachinko Exit': Transition('Sandfalls Pachinko', 'Sandfalls Sifted Sands', DirectionType.SOUTH, TransitionType.DOORS, True_()),
    'Sandfalls Payload Passage Bottom Burrow West': Transition('Sandfalls Payload Passage Bottom', 'Sandfalls Sandwater Junction Top', DirectionType.WEST, TransitionType.BURROW, CanBurrow()),
    'Sandfalls Payload Passage Chest East Burrow': Transition('Sandfalls Payload Passage Chest', 'Sandfalls Sifted Sands', DirectionType.EAST, TransitionType.BURROW, CanBurrow()),
    'Sandfalls Payload Passage East Burrow 1': Transition('Sandfalls Payload Passage', 'Sandfalls Sifted Sands', DirectionType.EAST, TransitionType.BURROW, CanBurrow()),
    'Sandfalls Payload Passage East Burrow 2': Transition('Sandfalls Payload Passage', 'Sandfalls Sifted Sands', DirectionType.EAST, TransitionType.BURROW, CanBurrow()),
    'Sandfalls Ring Dive Parlor Geyser Up': Transition('Sandfalls Ring Dive Parlor', 'Sandfalls Sifted Sands Funnel', DirectionType.OVERWORLD, TransitionType.GEYSER_UP, True_()),
    'Sandfalls Sandwater Junction North Rope': Transition('Sandfalls Sandwater Junction', 'Sandfalls Sandwater Junction Top', DirectionType.NORTH, TransitionType.SCREENS, CanClimb()),
    'Sandfalls Sandwater Junction South Rope': Transition('Sandfalls Sandwater Junction', "Loner's Landing Boardwalk Sandfalls Ledge", DirectionType.SOUTH, TransitionType.SCREENS, CanClimb()),
    'Sandfalls Sandwater Junction South Transition': Transition('Sandfalls Sandwater Junction', "Loner's Landing Boardwalk Sandfalls Lake", DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    'Sandfalls Sandwater Junction Top Burrow East': Transition('Sandfalls Sandwater Junction Top', 'Sandfalls Payload Passage Bottom', DirectionType.EAST, TransitionType.BURROW, CanBurrow()),
    'Sandfalls Sandwater Junction Top South Rope': Transition('Sandfalls Sandwater Junction Top', 'Sandfalls Sandwater Junction', DirectionType.SOUTH, TransitionType.SCREENS, CanClimb()),
    'Sandfalls Sandy Station North Transition': Transition('Sandfalls Sandy Station', 'Sandfalls Sifted Sands', DirectionType.NORTH, TransitionType.SCREENS, True_()),
    'Sandfalls Sandy Station Train': Transition('Sandfalls Sandy Station', 'Ossex Train Caboose', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has(PermanentUpgrades.TRAIN_PASS.value) & Has(PermanentUpgrades.BONE_BEACH_TICKET.value)),
    'Sandfalls Shifty Seclusion Exit': Transition('Sandfalls Shifty Seclusion', 'Sandfalls Sifted Sands', DirectionType.SOUTH, TransitionType.DOORS, True_()),
    'Sandfalls Sifted Sands Burrow West': Transition('Sandfalls Sifted Sands', 'Sandfalls Payload Passage Chest', DirectionType.WEST, TransitionType.BURROW, CanBurrow() & CanCarry()),
    'Sandfalls Sifted Sands Den Door': Transition('Sandfalls Sifted Sands', 'Sandfalls Miners Den Entrance', DirectionType.NORTH, TransitionType.STAIRS, HasVialsCount(count=3) & CanBurrow() & CanCarry()),
    'Sandfalls Sifted Sands East Moving Burrow': Transition('Sandfalls Sifted Sands', 'Sandfalls Sifted Sands Hidden Cave', DirectionType.EAST, TransitionType.BURROW, CanBurrow()),
    'Sandfalls Sifted Sands Funnel Geyser Down': Transition('Sandfalls Sifted Sands Funnel', 'Sandfalls Ring Dive Parlor', DirectionType.OVERWORLD, TransitionType.GEYSER_DOWN, True_()),
    'Sandfalls Sifted Sands Hidden Left Bomb South Transition': Transition('Sandfalls Sifted Sands Hidden Left Bomb', 'Sandfalls Spike Squares', DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    'Sandfalls Sifted Sands North Transition': Transition('Sandfalls Sifted Sands', 'Sandfalls Mining Outlook', DirectionType.NORTH, TransitionType.SCREENS, True_()),
    'Sandfalls Sifted Sands Pachinko Cave': Transition('Sandfalls Sifted Sands', 'Sandfalls Pachinko', DirectionType.NORTH, TransitionType.DOORS, CanBurrow() & CanCarry() & HasKear(kear=SingleKears.SANDFALL_CAVE_KEAR.value)),
    'Sandfalls Sifted Sands Payload West Burrow 1': Transition('Sandfalls Sifted Sands', 'Sandfalls Payload Passage', DirectionType.WEST, TransitionType.BURROW, CanBurrow()),
    'Sandfalls Sifted Sands Payload West Burrow 2': Transition('Sandfalls Sifted Sands', 'Sandfalls Payload Passage', DirectionType.WEST, TransitionType.BURROW, CanBurrow()),
    'Sandfalls Sifted Sands Shifty Cave': Transition('Sandfalls Sifted Sands', 'Sandfalls Shifty Seclusion', DirectionType.NORTH, TransitionType.DOORS, CanBurrow() & CanCarry()),
    'Sandfalls Sifted Sands South Burrow': Transition('Sandfalls Sifted Sands', 'Sandfalls Spike Squares', DirectionType.SOUTH, TransitionType.BURROW, CanBurrow()),
    'Sandfalls Sifted Sands South Transition': Transition('Sandfalls Sifted Sands', 'Sandfalls Sandy Station', DirectionType.SOUTH, TransitionType.SCREENS, CanBurrow() & CanCarry()),
    'Sandfalls Sifted Sands Under Burrow East': Transition('Sandfalls Sifted Sands Hidden Cave', 'Sandfalls Sifted Sands', DirectionType.EAST, TransitionType.BURROW, CanBurrow()),
    'Sandfalls Sifted Sands Under Burrow West': Transition('Sandfalls Sifted Sands Hidden Cave', 'Sandfalls Sifted Sands', DirectionType.WEST, TransitionType.BURROW, CanBurrow()),
    'Sandfalls Sifted Sands West Moving Burrow': Transition('Sandfalls Sifted Sands', 'Sandfalls Sifted Sands Hidden Cave', DirectionType.WEST, TransitionType.BURROW, CanBurrow()),
    'Sandfalls Spike Squares North Burrow': Transition('Sandfalls Spike Squares', 'Sandfalls Sifted Sands', DirectionType.NORTH, TransitionType.BURROW, CanBurrow()),
    'Sandfalls Spike Squares North Transition': Transition('Sandfalls Spike Squares', 'Sandfalls Sifted Sands Hidden Left Bomb', DirectionType.NORTH, TransitionType.SCREENS, True_()),
}
