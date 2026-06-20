from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from ... import RegionConnection, Transition, LocationData
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanBounce, CanJumpTiles, CanClimb, CanCarry

collectable_locations: dict[str, LocationData] = {
    "AO Mirror's End Beach Room Chest": LocationData(281, "Astral Orrery Mirror's End"),
    # needs red tile switch, burrow,
    "AO Mirror's End Reckless Beastium": LocationData(276, "Astral Orrery Mirror's End"),
    # needs 3 tiles of air movement, carry,
    "AO Mirror's End West Ledge Trinket Bag": LocationData(279, "Astral Orrery Mirror's End"),
    # needs has("astral orrey mirror room left side kear") & ((yellow & burrow) | (red, green, yellow)),
    "AO Mirror's End Trunkstar Core": LocationData(282, "Astral Orrery Mirror's End"),  # needs fishing rod,
    "AO Mirror's End Moving Platform Room Chest": LocationData(280, "Astral Orrery Mirror's End Blue Chest"),
    "AO Stellarium East Chest": LocationData(129, "Astral Orrery Stellarium"),
    # needs has("astral orrery stellarium kear"),
    "AO Tubert Vial Salvo": LocationData(137, "Astral Orrery Stellarium"),
    "AO Tubert Vial Kear": LocationData(138, "Astral Orrery Stellarium"),  # needs mirror,
    "AO Gravity Zone Long Hallway Chest": LocationData(133, "Astral Orrery Gravity Zone"),
    # needs 2 tiles of air movement,
    "AO Gravity Zone Secret Room #1 Kear": LocationData(134, "Astral Orrery Gravity Zone"),
    "AO Gravity Zone Secret Room #2 Chest": LocationData(126, "Astral Orrery Gravity Zone"),  # needs burrow,
    "AO Cog Chamber Secret Room #1 Chest": LocationData(130, "Astral Orrery Cog Chamber"),  # needs burrow, carry,
    "AO Cog Chamber Secret Room #1 Kear": LocationData(135, "Astral Orrery Cog Chamber"),  # needs burrow, carry,
    "AO Mutant Lab Secret Room #1 Chest": LocationData(131, "Astral Orrery Mutant Lab"),  # needs burrow,
    "AO Mutant Lab Secret Room #2 Bridge Weaver": LocationData(132, "Astral Orrery Mutant Lab"),  # needs burrow,
    "AO Hall of Scholars Below Boss Chamber Bonestone": LocationData(126, "Astral Orrery Hall of Scholars"),
    "AO Hall of Scholars Exit Chest": LocationData(136, "Astral Orrery Hall of Scholars End"),  # needs burrow,
    "AO Sealed Archive Health Rose": LocationData(125, "Astral Orrery Sealed Archive Congealed Chamber"),


}
boss_locations: dict[str, LocationData] = {
    "AO Defeat Lumenarks": LocationData(None, "Astral Orrery Hall Of Scholars"),  # needs burrow,
    "AO Sealed Archive The Congealed": LocationData(None, "Astral Orrery Sealed Archive Congealed Chamber"),
    "AO Starry Generator Activated": LocationData(None, "Astral Orrery Starry Generator"),
}

