from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from .. import LocationData
from ... import RegionConnection
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanJumpTiles, CanBounce, ReachingSideArm, CanClimb

collectable_locations: dict[str, LocationData] = {
    "EH Grassland Trinket Bag" : LocationData(221, "Eastern Heath Grassland", CanJumpOneTile() & CanBurrow()),
    # "Lock" : LocationData(222, ""),
    "EH Grassland Waterfall Windfall Charm" : LocationData(223, "Eastern Heath Grassland Waterfall"),
    # "Lock" : LocationData(224, ""),
    # "Lock" : LocationData(225, ""),
    "EH Choppe Shoppe Chain Capacitor" : LocationData(226, "Eastern Heath Choppe Shoppe", Has("Choppe Shoppe Kear") & (ReachingSideArm() | CanJumpOneTile())),
    # "Lock" : LocationData(227, ""),
    "EH Grassland Waterfall Chest" : LocationData(228, "Eastern Heath Grassland Waterfall", CanJumpOneTile() & CanBurrow()),
    "EH Buckler's Bluff Joule Box": LocationData(229, "Eastern Heath Buckler's Bluff", Has("Eastern Heath Buckler's Bluff Kear") & CanJumpOneTile() & CanJumpTiles(distance=5)),
    "EH Under the Bridge Chest" : LocationData(230, "Eastern Heath Under the Bridge", CanJumpOneTile() & CanBurrow()),
    "EH Grassland Riverbed Chest" : LocationData(231, "Eastern Heath Grassland Waterfall", CanJumpTiles(distance=1)),
    "EH Grassland Bush Room Bonestone" : LocationData(232, "Eastern Heath Grassland Bush Room", CanJumpTiles(distance=1) & Has("Eastern Hearth Grassland Bushroom Kear")),
    "EH Grassland Horizontal Spinner Room Chest" : LocationData(233, "", CanJumpOneTile() & CanBurrow()),
    "EH Grotto Chest" : LocationData(234, "Eastern Heath Grotto", Has("Grassland Grotto Kear") & CanJumpOneTile() & CanBurrow()),
    "EH Grassland Poppit Cave Chest" : LocationData(235, "Eastern Heath Grassland Poppit Cave", CanJumpOneTile() & CanBurrow()),
    "EH Frozen Pass Chest" : LocationData(236, "Eastern Heath Frozen Pass", CanJumpOneTile() & CanBurrow() & CanClimb()),
    "EH Frozen Pass IceBlock" : LocationData(237, "Eastern Heath Frozen Pass", CanJumpOneTile() & CanBurrow()),
    "EH Grassland Vertical Spinner Room Chest" : LocationData(238, "Eastern Heath Grassland Vertical Spinner Room",Has("Grassland Vertical Spinner Kear") & CanJumpOneTile() & CanBurrow() & (Has("Volt Axe") | Has ("Spring Heeled Boots"))),
    "EH Grassland Poppit Cave Willow" : LocationData(239, "Eastern Heath Grassland Poppit Cave", CanJumpOneTile() & CanBurrow()),
    "EH Grassland Poppit Cave Kear" : LocationData(240, "Eastern Heath Grassland Poppit Cave", CanJumpOneTile() & CanBurrow()),
    "EH Grassland Dork Eyes" : LocationData(241, "Eastern Heath Grassland Bridge", Has("Fishing Rod")),
}

boss_locations: dict[str, LocationData] = {
    "EH Grassland Maxi": LocationData(0, "Eastern Heath Grassland", CanJumpOneTile() & CanBurrow()),
}

connections: dict[str, RegionConnection] = {
    "Eastern Hearth Grassland_Ossex" : RegionConnection("Eastern Hearth Grassland", "Ossex"),
    "Eastern Hearth Grassland_Southern Outskirts" : RegionConnection("Eastern Hearth Grassland", "Southern Outskirts"),

    "Eastern Hearth Grassland_Eastern Heath Grassland Bridge" : RegionConnection("Eastern Hearth Grassland", "Eastern Heath Grassland Bridge"),
    "Eastern Heath Grassland Bridge_Eastern Hearth Grassland" : RegionConnection("Eastern Heath Grassland Bridge", "Eastern Hearth Grassland"),

    "Eastern Hearth Grassland_Eastern Heath Grassland Bush Room" : RegionConnection("Eastern Hearth Grassland", "Eastern Heath Grassland Bush Room"),
    "Eastern Heath Grassland Bush Room_Eastern Hearth Grassland" : RegionConnection("Eastern Heath Grassland Bush Room", "Eastern Hearth Grassland"),

    "Eastern Hearth Grassland_Eastern Heath Grassland Riverbed" : RegionConnection("Eastern Hearth Grassland", "Eastern Heath Grassland Riverbed"),
    "Eastern Heath Grassland Riverbed_Eastern Hearth Grassland" : RegionConnection("Eastern Heath Grassland Riverbed", "Eastern Hearth Grassland"),

    "Eastern Hearth Grassland_Eastern Heath Choppe Shoppe" : RegionConnection("Eastern Hearth Grassland", "Eastern Heath Choppe Shoppe"),
    "Eastern Heath Choppe Shoppe_Eastern Hearth Grassland" : RegionConnection("Eastern Heath Choppe Shoppe", "Eastern Hearth Grassland"),

    "Eastern Hearth Grassland_Eastern Heath Grassland Waterfall" : RegionConnection("Eastern Hearth Grassland", "Eastern Heath Grassland Waterfall"),
    "Eastern Heath Grassland Waterfall_Eastern Hearth Grassland" : RegionConnection("Eastern Heath Grassland Waterfall", "Eastern Hearth Grassland"),

    "Eastern Hearth Grassland_Eastern Heath Grassland Vertical Spinner Room" : RegionConnection("Eastern Hearth Grassland", "Eastern Heath Grassland Vertical Spinner Room"),
    "Eastern Heath Grassland Vertical Spinner Room_Eastern Hearth Grassland" : RegionConnection("Eastern Heath Grassland Vertical Spinner Room", "Eastern Hearth Grassland"),

    "Eastern Hearth Grassland_Eastern Heath Under the Bridge" : RegionConnection("Eastern Hearth Grassland", "Eastern Heath Under the Bridge"),
    "Eastern Heath Under the Bridge_Eastern Hearth Grassland" : RegionConnection("Eastern Heath Under the Bridge", "Eastern Hearth Grassland"),

    "Eastern Hearth Grassland_Eastern Heath Grassland Poppit Cave" : RegionConnection("Eastern Hearth Grassland", "Eastern Heath Grassland Poppit Cave"),
    "Eastern Heath Grassland Poppit Cave_Eastern Hearth Grassland" : RegionConnection("Eastern Heath Grassland Poppit Cave", "Eastern Hearth Grassland"),

    "Eastern Hearth Grassland_Eastern Heath Frozen Pass" : RegionConnection("Eastern Hearth Grassland", "Eastern Heath Frozen Pass"),
    "Eastern Heath Frozen Pass_Eastern Hearth Grassland" : RegionConnection("Eastern Heath Frozen Pass", "Eastern Hearth Grassland"),

}