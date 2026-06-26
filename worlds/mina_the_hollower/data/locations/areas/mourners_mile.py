from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from ... import RegionConnection, Transition, LocationData
from ...rules.ability_rules import CanBurrow, CanBounce, CanJumpTiles, CanClimb, CanCarry


boss_locations: dict[str, LocationData] = {
}

collectable_locations: dict[str, LocationData] = {
    "MM Knight's Rest Chest": LocationData(311, "Mourner's Mile Knight's Rest Chest"),
    "MM Statue Room Bonestone": LocationData(315, "Mourner's Mile Statue Room Rope"),
    "MM Shallow Tomb Kear": LocationData(305, "Mourner's Mile Dark Shallow Tomb Dark"),
    "MM Ring Tomb Spike Spurs": LocationData(316, "Mourner's Mile Shallow Tomb"),
    "MM Spike Vault Vial Pouch": LocationData(312, "Mourner's Mile Spike Vault Upper"),
    "MM Spike Vault Hidden Room Kear": LocationData(310, "Mourner's Mile Spike Vault Hidden Room"),
    "MM Tower Tunnel Chest #1": LocationData(313, "Mourner's Mile Tower Tunnel Dark", CanBurrow()),
    "MM Tower Tunnel Chest #2": LocationData(314, "Mourner's Mile Tower Tunnel Dark", CanBurrow()),
    "MM Knight's Stand Bonestone": LocationData(303, "Mourner's Mile Knight's Guard Hill"),
    "MM Mina's Grave Chest": LocationData(309, "Mourner's Mile Mina's Grave"),
    "MM Mina's Grave Starving Beastium": LocationData(308, "Mourner's Mile Mina's Grave"),
    "MM Spike Hell Chest": LocationData(355, "Mourner's Mile Spike Hell Sandfall"),
}


