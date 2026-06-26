from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from ... import RegionConnection, Transition, LocationData
from ...items import SingleKears
from ...rules.ability_rules import CanBurrow, CanBounce, CanJumpTiles, CanClimb, CanCarry, CanSwim
from ...rules.state_rules import HasKear

collectable_locations: dict[str, LocationData] = {
    "RM Foyer Library Chest" : LocationData(275, "Radiant Manor Foyer Library", CanJumpTiles(distance=2) & CanClimb()),
    "RM Mimic Chamber Dodging Pendulum" : LocationData(140, "Radiant Manor Mimic Chamber", CanBurrow()),
    "RM Rafters Chest" : LocationData(143, "Radiant Manor Rafters", CanBurrow()),
    "RM Servant's Quarters Spring Heels" : LocationData(145, "Radiant Manor Servant's Quarters", CanBurrow()),
    "RM Ballroom Chest" : LocationData(144, "Radiant Manor Ballroom Balcony East"),
    "RM Tile Chamber Chest" : LocationData(142, "Radiant Manor Balcony East Chamber", CanJumpTiles(distance=2)),
    "RM Meowstro's Chamber Bonestone" : LocationData(139, "Radiant Manor Meowstro's Chamber", CanBurrow() & CanSwim() & CanCarry() & CanBounce() & CanClimb() & HasKear(kear=SingleKears.RADIANT_MANOR_MEOWSTRO_ROOM_KEAR.value)), #needs burrow, swim, carry, float, climb, kear,

}


boss_locations: dict[str, LocationData] = {
    "RM Furgus' Chamber" : LocationData(None, "Radiant Manor Servant's Arena"),
    "RM Study Lionel" : LocationData(None, "Radiant Manor Study"),
}