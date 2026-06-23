from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from ... import RegionConnection, Transition, LocationData, TransitionType, DirectionType
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanJumpTiles, CanBounce, HasVialsCount, CanClimb

collectable_locations: dict[str, LocationData] = {
    "SO Commons Ossex Entry Left Chest" : LocationData(270, "Ossex Entry Western Wall Chest"),
    "SO Commons Ossex Entry Right Chest" : LocationData(266, "Ossex Entry Eastern Wall Chest"),
    "SO Commons Chest" : LocationData(264, "Southern Outskirts Commons Main", CanBurrow() & CanBounce()),
    "SO Commons Crumblefin Head" : LocationData(274, "Southern Outskirts Commons Cliff"),
    "SO Cave Network Chest" : LocationData(265, "Southern Outskirts Cave Network Deep Exit"),
    "SO Cave Network Side Room Chest" : LocationData(268, "Southern Outskirts Cave Deep Arena"),
    "SO Poppit Keri" : LocationData(272, "Southern Outskirts Poppit"),
    "SO Poppit Kear" : LocationData(273, "Southern Outskirts Poppit"),
    "SO Southern Pit Room Bonestone" : LocationData(261, "Southern Outskirts Commons Southern Pit Room Main", CanJumpTiles(distance=5)),
    "SO Western Pit Room Chest" : LocationData(267, "Southern Outskirts Commons Western Pit Room Main"),
    "SO Residence Trinket" : LocationData(269, "Southern Outskirts Residence Basement"),
    "SO Mining Passage Chest" : LocationData(331, "Southern Outskirts Mining Passage Secret"),
    "SO Moonbath Lace Glove" : LocationData(263, "Southern Outskirts Moonbath"),
    "SO Four Flowers Chest" : LocationData(271, "Southern Outskirts Four Flowers Shortcut", CanBurrow() & CanBounce()),
}

boss_locations: dict[str, LocationData] = {
    "SO Moonbath Dugin #1" : LocationData(None, "Southern Outskirts Moonbath"),
    "SO Moonbath Dugin #2" : LocationData(None, "Southern Outskirts Moonbath"),
}
