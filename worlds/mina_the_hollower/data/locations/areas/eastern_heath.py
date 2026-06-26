from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_, CanReachLocation
from ... import RegionConnection, Transition, LocationData, TransitionType, DirectionType
from ...items import Trinkets, SingleKears
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanJumpTiles, CanBounce, HasReachingSideArm, CanClimb, \
    CanSwim, HasFishingRod
from ...rules.state_rules import HasRepairedSolemnGenerator, HasKear, HasRepairedOneGenerator

collectable_locations: dict[str, LocationData] = {
    "EH Grassland Trinket Bag" : LocationData(221, "Eastern Heath Grassland", HasRepairedOneGenerator()),
    "EH Grassland Dork Eyes" : LocationData(241, "Eastern Heath Grassland Bridge Right", HasFishingRod()), #needs fishing rod,
    "EH Grassland Ossex Patio Chest" : LocationData(231, "Eastern Heath I Screen", CanBurrow()),
    "EH Grassland Bush Room Bonestone" : LocationData(236, "Eastern Heath Bush Room", HasKear(kear=SingleKears.EASTERN_HEATH_GRASSLAND_BUSHROOM_KEAR.value)), #needs kear,
    "EH Grassland Riverbed Chest" : LocationData(233, "Eastern Heath Grassland Riverbed Bottom"),
    "EH Choppe Shoppe Chain Capacitor" : LocationData(226, "Eastern Heath Choppe Shoppe"),
    "EH Hidden Grotto Chest" : LocationData(228, "Eastern Heath Hidden Grotto"),
    "EH Grassland Waterfall Chest" : LocationData(234, "Eastern Heath Grassland Waterfall Second Level"),
    "EH Grassland Waterfall Windfall Charm" : LocationData(223, "Eastern Heath Grassland Waterfall Second Level", HasReachingSideArm() | Has(Trinkets.SPRING_HEELS.value)),
    "EH Grassland Vertical Spinner Room Chest" : LocationData(238, "Eastern Heath East Corner", HasRepairedSolemnGenerator()),
    "EH Under the Bridge Chest" : LocationData(230, "Eastern Heath Under Bridge West"),
    "EH Buckler's Bluff Joule Box" : LocationData(229, "Eastern Heath Buckler's Bluff Cliff"),
    "EH Grassland Poppit Cave Chest" : LocationData(235, "Eastern Heath Grassland Poppit Cave"),
    "EH Grassland Poppit Cave Willow" : LocationData(239, "Eastern Heath Poppit"),
    "EH Grassland Poppit Cave Kear" : LocationData(240, "Eastern Heath Poppit"),
    "EH Frozen Pass Chest" : LocationData(232, "Eastern Heath Frozen Pass Top"),
    "EH Frozen Pass IceBlock" : LocationData(237, "Eastern Heath Frozen Pass Top"),
}

boss_locations: dict[str, LocationData] = {
    "EH Grassland Maxi": LocationData(1018, "Eastern Heath Grassland", HasRepairedOneGenerator()),
}
