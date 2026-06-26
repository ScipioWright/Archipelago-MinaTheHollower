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
    'Kindlewood Behind Madd House',
    'Kindlewood Farm Crossing',
    'Kindlewood Farm Crossing Above School',
    'Kindlewood Farm Crossing Entrance',
    'Kindlewood Farm Crossing Pumpkin Patch',
    'Kindlewood Farm Crossing Shack',
    'Kindlewood Farm Crossing Shack Outside',
    'Kindlewood Farm Tomato',
    'Kindlewood Overgrowth Behind Residence',
    'Kindlewood Overgrowth Behind Residence Lawn',
    'Kindlewood Overgrowth Bonfire Left',
    'Kindlewood Overgrowth Bonfire Main',
    'Kindlewood Overgrowth Bonfire Top',
    'Kindlewood Overgrowth Entry Main',
    'Kindlewood Overgrowth Entry Upper Left',
    'Kindlewood Overgrowth Madd Arena',
    'Kindlewood Overgrowth Madd House',
    'Kindlewood Overgrowth Residence Barn',
    'Kindlewood Overgrowth Residence Barn Burrow',
    'Kindlewood Overgrowth Residence Basement',
    'Kindlewood Overgrowth Residence Yard',
    'Kindlewood Rail Tunnel',
    'Kindlewood Rail Tunnel Tracks',
    'Kindlewood School',
    'Kindlewood School Backyard',
    'Kindlewood School Side',
    'Kindlewood School Yard',
    'Kindlewood Train Tracks',
    "Kindlewood Wallower's Path Cliff Bush",
    'Kindlewood Wallowers Path',
    'Kindlewood Wallowers Path End',
}

connections: dict[str, RegionConnection] = {
    'Kindlewood Farm Crossing Entrance_Kindlewood Farm Crossing': RegionConnection('Kindlewood Farm Crossing Entrance', 'Kindlewood Farm Crossing', CanBurrow()),
    'Kindlewood Farm Crossing Entrance_Kindlewood Farm Crossing Pumpkin Patch': RegionConnection('Kindlewood Farm Crossing Entrance', 'Kindlewood Farm Crossing Pumpkin Patch', CanBurrow()),
    'Kindlewood Farm Crossing Pumpkin Patch_Kindlewood Farm Crossing Entrance': RegionConnection('Kindlewood Farm Crossing Pumpkin Patch', 'Kindlewood Farm Crossing Entrance', CanBurrow()),
    'Kindlewood Farm Crossing Shack Outside_Kindlewood Farm Tomato': RegionConnection('Kindlewood Farm Crossing Shack Outside', 'Kindlewood Farm Tomato', HasKear(kear=SingleKears.KINDLEWOOD_TOMATO_PATCH_KEAR.value)),
    'Kindlewood Farm Crossing_Kindlewood Farm Crossing Entrance': RegionConnection('Kindlewood Farm Crossing', 'Kindlewood Farm Crossing Entrance', CanBurrow()),
    'Kindlewood Farm Tomato_Kindlewood Farm Crossing Shack Outside': RegionConnection('Kindlewood Farm Tomato', 'Kindlewood Farm Crossing Shack Outside', HasKear(kear=SingleKears.KINDLEWOOD_TOMATO_PATCH_KEAR.value)),
    'Kindlewood Farm Tomato_Kindlewood Train Tracks': RegionConnection('Kindlewood Farm Tomato', 'Kindlewood Train Tracks', CanBurrow()),
    'Kindlewood Overgrowth Behind Residence Lawn_Kindlewood Overgrowth Behind Residence': RegionConnection('Kindlewood Overgrowth Behind Residence Lawn', 'Kindlewood Overgrowth Behind Residence', CanCarry()),
    'Kindlewood Overgrowth Behind Residence_Kindlewood Overgrowth Behind Residence Lawn': RegionConnection('Kindlewood Overgrowth Behind Residence', 'Kindlewood Overgrowth Behind Residence Lawn', True_()),
    'Kindlewood Overgrowth Bonfire Left_Kindlewood Overgrowth Bonfire Main': RegionConnection('Kindlewood Overgrowth Bonfire Left', 'Kindlewood Overgrowth Bonfire Main', CanBurrow()),
    'Kindlewood Overgrowth Bonfire Main_Kindlewood Overgrowth Bonfire Left': RegionConnection('Kindlewood Overgrowth Bonfire Main', 'Kindlewood Overgrowth Bonfire Left', CanBurrow()),
    'Kindlewood Overgrowth Bonfire Top_Kindlewood Overgrowth Bonfire Left': RegionConnection('Kindlewood Overgrowth Bonfire Top', 'Kindlewood Overgrowth Bonfire Left', CanBurrow()),
    'Kindlewood Overgrowth Entry Main_Kindlewood Overgrowth Entry Upper Left': RegionConnection('Kindlewood Overgrowth Entry Main', 'Kindlewood Overgrowth Entry Upper Left', True_()),
    'Kindlewood Overgrowth Residence Barn Burrow_Kindlewood Overgrowth Residence Barn': RegionConnection('Kindlewood Overgrowth Residence Barn Burrow', 'Kindlewood Overgrowth Residence Barn', CanClimb()),
    'Kindlewood Overgrowth Residence Barn_Kindlewood Overgrowth Residence Barn Burrow': RegionConnection('Kindlewood Overgrowth Residence Barn', 'Kindlewood Overgrowth Residence Barn Burrow', CanCarry()),
    'Kindlewood Rail Tunnel Tracks_Kindlewood Rail Tunnel': RegionConnection('Kindlewood Rail Tunnel Tracks', 'Kindlewood Rail Tunnel', CanBurrow() & CanClimb()),
    'Kindlewood Rail Tunnel_Kindlewood Rail Tunnel Tracks': RegionConnection('Kindlewood Rail Tunnel', 'Kindlewood Rail Tunnel Tracks', CanBurrow() & CanClimb()),
    'Kindlewood Wallowers Path End_Kindlewood Wallowers Path': RegionConnection('Kindlewood Wallowers Path End', 'Kindlewood Wallowers Path', CanBurrow()),
    "Kindlewood Wallowers Path_Kindlewood Wallower's Path Cliff Bush": RegionConnection('Kindlewood Wallowers Path', "Kindlewood Wallower's Path Cliff Bush", CanBurrow()),
    'Kindlewood Wallowers Path_Kindlewood Wallowers Path End': RegionConnection('Kindlewood Wallowers Path', 'Kindlewood Wallowers Path End', Has(Trinkets.WALLOWERS_GAUNTLETS.value) | CanJumpTiles(distance=7)),
}

transitions: dict[str, Transition] = {
    'Kindlewood Behind Madd House South Burrow': Transition('Kindlewood Behind Madd House', 'Kindlewood Overgrowth Madd Arena', DirectionType.SOUTH, TransitionType.BURROW, PowerLevelThreshold(power=25)),
    'Kindlewood Farm Crossing Above School East Burrow': Transition('Kindlewood Farm Crossing Above School', 'Kindlewood Farm Crossing Pumpkin Patch', DirectionType.EAST, TransitionType.BURROW, CanBurrow()),
    'Kindlewood Farm Crossing Do_Not_Randomize_Entrance': Transition('Kindlewood Farm Crossing', 'Ossex Train Caboose', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has(PermanentUpgrades.TRAIN_PASS.value) & Has(PermanentUpgrades.SEPTEMBURG_TICKET.value)),
    'Kindlewood Farm Crossing Pumpkin Patch North Burrow': Transition('Kindlewood Farm Crossing Pumpkin Patch', 'Kindlewood Farm Crossing Shack', DirectionType.NORTH, TransitionType.BURROW, CanBurrow()),
    'Kindlewood Farm Crossing Pumpkin Patch West Burrow': Transition('Kindlewood Farm Crossing Pumpkin Patch', 'Kindlewood Farm Crossing Above School', DirectionType.WEST, TransitionType.BURROW, CanBurrow()),
    'Kindlewood Farm Crossing Shack East Burrow': Transition('Kindlewood Farm Crossing Shack', 'Kindlewood Farm Crossing Shack Outside', DirectionType.EAST, TransitionType.BURROW, CanBurrow()),
    'Kindlewood Farm Crossing Shack Outside West Burrow': Transition('Kindlewood Farm Crossing Shack Outside', 'Kindlewood Farm Crossing Shack', DirectionType.WEST, TransitionType.BURROW, CanBurrow()),
    'Kindlewood Farm Crossing Shack South Burrow': Transition('Kindlewood Farm Crossing Shack', 'Kindlewood Farm Crossing Pumpkin Patch', DirectionType.SOUTH, TransitionType.BURROW, CanBurrow()),
    'Kindlewood Farm Crossing South Burrow': Transition('Kindlewood Farm Crossing', 'Kindlewood Wallowers Path', DirectionType.SOUTH, TransitionType.BURROW, True_()),
    'Kindlewood Farm Crossing West Transition': Transition('Kindlewood Farm Crossing', 'Kindlewood School Yard', DirectionType.WEST, TransitionType.SCREENS, True_()),
    'Kindlewood Farm Tomato Pipe': Transition('Kindlewood Farm Tomato', 'Kindlewood Farm Crossing Pumpkin Patch', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, True_()),
    'Kindlewood Overgrowth Behind Residence Lawn South Burrow': Transition('Kindlewood Overgrowth Behind Residence Lawn', 'Kindlewood Overgrowth Residence Barn Burrow', DirectionType.SOUTH, TransitionType.BURROW, CanBurrow()),
    'Kindlewood Overgrowth Behind Residence West Transition': Transition('Kindlewood Overgrowth Behind Residence', 'Kindlewood Overgrowth Bonfire Top', DirectionType.WEST, TransitionType.SCREENS, True_()),
    'Kindlewood Overgrowth Bonfire Left South Burrow': Transition('Kindlewood Overgrowth Bonfire Left', 'Kindlewood Overgrowth Entry Upper Left', DirectionType.SOUTH, TransitionType.BURROW, CanBurrow()),
    'Kindlewood Overgrowth Bonfire Left West Burrow': Transition('Kindlewood Overgrowth Bonfire Left', "Kindlewood Wallower's Path Cliff Bush", DirectionType.WEST, TransitionType.BURROW, CanBurrow()),
    'Kindlewood Overgrowth Bonfire Main East Transition': Transition('Kindlewood Overgrowth Bonfire Main', 'Kindlewood Overgrowth Residence Yard', DirectionType.EAST, TransitionType.SCREENS, True_()),
    'Kindlewood Overgrowth Bonfire Top East Transition': Transition('Kindlewood Overgrowth Bonfire Top', 'Kindlewood Overgrowth Behind Residence', DirectionType.EAST, TransitionType.SCREENS, True_()),
    'Kindlewood Overgrowth Bonfire Top North Transition': Transition('Kindlewood Overgrowth Bonfire Top', 'Kindlewood Overgrowth Madd Arena', DirectionType.NORTH, TransitionType.SCREENS, True_()),
    'Kindlewood Overgrowth Entry Main East Area Transition': Transition('Kindlewood Overgrowth Entry Main', 'Western Wilds Brutes', DirectionType.EAST, TransitionType.AREA_SCREENS, CanBurrow()),
    'Kindlewood Overgrowth Entry Upper Left North Burrow': Transition('Kindlewood Overgrowth Entry Upper Left', 'Kindlewood Overgrowth Bonfire Left', DirectionType.NORTH, TransitionType.BURROW, CanBurrow()),
    'Kindlewood Overgrowth Madd Arena Bottom West Transition': Transition('Kindlewood Overgrowth Madd Arena', 'Kindlewood Farm Crossing Entrance', DirectionType.WEST, TransitionType.SCREENS, PowerLevelThreshold(power=25)),
    'Kindlewood Overgrowth Madd Arena Doors': Transition('Kindlewood Overgrowth Madd Arena', 'Kindlewood Overgrowth Madd House', DirectionType.NORTH, TransitionType.DOORS, PowerLevelThreshold(power=25)),
    'Kindlewood Overgrowth Madd Arena North Burrow': Transition('Kindlewood Overgrowth Madd Arena', 'Kindlewood Behind Madd House', DirectionType.NORTH, TransitionType.BURROW, CanCarry() & CanBurrow() & HasAccessToTorch() & PowerLevelThreshold(power=25)),
    'Kindlewood Overgrowth Madd Arena South Transition': Transition('Kindlewood Overgrowth Madd Arena', 'Kindlewood Overgrowth Bonfire Top', DirectionType.SOUTH, TransitionType.SCREENS, PowerLevelThreshold(power=25)),
    'Kindlewood Overgrowth Madd Arena Top West Transition': Transition('Kindlewood Overgrowth Madd Arena', 'Kindlewood Farm Crossing Entrance', DirectionType.WEST, TransitionType.SCREENS, PowerLevelThreshold(power=25)),
    'Kindlewood Overgrowth Madd House Doors': Transition('Kindlewood Overgrowth Madd House', 'Kindlewood Overgrowth Madd Arena', DirectionType.SOUTH, TransitionType.DOORS, True_()),
    'Kindlewood Overgrowth Residence Barn Burrow North Burrow': Transition('Kindlewood Overgrowth Residence Barn Burrow', 'Kindlewood Overgrowth Behind Residence Lawn', DirectionType.NORTH, TransitionType.BURROW, CanBurrow()),
    'Kindlewood Overgrowth Residence Barn Doors': Transition('Kindlewood Overgrowth Residence Barn', 'Kindlewood Overgrowth Residence Yard', DirectionType.SOUTH, TransitionType.DOORS, True_()),
    'Kindlewood Overgrowth Residence Barn Geyser_Down': Transition('Kindlewood Overgrowth Residence Barn', 'Kindlewood Overgrowth Residence Basement', DirectionType.OVERWORLD, TransitionType.GEYSER_DOWN, CanCarry()),
    'Kindlewood Overgrowth Residence Basement Geyser_Up': Transition('Kindlewood Overgrowth Residence Basement', 'Kindlewood Overgrowth Residence Barn', DirectionType.OVERWORLD, TransitionType.GEYSER_UP, True_()),
    'Kindlewood Overgrowth Residence Yard Doors': Transition('Kindlewood Overgrowth Residence Yard', 'Kindlewood Overgrowth Residence Barn', DirectionType.NORTH, TransitionType.DOORS, True_()),
    'Kindlewood Overgrowth Residence Yard West Transition': Transition('Kindlewood Overgrowth Residence Yard', 'Kindlewood Overgrowth Bonfire Main', DirectionType.WEST, TransitionType.SCREENS, True_()),
    'Kindlewood Rail Tunnel Tracks West Transition': Transition('Kindlewood Rail Tunnel Tracks', 'Kindlewood Train Tracks', DirectionType.WEST, TransitionType.SCREENS, True_()),
    'Kindlewood School Backyard Doors': Transition('Kindlewood School Backyard', 'Kindlewood School Side', DirectionType.NORTH, TransitionType.DOORS, True_()),
    'Kindlewood School Backyard Stairs': Transition('Kindlewood School Backyard', 'Septemburg Wastewater Canal Well Entrance', DirectionType.NORTH, TransitionType.STAIRS, True_()),
    'Kindlewood School Doors': Transition('Kindlewood School', 'Kindlewood School Yard', DirectionType.SOUTH, TransitionType.DOORS, True_()),
    'Kindlewood School Side Doors': Transition('Kindlewood School Side', 'Kindlewood School Backyard', DirectionType.SOUTH, TransitionType.DOORS, True_()),
    'Kindlewood School Side East Burrow': Transition('Kindlewood School Side', 'Kindlewood School', DirectionType.EAST, TransitionType.BURROW, True_()),
    'Kindlewood School West Burrow': Transition('Kindlewood School', 'Kindlewood School Side', DirectionType.WEST, TransitionType.BURROW, True_()),
    'Kindlewood School Yard Doors': Transition('Kindlewood School Yard', 'Kindlewood School', DirectionType.NORTH, TransitionType.DOORS, True_()),
    'Kindlewood School Yard East Transition': Transition('Kindlewood School Yard', 'Kindlewood Farm Crossing', DirectionType.EAST, TransitionType.SCREENS, True_()),
    'Kindlewood School Yard West Area Transition': Transition('Kindlewood School Yard', 'Septemburg Withered Farms Start East', DirectionType.WEST, TransitionType.AREA_SCREENS, True_()),
    'Kindlewood Train Tracks East Transition': Transition('Kindlewood Train Tracks', 'Kindlewood Rail Tunnel Tracks', DirectionType.EAST, TransitionType.SCREENS, True_()),
    "Kindlewood Wallower's Path Cliff Bush East Burrow": Transition("Kindlewood Wallower's Path Cliff Bush", 'Kindlewood Overgrowth Bonfire Left', DirectionType.EAST, TransitionType.BURROW, True_()),
    'Kindlewood Wallowers Path North Burrow': Transition('Kindlewood Wallowers Path', 'Kindlewood Farm Crossing', DirectionType.NORTH, TransitionType.BURROW, True_()),
}
