from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from ... import RegionConnection, Transition, LocationData
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanJumpTiles, CanBounce, CanSwim, CanCarry, CanClimb


collectable_locations: dict[str, LocationData] = {
    "NB Boat Takeoff Shrimpter Tail" : LocationData(50, "Nox's Bayou Boat Station"), #needs fishing rod,
    "NB Guard Room Twill Weave" : LocationData(47, "Nox's Bayou Guard Room"),
    "NB First Flooder Chest" : LocationData(39, "Nox's Bayou Lily Full Pump Room"),
    "NB Shallow Pool Chest" : LocationData(38, "Nox's Bayou Shallow Pool"),
    "NB Lagoon Burrow Chest" : LocationData(42, "Nox's Bayou Big Lagoon Dark"),
    "NB Submerged Side Room Vascular Syrup" : LocationData(40, "Nox's Bayou Big Lagoon East Side Room"),
    "NB Swamp Shack Pit Preserver" : LocationData(48, "Nox's Bayou Swamp Shack"),
    "NB Swamp Shack Kear" : LocationData(49, "Nox's Bayou Swamp Shack"),
    "NB Swamp Shack Blastrike Maul" : LocationData(45, "Nox's Bayou Swamp Shack"), #needs has("nox's bayou swamp shack kear",
    "NB Moonlit Path Chest" : LocationData(43, "Nox's Bayou Moonlit Path"),
    "NB Moonlit Hideaway Iron Lung" : LocationData(37, "Nox's Bayou Moonlit Mirror"),
    "NB Plant Pond Chest" : LocationData(35, "Nox's Bayou Thick Plant Pond Cave"),
    "NB Twin Thicket Chest" : LocationData(36, "Nox's Bayou Twin Thicket"),
    "NB Hidden Cave Chest" : LocationData(44, "Nox's Bayou Canopy Bridge Cave"),
    "NB Grate Lake Chest" : LocationData(41, "Nox's Bayou Tainted Lair Grate Bridge"),
    "NB Tainted Depths Health Rose" : LocationData(34, "Nox's Bayou Tainted Lair Arena"), #needs swim,
    "NB Gutter Tunnel Chest" : LocationData(46, "Nox's Bayou Tainted Tunnel"), #needs burrow,
}


boss_locations: dict[str, LocationData] = {
    "NB Moonlit Mosh Mock Moon" : LocationData(1017, "Nox's Bayou Moonlit Arena"),
    "NB Tainted Depths Nox's Beast": LocationData(None, "Nox's Bayou Tainted Lair Arena"),  # needs swim,
    "NB Swampy Generator Activated": LocationData(None, "Nox's Bayou Swampy Generator"),
}