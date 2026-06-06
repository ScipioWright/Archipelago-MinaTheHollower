from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from .. import LocationData
from ... import RegionConnectionData
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanJumpTiles, CanBounce

collectable_locations: dict[str, LocationData] = {
    "SO Commons Ossex Entry Right Chest" : LocationData(261, "Southern Outskirts", CanJumpOneTile() & CanBurrow() & ("SO Commons Ossex Entry Right Chest Kear")),
    "Trinket_LaceGlove" : LocationData(263, "Southern Outskirts"),
    "SO Cave Network Side Room Chest" : LocationData(264, "Southern Outskirts",
             CanJumpOneTile() & CanBounce() & CanBurrow() & Has("SO Cave Network Side Room Chest Kear")),
    "SO Cave Network Chest" : LocationData(265, "Southern Outskirts", Has("SO Cave Network Chest Kear")),
    "SO Southern Pit Room Bonestone" : LocationData(266, "Southern Outskirts", CanJumpTiles(distance=5)),
    "SO Commons Chest" : LocationData(267, "Southern Outskirts", CanJumpOneTile() & CanBounce() & CanBurrow()),
    "SO Western Pit Room Chest" : LocationData(268, "Southern Outskirts", CanJumpOneTile() | CanJumpTiles(distance=3) ),
    "SO Residence Primed Vial Pouch" : LocationData(269, "Southern Outskirts", CanJumpOneTile() & CanBurrow()),
    "SO Commons Ossex Entry Left Chest" : LocationData(270, "Southern Outskirts", CanJumpOneTile() & CanBurrow()),
    "SO Bonestone_04" : LocationData(271, "Southern Outskirts"),
    "SO Poppit Keri" : LocationData(272, "Southern Outskirts",CanJumpOneTile() & CanBounce() & CanBurrow() ),
    "SO Poppit Kear" : LocationData(273, "Southern Outskirts",CanJumpOneTile() & CanBounce() & CanBurrow() ),
    "Fish_Crumble" : LocationData(274, "Southern Outskirts"),
}

connections: dict[str, RegionConnectionData] = {

    "Southern Outskirts_LL Boardwalk" : RegionConnectionData("Southern Outskirts", "LL Boardwalk", CanJumpTiles(distance=2)),
    "Southern Outskirts_Ossex" : RegionConnectionData("Southern Outskirts", "Ossex"),
    "Southern Outskirts_Western Wilds Occupied Bridge" : RegionConnectionData("Southern Outskirts", "Western Wilds Occupied Bridge", CanJumpOneTile() & CanBurrow()),
    "Southern Outskirts_Eastern Heath Grassland" : RegionConnectionData("Southern Outskirts", "Eastern Heath Grassland", CanJumpOneTile()),
}