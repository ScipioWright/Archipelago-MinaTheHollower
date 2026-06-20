from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from ... import RegionConnection, Transition, LocationData
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanBounce, CanJumpTiles, CanClimb, CanCarry


collectable_locations: dict[str, LocationData] = {
    "RM Foyer Library Chest" : LocationData(275, "Radiant Manor Foyer Library"), #needs 2 tiles of air movement,
    "RM Mimic Chamber Dodging Pendulum" : LocationData(140, "Radiant Manor Mimic Chamber"), #needs burrow,
    "RM Rafters Chest" : LocationData(143, "Radiant Manor Rafters"), #needs burrow,
    "RM Servant's Quarters Spring Heels" : LocationData(145, "Radiant Manor Servant's Quarters"), #needs burrow,
    "RM Ballroom Chest" : LocationData(144, "Radiant Manor Ballroom Balcony East"),
    "RM Tile Chamber Chest" : LocationData(142, "Radiant Manor Balcony East Chamber"), #needs 2 tiles of air movement,
    "RM Meowstro's Chamber Bonestone" : LocationData(139, "Radiant Manor Meowstro's Chamber"), #needs burrow, swim, carry, float, climb, kear,

}


boss_locations: dict[str, LocationData] = {
    "RM Furgus' Chamber" : LocationData(None, "Radiant Manor Servant's Arena"),
    "RM Study Lionel" : LocationData(None, "Radiant Manor Study"),
}