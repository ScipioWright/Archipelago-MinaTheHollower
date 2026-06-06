from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from worlds.stardew_valley.strings.craftable_names import Fishing
from .. import LocationData
from ... import RegionConnectionData
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanJumpTiles, CanBlossomBounce

collectable_locations: dict[str, LocationData] = {
    "WW Balcony Dummy Cache" : LocationData(242, "Western Wilds Balcony", ),
    "WW Secret Passage Chest" : LocationData(243, "Western Wilds Secret Passageway"),
    # "Lock" : LocationData(244, "Western Wilds", ),
    "WW Occupied Bridge Dead Leaf" : LocationData(245, "Western Wilds Occupied Bridge"),
    # "Lock" : LocationData(246, "Western Wilds", ),
    # "Lock" : LocationData(247, "Western Wilds", ),
    "WW Secret Passage Joule Box" : LocationData(248, "Western Wilds Secret Passageway"),
    "WW Molten Foundry Flame Guard" : LocationData(249, "Western Wilds Molten Foundry"),
    "WW Occupied Bridge Across Chest" : LocationData(250, "Western Wilds Occupied Bridge"),
    "WW Molten Foundry Poppit Kear" : LocationData(251, "Western Wilds Molten Foundry"),
    "WW Occupied Bridge Underneath Chest" : LocationData(252, "Western Wilds Occupied Bridge"),
    "WW Occupied Bridge Far Chest" : LocationData(253, "Western Wilds Occupied Bridge"),
    "WW Molten Foundry Dark Chest" : LocationData(254, "Western Wilds Molten Foundry"),
    "WW Balcony Chest" : LocationData(255, "Western Wilds Balcony" ),
    "WW Molten Foundry Poppit Helio" : LocationData(256, "Western Wilds Molten Foundry" ),
    "WW unknown kear" : LocationData(257, "Western Wilds Molten Foundry"),
    "WW Western Pond Glomper Stalk" : LocationData(258, "Western Wilds Western Pond", Has("Fishing Rod")),
    "WW Occupied Bridge Cuddlepus Shell" : LocationData(259, "Western Wilds Occupied Bridge", Has("Fishing Rod")),
}

connections: dict[str, RegionConnectionData] = {

    "Western Wilds Occupied Bridge_Southern Outskirts" : RegionConnectionData("Western Wilds Occupied Bridge","Southern Outskirts", CanJumpOneTile() & CanBurrow()),
    "Western Wilds Occupied Bridge_Ossex" : RegionConnectionData("Western Wilds Occupied Bridge", "Ossex", CanJumpOneTile() & CanBurrow()),
    "Western Wilds Occupied Bridge_Waterfall Shanty Swamp" : RegionConnectionData("Western Wilds Occupied Bridge","Waterfall Shanty Swamp", CanJumpOneTile() & CanBurrow()),

    "Western Wilds Occupied Bridge_Western Wilds Secret Passageway" : RegionConnectionData("Western Wilds Occupied Bridge", "Western Wilds Secret Passageway"),
    "Western Wilds Secret Passageway_Western Wilds Occupied Bridge" : RegionConnectionData("Western Wilds Secret Passageway", "Western Wilds Occupied Bridge"),
    "Western Wilds Occupied Bridge_Western Wilds Molten Foundry" : RegionConnectionData("Western Wilds Occupied Bridge", "Western Wilds Molten Foundry"),
    "Western Wilds Molten Foundry_Western Wilds Occupied Bridge" : RegionConnectionData("Western Wilds Molten Foundry","Western Wilds Occupied Bridge"),
    "Western Wilds Occupied Bridge_Western Wilds Western Pond" : RegionConnectionData("Western Wilds Occupied Bridge", "Western Wilds Western Pond"),
    "Western Wilds Western Pond_Western Wilds Occupied Bridge" : RegionConnectionData("Western Wilds Western Pond","Western Wilds Occupied Bridge"),
    "Western Wilds Occupied Bridge_Western Wilds Balcony" : RegionConnectionData("Western Wilds Occupied Bridge", "Western Wilds Balcony"),
    "Western Wilds Balcony_Western Wilds Occupied Bridge" : RegionConnectionData("Western Wilds Balcony","Western Wilds Occupied Bridge"),


}