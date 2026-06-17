# AUTO-GENERATED -- DO NOT EDIT.
# Regenerate from the spreadsheet export with:
#   python -m worlds.mina_the_hollower.tools.generate_edges <edges.csv>
# The spreadsheet is the source of truth, not this file.

from rule_builder.rules import Has, True_, CanReachLocation
from ... import RegionConnection, Transition, DirectionType, TransitionType
from ...rules.ability_rules import (
    CanBurrow, CanCarry, CanClimb, CanSwim, CanBounce,
    HasVialsCount, CanJumpOneTile, CanJumpTiles, HasReachingSideArm,
)
from ...rules.state_rules import (
   HasLadder,
)


regions: set[str] = {
    'Septemburg Tunnel Room',
}

connections: dict[str, RegionConnection] = {
}

transitions: dict[str, Transition] = {
    'Septemburg Tunnel Room Tunnel': Transition('Septemburg Tunnel Room', "Nox's Bayou Tainted Tunnel", DirectionType.SOUTH, TransitionType.DOORS),
}
