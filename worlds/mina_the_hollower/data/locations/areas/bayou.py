from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from .. import LocationData
from ... import RegionConnectionData
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanJumpTiles, CanBounce, CanSwim, CanCarry, CanClimb

collectable_locations: dict[str, LocationData] = {
    # "Lock" : LocationData(33, ""),
    "Health_Upgrade" : LocationData(34, ""),
    "Bonestone_03" : LocationData(35, ""),
    "Bonestone_02" : LocationData(36, ""),
    "NB Moonlit Hideaway Iron Lung" : LocationData(37, "Nox's Bayou Moonlit Hideaway"),
    "Bonestone_02" : LocationData(38, ""),
    "Bonestone_03" : LocationData(39, ""),
    "Trinket_VSyrup" : LocationData(40, ""),
    "Bonestone_03" : LocationData(41, ""),
    "Key" : LocationData(42, ""),
    "Bonestone_02" : LocationData(43, ""),
    "Key" : LocationData(44, ""),
    "Hammer_Level_2" : LocationData(45, ""),
    "Bonestone_02" : LocationData(46, ""),
    "Trinket_TwilWeave" : LocationData(47, ""),
    "Trinket_CrashPad" : LocationData(48, ""),
    "Key" : LocationData(49, ""),
    "Fish_Shrimpster" : LocationData(50, ""),
}

connections: dict[str, RegionConnectionData] = {
    "Bayou_Lower Backwaters" : RegionConnectionData("Waterfall Backwaters", "Western Wilds Occupied Bridge", (CanSwim() | CanJumpTiles(distance=4)) & CanBurrow()),

    "Upper Backwaters_Waterfall Backwaters" : RegionConnectionData("Upper Backwaters","Waterfall Backwaters", (CanSwim() | CanJumpTiles(distance=4))),
    "Waterfall Backwaters_Upper Backwaters" : RegionConnectionData("Waterfall Backwaters","Upper Backwaters", (CanSwim() | CanJumpTiles(distance=4))),
}