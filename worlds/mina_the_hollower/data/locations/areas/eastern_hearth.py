from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_, CanReachLocation
from ... import RegionConnection, Transition, LocationData, TransitionType, DirectionType
from ...items import Trinkets, SingleKears
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanJumpTiles, CanBounce, HasReachingSideArm, CanClimb, \
    CanSwim, HasFishingRod
from ...rules.state_rules import HasCompletedOneSparkGenerator, HasRepairedSolemnGenerator, HasKear

collectable_locations: dict[str, LocationData] = {
    "EH Grassland Trinket Bag" : LocationData(221, "Eastern Hearth Grassland", HasCompletedOneSparkGenerator()),
    "EH Grassland Dork Eyes" : LocationData(241, "Eastern Hearth Grassland Bridge Right", HasFishingRod()), #needs fishing rod,
    "EH Grassland Ossex Patio Chest" : LocationData(231, "Eastern Hearth I Screen", CanBurrow()),
    "EH Grassland Bush Room Bonestone" : LocationData(236, "Eastern Hearth Bush Room", HasKear(kear=SingleKears.EASTERN_HEARTH_GRASSLAND_BUSHROOM_KEAR.value)), #needs kear,
    "EH Grassland Riverbed Chest" : LocationData(233, "Eastern Hearth Grassland Riverbed Bottom"),
    "EH Choppe Shoppe Chain Capacitor" : LocationData(226, "Eastern Hearth Choppe Shoppe"),
    "EH Hidden Grotto Chest" : LocationData(228, "Eastern Hearth Hidden Grotto"),
    "EH Grassland Waterfall Chest" : LocationData(234, "Eastern Hearth Grassland Waterfall Second Level"),
    "EH Grassland Waterfall Windfall Charm" : LocationData(223, "Eastern Hearth Grassland Waterfall Second Level", HasReachingSideArm() | Has(Trinkets.SPRING_HEELS.value)),
    "EH Grassland Vertical Spinner Room Chest" : LocationData(238, "Eastern Hearth East Corner", HasRepairedSolemnGenerator()),
    "EH Under the Bridge Chest" : LocationData(230, "Eastern Hearth Under Bridge West"),
    "EH Buckler's Bluff Joule Box" : LocationData(229, "Eastern Hearth Buckler's Bluff Cliff"),
    "EH Grassland Poppit Cave Chest" : LocationData(235, "Eastern Hearth Grassland Poppit Cave"),
    "EH Grassland Poppit Cave Willow" : LocationData(239, "Eastern Hearth Poppit"),
    "EH Grassland Poppit Cave Kear" : LocationData(240, "Eastern Hearth Poppit"),
    "EH Frozen Pass Chest" : LocationData(232, "Eastern Hearth Frozen Pass Top"),
    "EH Frozen Pass IceBlock" : LocationData(237, "Eastern Hearth Frozen Pass Top"),
}

boss_locations: dict[str, LocationData] = {
    "EH Grassland Maxi": LocationData(1018, "Eastern Heath Grassland", HasCompletedOneSparkGenerator()),
}
