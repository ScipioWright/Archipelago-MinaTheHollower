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
    'Ossex Western Wall',
    'Western Wilds Balcony',
    'Western Wilds Balcony Path',
    'Western Wilds Brutes',
    'Western Wilds End',
    'Western Wilds Foundry Path',
    'Western Wilds Foundry Path Door',
    'Western Wilds Lava',
    'Western Wilds Main',
    'Western Wilds Molten Dungeon End',
    'Western Wilds Molten Dungeon Entrance',
    'Western Wilds Molten Dungeon Fences',
    'Western Wilds Molten Dungeon Middle',
    'Western Wilds Molten Dungeon Moving',
    'Western Wilds Molten Foundry Dark',
    'Western Wilds Molten Foundry Dark Poppit',
    'Western Wilds Molten Foundry Main',
    'Western Wilds Molten Foundry Secret',
    'Western Wilds Occupied Bridge',
    'Western Wilds Ossex Bridge',
    'Western Wilds Overgrown Path',
    'Western Wilds Secret Passageway East',
    'Western Wilds Secret Passageway West',
    'Western Wilds Western Pond',
}

connections: dict[str, RegionConnection] = {
    'Ossex Western Wall_Western Wilds Overgrown Path': RegionConnection('Ossex Western Wall', 'Western Wilds Overgrown Path', True_()),
    'Western Wilds Balcony Path_Western Wilds Main': RegionConnection('Western Wilds Balcony Path', 'Western Wilds Main', CanBurrow()),
    'Western Wilds Brutes_Western Wilds Lava': RegionConnection('Western Wilds Brutes', 'Western Wilds Lava', True_()),
    'Western Wilds End_Western Wilds Lava': RegionConnection('Western Wilds End', 'Western Wilds Lava', CanBurrow()),
    'Western Wilds Foundry Path_Western Wilds Foundry Path Door': RegionConnection('Western Wilds Foundry Path', 'Western Wilds Foundry Path Door', CanJumpTiles(distance=2)),
    'Western Wilds Foundry Path_Western Wilds Main': RegionConnection('Western Wilds Foundry Path', 'Western Wilds Main', CanBurrow()),
    'Western Wilds Lava_Western Wilds End': RegionConnection('Western Wilds Lava', 'Western Wilds End', CanBurrow()),
    'Western Wilds Lava_Western Wilds Main': RegionConnection('Western Wilds Lava', 'Western Wilds Main', CanBurrow()),
    'Western Wilds Main_Western Wilds Balcony Path': RegionConnection('Western Wilds Main', 'Western Wilds Balcony Path', CanBurrow()),
    'Western Wilds Main_Western Wilds Foundry Path': RegionConnection('Western Wilds Main', 'Western Wilds Foundry Path', CanBurrow()),
    'Western Wilds Main_Western Wilds Lava': RegionConnection('Western Wilds Main', 'Western Wilds Lava', CanBurrow()),
    'Western Wilds Molten Dungeon End_Western Wilds Molten Dungeon Entrance': RegionConnection('Western Wilds Molten Dungeon End', 'Western Wilds Molten Dungeon Entrance', True_()),
    'Western Wilds Molten Dungeon Fences_Western Wilds Molten Dungeon Middle': RegionConnection('Western Wilds Molten Dungeon Fences', 'Western Wilds Molten Dungeon Middle', CanBurrow()),
    'Western Wilds Molten Dungeon Middle_Western Wilds Molten Dungeon Fences': RegionConnection('Western Wilds Molten Dungeon Middle', 'Western Wilds Molten Dungeon Fences', CanBurrow()),
    'Western Wilds Molten Foundry Dark Poppit_Western Wilds Molten Foundry Dark': RegionConnection('Western Wilds Molten Foundry Dark Poppit', 'Western Wilds Molten Foundry Dark', True_()),
    'Western Wilds Molten Foundry Dark_Western Wilds Molten Foundry Dark Poppit': RegionConnection('Western Wilds Molten Foundry Dark', 'Western Wilds Molten Foundry Dark Poppit', CanBurrow()),
    'Western Wilds Molten Foundry Main_Western Wilds Molten Foundry Secret': RegionConnection('Western Wilds Molten Foundry Main', 'Western Wilds Molten Foundry Secret', CanBurrow()),
    'Western Wilds Molten Foundry Secret_Western Wilds Molten Foundry Main': RegionConnection('Western Wilds Molten Foundry Secret', 'Western Wilds Molten Foundry Main', CanBurrow()),
    'Western Wilds Occupied Bridge_Western Wilds Brutes': RegionConnection('Western Wilds Occupied Bridge', 'Western Wilds Brutes', True_()),
    'Western Wilds Occupied Bridge_Western Wilds Ossex Bridge': RegionConnection('Western Wilds Occupied Bridge', 'Western Wilds Ossex Bridge', CanBurrow()),
    'Western Wilds Ossex Bridge_Western Wilds Main': RegionConnection('Western Wilds Ossex Bridge', 'Western Wilds Main', True_()),
    'Western Wilds Ossex Bridge_Western Wilds Occupied Bridge': RegionConnection('Western Wilds Ossex Bridge', 'Western Wilds Occupied Bridge', CanBurrow()),
    'Western Wilds Secret Passageway East_Western Wilds Secret Passageway West': RegionConnection('Western Wilds Secret Passageway East', 'Western Wilds Secret Passageway West', CanJumpTiles(distance=3)),
    'Western Wilds Secret Passageway West_Western Wilds Secret Passageway East': RegionConnection('Western Wilds Secret Passageway West', 'Western Wilds Secret Passageway East', CanJumpTiles(distance=3)),
    'Western Wilds Western Pond_Western Wilds End': RegionConnection('Western Wilds Western Pond', 'Western Wilds End', True_()),
}

transitions: dict[str, Transition] = {
    'Ossex Western Wall North Burrow': Transition('Ossex Western Wall', 'Ossex Bowery Begger Residence Back Corner', DirectionType.NORTH, TransitionType.BURROW, CanBurrow()),
    'Ossex Western Wall South Burrow': Transition('Ossex Western Wall', 'Ossex South Western Wall', DirectionType.SOUTH, TransitionType.BURROW, CanBurrow()),
    'Western Wilds Balcony Path North Transition': Transition('Western Wilds Balcony Path', 'Western Wilds Balcony', DirectionType.NORTH, TransitionType.SCREENS, True_()),
    'Western Wilds Balcony South Transition': Transition('Western Wilds Balcony', 'Western Wilds Balcony Path', DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    'Western Wilds Brutes East Area Transition': Transition('Western Wilds Brutes', 'Kindlewood Overgrowth Entry Main', DirectionType.WEST, TransitionType.AREA_SCREENS, True_()),
    'Western Wilds End South Transition': Transition('Western Wilds End', 'Western Wilds Western Pond', DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    'Western Wilds Foundry Path North Door': Transition('Western Wilds Foundry Path Door', 'Western Wilds Molten Foundry Main', DirectionType.NORTH, TransitionType.DOORS, True_()),
    'Western Wilds Main South Transition': Transition('Western Wilds Main', 'Western Wilds Overgrown Path', DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    'Western Wilds Molten Dungeon End West Transition': Transition('Western Wilds Molten Dungeon End', 'Western Wilds Molten Dungeon Moving', DirectionType.WEST, TransitionType.SCREENS, True_()),
    'Western Wilds Molten Dungeon Entrance South Transition': Transition('Western Wilds Molten Dungeon Entrance', 'Western Wilds Molten Dungeon Fences', DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    'Western Wilds Molten Dungeon Entrance Stairs': Transition('Western Wilds Molten Dungeon Entrance', 'Western Wilds Molten Foundry Dark', DirectionType.NORTH, TransitionType.STAIRS, HasKear(kear=SingleKears.WESTERN_WILDS_FOUNDRY_KEAR.value)),
    'Western Wilds Molten Dungeon Fences North Transition': Transition('Western Wilds Molten Dungeon Fences', 'Western Wilds Molten Dungeon Entrance', DirectionType.NORTH, TransitionType.SCREENS, True_()),
    'Western Wilds Molten Dungeon Middle North Transition': Transition('Western Wilds Molten Dungeon Middle', 'Western Wilds Molten Dungeon Moving', DirectionType.NORTH, TransitionType.SCREENS, True_()),
    'Western Wilds Molten Dungeon Moving East Transition': Transition('Western Wilds Molten Dungeon Moving', 'Western Wilds Molten Dungeon End', DirectionType.EAST, TransitionType.SCREENS, True_()),
    'Western Wilds Molten Dungeon Moving South Transition': Transition('Western Wilds Molten Dungeon Moving', 'Western Wilds Molten Dungeon Middle', DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    'Western Wilds Molten Foundry Dark South Transition': Transition('Western Wilds Molten Foundry Dark', 'Western Wilds Molten Foundry Secret', DirectionType.SOUTH, TransitionType.SCREENS, True_()),
    'Western Wilds Molten Foundry Dark Stairs': Transition('Western Wilds Molten Foundry Dark', 'Western Wilds Molten Dungeon Entrance', DirectionType.NORTH, TransitionType.STAIRS, HasKear(kear=SingleKears.WESTERN_WILDS_FOUNDRY_KEAR.value)),
    'Western Wilds Molten Foundry Main South Transition East': Transition('Western Wilds Molten Foundry Main', 'Western Wilds Ossex Bridge', DirectionType.SOUTH, TransitionType.DOORS, True_()),
    'Western Wilds Molten Foundry Main South Transition West': Transition('Western Wilds Molten Foundry Main', 'Western Wilds Foundry Path', DirectionType.SOUTH, TransitionType.DOORS, True_()),
    'Western Wilds Molten Foundry Secret North Transition': Transition('Western Wilds Molten Foundry Secret', 'Western Wilds Molten Foundry Dark', DirectionType.NORTH, TransitionType.SCREENS, True_()),
    'Western Wilds Ossex Bridge Door': Transition('Western Wilds Ossex Bridge', 'Western Wilds Molten Foundry Main', DirectionType.NORTH, TransitionType.DOORS, True_()),
    'Western Wilds Ossex Bridge East Transition': Transition('Western Wilds Ossex Bridge', 'Ossex Bowery Upper', DirectionType.EAST, TransitionType.AREA_SCREENS, True_()),
    'Western Wilds Overgrown Path North Transition': Transition('Western Wilds Overgrown Path', 'Western Wilds Main', DirectionType.NORTH, TransitionType.SCREENS, True_()),
    'Western Wilds Overgrown Path Secret Pool Geyser': Transition('Western Wilds Overgrown Path', 'Western Wilds Secret Passageway East', DirectionType.OVERWORLD, TransitionType.GEYSER_DOWN, True_()),
    'Western Wilds Overgrown Path South Transition': Transition('Western Wilds Overgrown Path', 'Southern Outskirts Commons Western Pit Room Main', DirectionType.SOUTH, TransitionType.AREA_SCREENS, True_()),
    'Western Wilds Secret Passage East Geyser Up': Transition('Western Wilds Secret Passageway East', 'Western Wilds Overgrown Path', DirectionType.OVERWORLD, TransitionType.GEYSER_UP, True_()),
    'Western Wilds Secret Passage West Geyser Up': Transition('Western Wilds Secret Passageway West', 'Western Wilds Western Pond', DirectionType.OVERWORLD, TransitionType.GEYSER_UP, True_()),
    'Western Wilds Western Pond Secret Pool Geyser': Transition('Western Wilds Western Pond', 'Western Wilds Secret Passageway West', DirectionType.OVERWORLD, TransitionType.GEYSER_DOWN, True_()),
    'Western Wilds Western Pond South Area Transition': Transition('Western Wilds Western Pond', 'Backwaters Upper Swamp Entrance', DirectionType.SOUTH, TransitionType.AREA_SCREENS, True_()),
}
