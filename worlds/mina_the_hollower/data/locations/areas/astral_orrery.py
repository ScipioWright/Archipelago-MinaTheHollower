from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from ... import RegionConnection, Transition, LocationData
from ...items import AstralPlatforms, SingleKears
from ...rules.ability_rules import CanBurrow, CanBounce, CanJumpTiles, CanClimb, CanCarry, HasFishingRod
from ...rules.state_rules import HasKear

collectable_locations: dict[str, LocationData] = {
    "AO Mirror's End Beach Room Chest": LocationData(281, "Astral Orrery Mirror's End", Has(AstralPlatforms.RED_ASTRAL_PLATFORMS.value) & CanBurrow()),
    "AO Mirror's End Reckless Beastium": LocationData(276, "Astral Orrery Mirror's End", CanJumpTiles(distance=3) & CanCarry()),
    "AO Mirror's End West Ledge Trinket Bag": LocationData(279, "Astral Orrery Mirror's End",  HasKear(kear=SingleKears.ASTRAL_ORREY_MIRROR_ROOM_LEFT_SIDE_KEAR.value)
           & Has(AstralPlatforms.YELLOW_ASTRAL_PLATFORMS.value) & ( CanJumpTiles(distance=7) | CanBurrow() |
                (Has(AstralPlatforms.RED_ASTRAL_PLATFORMS.value) & Has(AstralPlatforms.GREEN_ASTRAL_PLATFORMS.value)))),
    "AO Mirror's End Trunkstar Core": LocationData(282, "Astral Orrery Mirror's End", HasFishingRod()),
    "AO Mirror's End Moving Platform Room Chest": LocationData(280, "Astral Orrery Mirror's End Blue Chest"),
    "AO Stellarium East Chest": LocationData(129, "Astral Orrery Stellarium", HasKear(kear=SingleKears.ASTRAL_ORRERY_STELLARIUM_KEAR.value)),
    "AO Tubert Vial Salvo": LocationData(137, "Astral Orrery Stellarium Mutant Switch"),
    "AO Tubert Vial Kear": LocationData(138, "Astral Orrery Stellarium Mutant Switch"),
    "AO Gravity Zone Long Hallway Chest": LocationData(133, "Astral Orrery Gravity Zone", CanJumpTiles(distance=2)),
    "AO Gravity Zone Secret Room #1 Kear": LocationData(134, "Astral Orrery Gravity Zone"),
    "AO Gravity Zone Secret Room #2 Chest": LocationData(126, "Astral Orrery Gravity Zone", CanBurrow()),
    "AO Cog Chamber Secret Room #1 Chest": LocationData(130, "Astral Orrery Cog Chamber", CanBurrow() & CanCarry()),
    "AO Cog Chamber Secret Room #1 Kear": LocationData(135, "Astral Orrery Cog Chamber", CanBurrow() & CanCarry()),
    "AO Mutant Lab Secret Room #1 Chest": LocationData(131, "Astral Orrery Mutant Lab", CanBurrow()),
    "AO Mutant Lab Secret Room #2 Bridge Weaver": LocationData(132, "Astral Orrery Mutant Lab", CanBurrow()),
    "AO Hall of Scholars Below Boss Chamber Bonestone": LocationData(126, "Astral Orrery Hall of Scholars"),
    "AO Hall of Scholars Exit Chest": LocationData(136, "Astral Orrery Hall of Scholars End", CanBurrow()),
    "AO Sealed Archive Health Rose": LocationData(125, "Astral Orrery Sealed Archive Congealed Chamber"),


}
boss_locations: dict[str, LocationData] = {
    "AO Defeat Lumenarks": LocationData(None, "Astral Orrery Hall Of Scholars"),
    "AO Sealed Archive The Congealed": LocationData(None, "Astral Orrery Sealed Archive Congealed Chamber"),
    "AO Starry Generator Activated": LocationData(None, "Astral Orrery Starry Generator"),
}

