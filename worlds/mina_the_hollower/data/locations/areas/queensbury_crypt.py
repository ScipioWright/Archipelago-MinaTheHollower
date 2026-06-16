from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from ... import RegionConnection, Transition, LocationData
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanBounce, CanJumpTiles, CanClimb, CanCarry


collectable_locations: dict[str, LocationData] = {
    "QC Old Graveyard Bonestone": LocationData(51, "Queensbury Crypt Old Graveyard Main"),
    "QC Old Graveyard Kear": LocationData(52, "Queensbury Crypt Old Graveyard Sodsby"),  # needs burrow,
    "QC Bonnet Tomb Desperation Bonnet": LocationData(57, "Queensbury Crypt Bonnet Tomb Inner"),  # needs burrow, kear,
    "QC Broken Bridge Bonestone": LocationData(54, "Queensbury Crypt Broken Bridge"),
    "QC Pipe Room Bonestone": LocationData(53, "Queensbury Crypt Pipe Room"),
    "QC Castle Entry Weapon Chest": LocationData(56, "Queensbury Crypt Castle Entry"),
    "QC Smelly Secret Kear": LocationData(64, "Queensbury Crypt Smelly Secret"),
    "QC Hidden Tunnel Bonestone": LocationData(61, "Queensbury Crypt Hidden Tunnel"),  # needs burrow,
    "QC Statue Head Hall Chest": LocationData(63, "Queensbury Crypt Statue Head Hall Entrance"),  # needs burrow, carry,
    "QC Mirror Room Chest": LocationData(65, "Queensbury Crypt Mirror Room West"),  # needs burrow, carry,
    "QC Mirror Room Stolenoid": LocationData(66, "Queensbury Crypt Mirror Room West"),  # needs burrow, carry,
    "QC Mirror Room Kear": LocationData(67, "Queensbury Crypt Mirror Room West"),  # needs burrow, carry,
    "QC Putrid Place Bonestone": LocationData(62, "Queensbury Crypt Putrid Place"),  # needs burrow, carry,
    "QC Putrid Place Tombstone": LocationData(68, "Queensbury Crypt Putrid Place"),  # needs burrow, carry, fishing rod,
    "QC Rancid Room Fly Bait": LocationData(59, "Queensbury Crypt Rancid Room"),  # needs burrow, carry, 2 vials,
    "QC Ancestral Chamber Health Rose": LocationData(58, "Queensbury Crypt Ancestral Chamber"),  # needs burrow, carry,
    "QC Royal Tomb Proto Spark": LocationData(60, "Queensbury Crypt Royal Tomb"),# needs burrow, carry, climb, 2 vials,


}
boss_locations: dict[str, LocationData] = {
    "QC Rancid Room Midden": LocationData(0, "Queensbury Crypt Rancid Room"),
    "QC Ancestral Chamber The Duchess": LocationData(1018, "Queensbury Crypt Ancestral Chamber"),
    "QC Solemn Generator Activated": LocationData(0, "Queensbury Crypt Solemn Generator"),
}