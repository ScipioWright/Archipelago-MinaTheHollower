# AUTO-GENERATED -- DO NOT EDIT.
# Regenerate from the spreadsheet export with:
#   python -m worlds.mina_the_hollower.tools.generate_edges <edges.csv>
# The spreadsheet is the source of truth, not this file.

from rule_builder.rules import Has, True_, CanReachLocation
from ... import RegionConnection, Transition, DirectionType, TransitionType
from ...rules.ability_rules import (
    CanBurrow, CanCarry, CanClimb, CanSwim, CanBounce,
    HasVialsCount, CanJumpOneTile, CanJumpTiles, ReachingSideArm,
)


regions: set[str] = {
    'Sandfalls Mining Outlook',
}

connections: dict[str, RegionConnection] = {
}

transitions: dict[str, Transition] = {
    'Sandfalls Mining Outlook': Transition('Sandfalls Mining Outlook', 'Southern Outskirts Four Flowers Sandfall', DirectionType.WEST, TransitionType.AREA_SCREENS),
    'Sandfalls Mining Outlook Cave Stairs': Transition('Sandfalls Mining Outlook', 'Southern Outskirts Mining Passage Exit', DirectionType.NORTH, TransitionType.STAIRS),
}
