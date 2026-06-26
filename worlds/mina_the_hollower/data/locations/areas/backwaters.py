from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from ... import RegionConnection, Transition, LocationData
from ...items import Trinkets, SingleKears, Sidearms, FishingUpgrades
from ...rules.ability_rules import CanBurrow, CanJumpTiles, CanBounce, CanSwim, CanCarry, CanClimb, \
    HasFishingRod
from ...rules.state_rules import HasLadder, HasKear

collectable_locations: dict[str, LocationData] = {
    "BW Upper Shanty Swamp Plasma Jug": LocationData(290, "Backwaters Upper Swamp Waterfall"),
    "BW Upper Shanty Swamp Glutton's Jug": LocationData(289, "Backwaters Upper Swamp Waterfall", Has(Trinkets.EMPTY_JUG.value)),
    "BW Upper Swamp Side Room Chest": LocationData(296, "Backwaters Upper Swamp Secret Room", CanSwim()),
    "BW Lantern Cave Bonestone": LocationData(287, "Backwaters Upper Lantern Cave"),
    "BW Lantern Cave Vial Pouch": LocationData(295, "Backwaters Upper Lantern Cave"),
    "BW Pinky's Parlor Spark Catcher": LocationData(297, "Backwaters Pinky Shop"),
    "BW Pinky's Parlor Kear": LocationData(298, "Backwaters Pinky Shop"),
    "BW Pinky's Parlor Joule Box": LocationData(286, "Backwaters Pinky Shop Back", HasLadder()),
    "BW Lower Shanty Swamp Bonestone Block": LocationData(293, "Backwaters Lower Swamp Fishing", HasKear(kear=SingleKears.BACKWATERS_FISHING_KEAR.value) & (CanSwim() | CanJumpTiles(distance=4))),
    "BW Lower Shanty Swamp Evasion Powder": LocationData(294, "Backwaters Lower Swamp Station Entrance", HasLadder()),
    "BW Lower Shanty Swamp Bonestone": LocationData(288, "Backwaters Lower Swamp Station Entrance", HasLadder()),
    "BW Lower Shanty Swamp Tumbling Tutu": LocationData(291, "Backwaters Lower Swamp Shanty Band", CanCarry() & CanBurrow() & CanSwim() & CanClimb()),
    "BW Lucky's Lair Kear": LocationData(292, "Backwaters Lucky's Lair", CanBurrow() & CanCarry()),
    "BW Fishing Hole Fishing Rod": LocationData(300, "Backwaters Fishing Hole"),
    "BW Fishing Hole Fleeper Head": LocationData(299, "Backwaters Fishing Hole", HasFishingRod()),
    "BW Fishing Hole Thalessian Pearl": LocationData(302, "Backwaters Fishing Hole", HasFishingRod() & CanSwim() & (Has(Trinkets.TUNNELING_CODEX.value) | Has(FishingUpgrades.FISHING_ROD.value, count=2))),
    "BW Fishing Hole Gilded Rod": LocationData(301, "Backwaters Fishing Hole", HasFishingRod() & CanSwim() & (Has(Trinkets.TUNNELING_CODEX.value) | Has(FishingUpgrades.FISHING_ROD.value, count=2))),
}

boss_locations: dict[str, LocationData] = {
    "Defeat Fish Boss": LocationData(0, "Waterfall Backwaters"),
}

