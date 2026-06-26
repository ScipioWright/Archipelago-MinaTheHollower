from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from ... import RegionConnection, Transition, LocationData
from ...rules.ability_rules import CanBurrow, CanBounce, CanJumpTiles, CanClimb, CanCarry, CanSwim, \
    HasFishingRod

collectable_locations: dict[str, LocationData] = {
    "BB Sandwater Junction Goremaw Fang": LocationData(88, "Bone Beach Aquatic", HasFishingRod() & CanSwim()),
    "BB Bone Rush Trail Furgus Tunnel Chest": LocationData(354, "Bone Beach Bone Rush Mine"),
    "BB Gold Grasp Bonestone": LocationData(71, "Bone Beach Bone Rush Drop"),
    "BB Large Conveyor Bonestone": LocationData(70, "Bone Beach Bone Rush Conveyor Top", CanBounce()),
    "BB Split Room Chest": LocationData(78, "Bone Beach Worms Back Split", CanJumpTiles(distance=2)),
    "BB Aquatic Conveyor Chest": LocationData(73, "Bone Beach Aquatic Conveyor", CanBurrow()),
    "BB Brac's Tent Polyp Lamp": LocationData(80, "Bone Beach Brac's Tent"),
    "BB Brac's Tent Kear": LocationData(81, "Bone Beach Brac's Tent"),
    "BB Secret Shoals Joule Syringe": LocationData(74, "Bone Beach Secret Shoals", CanSwim()),
    "BB Calcified Caverns Kear": LocationData(79, "Bone Beach Calcified Caves"),
    "BB Calcified Cage Bonestone": LocationData(76, "Bone Beach Calcified Cage"),
    "BB Submerged Handles Chest": LocationData(77, "Bone Beach Submerged Handles", CanSwim()),
    "BB Pulsing Tract Bonestone": LocationData(86, "Bone Beach Pulsing Tract Moving Top", CanJumpTiles(distance=2)),
    "BB Worm's Back Battery Buster": LocationData(75, "Bone Beach Worms Back Chest", CanBounce()),
    "BB Worm's Spine Bonestone": LocationData(72, "Bone Beach Worms Back Right", CanBurrow()),
    "BB Stomach Mine Kear": LocationData(84, "Bone Beach Stomach Mine Lower", CanBurrow() & CanBounce()),
    "BB Moving Stairs Bonestone": LocationData(85, "Bone Beach Gut Depths Hidden", CanBounce()),
    "BB Gut Passage Chest": LocationData(87, "Bone Beach Gut Depths Dark"),
    "BB Brain Alcove Health Rose": LocationData(83, "Bone Beach Brain Alcove"),

}


boss_locations: dict[str, LocationData] = {
    "BB Brain Alcove Mined Mind": LocationData(None, "Bone Beach Brain Alcove"),  # needs burrow,
}