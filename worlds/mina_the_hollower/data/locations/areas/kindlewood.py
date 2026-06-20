from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from ... import RegionConnection, Transition, LocationData
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanBounce, CanJumpTiles, CanClimb, CanCarry


collectable_locations: dict[str, LocationData] = {
    "KW Overgrowth Bonfire Chest": LocationData(340, "Kindlewood Overgrowth Bonfire Main"),
    "KW Residence Basement Chest": LocationData(441, "Kindlewood Overgrowth Residence Basement"),

    "KW Madd House Draining Beastium": LocationData(348, "Kindlewood Overgrowth Madd House"),
    "KW Madd House Oozing Organ": LocationData(347, "Kindlewood Overgrowth Madd House"),
    "KW Madd House Voltaic Guard": LocationData(349, "Kindlewood Overgrowth Madd House"),
    "KW Madd House Kear": LocationData(350, "Kindlewood Overgrowth Madd House"),
    "KW Behind Madd House Chest": LocationData(339, "Kindlewood Behind Madd House"),
    "KW Train Station Gourdan": LocationData(335, "Kindlewood Farm Crossing Pumpkin Patch"),  # needs oozing organ,
    "KW Train Station Ledge Chest": LocationData(346, "Kindlewood Farm Crossing Pumpkin Patch"),  # needs burrow,
    "KW Farm Crossing Shack Chest": LocationData(342, "Kindlewood Farm Crossing Shack"),# needs burrow, reaching sidearm,
    "KW Wallower's Room Wallower's Gauntlets": LocationData(344, "Kindlewood Wallowers Path"),  # needs kear, burrow,
    "KW Wallower's Room Chest": LocationData(345, "Kindlewood Wallowers Path"), # needs (wallower's gloves, burrow) or 5+ tiles of air movement,
    "KW Rail Tunnel Vial Pouch": LocationData(343, "Kindlewood Rail Tunnel"),  # needs burrow, carry,
}

boss_locations: dict[str, LocationData] = {
    "KW Madd House": LocationData(None, "Kindlewood Overgrowth Madd House"),
}

