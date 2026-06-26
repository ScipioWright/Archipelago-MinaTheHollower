from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from ... import RegionConnection, Transition, LocationData
from ...rules.ability_rules import CanBurrow, CanBounce, CanJumpTiles, CanClimb, CanCarry, HasFishingRod

collectable_locations: dict[str, LocationData] = {
    "CTP Frigid Station Missed Train Chest": LocationData(113, "Coltrane Peak Station Tracks"),
    "CTP Frozen Pass Rope Chest": LocationData(112, "Coltrane Peak Frozen Pass", CanClimb()),
    "CTP Dead Man's Gorge Passage Trinket": LocationData(110, "Coltrane Peak Gorge Ice Gauntlet"),
    "CTP Dead Man's Gorge Rail Kear": LocationData(111, "Coltrane Peak Train Tracks Secret", CanBurrow()),
    "CTP Frostbite Woods Blinking Glass": LocationData(114, "Coltrane Peak Frostbite Woods"),
    "CTP Rail Yard Purple Structure Chest": LocationData(118, "Coltrane Peak Rail Yard"),
    "CTP Rail Yard Cliff Chest": LocationData(117, "Coltrane Peak Rail Yard"),
    "CTP Rail Yard Casket Chest": LocationData(119, "Coltrane Peak Rail Yard Chest"),
    "CTP Rail Yard Kear Room Fish": LocationData(122, "Coltrane Peak Frozen River", CanBurrow() & HasFishingRod()),
    "CTP Rail Yard Kear Room Rupert Shop Trinket": LocationData(120, "Coltrane Peak Frozen River", CanBurrow()),
    "CTP Rail Yard Kear Room Rupert Shop Kear": LocationData(121, "Coltrane Peak Frozen River", CanBurrow()),
    "CTP Spiral Summit Kear": LocationData(116, "Coltrane Peak Spiral Summit Secret", CanBurrow() & CanClimb()),
    "CTP Agnes Express Bone Mimic": LocationData(123, "Coltrane Peak Agnes Express Rear"),
    "CTP Maelstrom Locomotress Health Rose": LocationData(124, "Coltrane Peak Agnes Express Arena"),
}


boss_locations: dict[str, LocationData] = {
    "CTP Frozen Generator Activated": LocationData(None, "Coltrane Peak Frozen Generator"),
    "CTP Maelstrom Locomotress Agnes Boss": LocationData(None, "Coltrane Peak Agnes Express Arena"),
    "CTP Icebound Cavern Frozen Horror Boss": LocationData(None, "Coltrane Peak Frozen Horror Arena"),
    "CTP Frostbite Woods Mirren": LocationData(None, "Coltrane Peak Mirren Room"),
    "CTP Fateful Cliff Thorne CTP Boss": LocationData(None, "Coltrane Peak Thorne Arena"),  # needs climb,
}