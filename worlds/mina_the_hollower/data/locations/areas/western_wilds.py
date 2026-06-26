from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from ... import RegionConnection, Transition, LocationData
from ...items import SingleKears, Trinkets
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanJumpTiles, CanBounce, CanCarry, HasFishingRod, CanClimb
from ...rules.state_rules import HasKear

collectable_locations: dict[str, LocationData] = {
    "WW Secret Passage Chest" : LocationData(251, "Western Wilds Secret Passageway East", CanJumpTiles(distance=3)),
    "WW Secret Passage Joule Box" : LocationData(248, "Western Wilds Secret Passageway East", CanJumpTiles(distance=5) & HasKear(kear=SingleKears.WESTERN_WILDS_SECRET_PASSAGE_KEAR.value)),
    "WW Occupied Bridge Brute Chest" : LocationData(253, "Western Wilds Brutes"),
    "WW Occupied Bridge Far Chest" : LocationData(250, "Western Wilds End", CanBurrow()),
    "WW Occupied Bridge Dead Leaf" : LocationData(245, "Western Wilds Brutes", CanBurrow() & CanCarry()), #needs kill the other leaf,
    "WW Occupied Bridge Cuddlepus Shell" : LocationData(259, "Western Wilds Western Pond", HasFishingRod()),
    "WW Occupied Bridge Underneath Chest" : LocationData(252, "Western Wilds Foundry Path", CanBurrow()),
    "WW Molten Foundry Poppit Helio" : LocationData(256, "Western Wilds Molten Foundry Dark Poppit"),
    "WW Molten Foundry Poppit Kear" : LocationData(257, "Western Wilds Molten Foundry Dark Poppit"),
    "WW Molten Foundry Dark Chest" : LocationData(255, "Western Wilds Molten Foundry Dark", CanBurrow() | Has(Trinkets.POLYP_LAMP.value)),
    "WW Molten Foundry Flame Guard" : LocationData(249, "Western Wilds Molten Dungeon End"),
    "WW Western Pond Glomper Stalk" : LocationData(258, "Western Wilds Western Pond", HasFishingRod()),
    "WW Balcony Chest" : LocationData(254, "Western Wilds Balcony", HasKear(kear=SingleKears.WESTERN_WILDS_BALCONY_KEAR.value)),
    "WW Balcony Dummy Cache" : LocationData(242, "Western Wilds Balcony", HasKear(kear=SingleKears.WESTERN_WILDS_BALCONY_KEAR.value) & CanBurrow() & CanCarry() & CanClimb()),
}

boss_locations: dict[str, LocationData] = {
}
