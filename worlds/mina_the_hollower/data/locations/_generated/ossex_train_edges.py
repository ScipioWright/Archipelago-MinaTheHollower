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
   HasLadder, HasCompletedBoneGenerator, HasAccessToTorch, HasDoneColtraneGenerator,
   AnyThreeAstralPlatforms, CompletedAllGenerators, InFinale
)


regions: set[str] = {
    'Ossex Train Cab',
    'Ossex Train Caboose',
    'Ossex Train Coupling',
    'Ossex Train Interior',
    'Ossex Train Private Cabin Left',
    'Ossex Train Private Cabin Middle',
    'Ossex Train Private Cabin Right',
}

connections: dict[str, RegionConnection] = {
}

transitions: dict[str, Transition] = {
    'Bayou Stop': Transition('Ossex Train Interior', 'Backwaters Lower Swamp Station', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has("BayouTicket")),
    'Bayou Stop 2': Transition('Ossex Train Cab', 'Ossex Station', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has("HUBTicket")),
    'Bayou Stop 2': Transition('Ossex Train Cab', 'Backwaters Lower Swamp Station', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has("BayouTicket")),
    'Coltrane Peak Stop': Transition('Ossex Train Interior', 'Coltrane Peak Thorne Arena', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has("FrozenTrainyardTicket")),
    'Coltrane Peak Stop 2': Transition('Ossex Train Cab', 'Coltrane Peak Thorne Arena', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has("FrozenTrainyardTicket")),
    'Kindlewood Stop': Transition('Ossex Train Interior', 'Kindlewood Farm Crossing', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has("SeptemburgTicket")),
    'Kindlewood Stop 2': Transition('Ossex Train Cab', 'Kindlewood Farm Crossing', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has("SeptemburgTicket")),
    'Ossex Stop': Transition('Ossex Train Interior', 'Ossex Station', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has("HUBTicket")),
    'Ossex Train Cab Left Exit': Transition('Ossex Train Cab', 'Ossex Train Coupling', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE),
    'Ossex Train Caboose East Transition': Transition('Ossex Train Caboose', 'Ossex Train Interior', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE),
    'Ossex Train Coupling East Exit': Transition('Ossex Train Coupling', 'Ossex Train Cab', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE),
    'Ossex Train Coupling West Exit': Transition('Ossex Train Coupling', 'Ossex Train Interior', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE),
    'Ossex Train Interior Cabin Door': Transition('Ossex Train Interior', 'Ossex Train Private Cabin Middle', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE),
    'Ossex Train Interior East Exit': Transition('Ossex Train Interior', 'Ossex Train Coupling', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE),
    'Ossex Train Interior Sneaky Burrow': Transition('Ossex Train Interior', 'Ossex Train Private Cabin Right', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, CanBurrow()),
    'Ossex Train Interior West Transition': Transition('Ossex Train Interior', 'Ossex Train Caboose', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE),
    'Ossex Train Private Cabin Left Burrow': Transition('Ossex Train Private Cabin Left', 'Ossex Train Private Cabin Right', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, CanBurrow()),
    'Ossex Train Private Cabin Middle Exit': Transition('Ossex Train Private Cabin Middle', 'Ossex Train Interior', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE),
    'Ossex Train Private Cabin Right Burrow': Transition('Ossex Train Private Cabin Right', 'Ossex Train Private Cabin Left', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, CanBurrow()),
    'Ossex Train Private Cabin Right Sneaky Burrow': Transition('Ossex Train Private Cabin Right', 'Ossex Train Interior', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, CanBurrow()),
    'Sandfalls Stop': Transition('Ossex Train Interior', 'Sandfalls Sandy Station', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has("BoneBeachTicket")),
    'Sandfalls Stop 2': Transition('Ossex Train Cab', 'Sandfalls Sandy Station', DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, Has("BoneBeachTicket")),
}
