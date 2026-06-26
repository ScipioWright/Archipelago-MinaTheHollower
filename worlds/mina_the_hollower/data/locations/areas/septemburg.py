from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from ... import RegionConnection, Transition, LocationData
from ...items import SingleKears
from ...rules.ability_rules import CanBurrow, CanBounce, CanJumpTiles, CanClimb, CanCarry, HasFishingRod, CanSpring
from ...rules.state_rules import HasKear, HasRepairedWindyGenerator

collectable_locations: dict[str, LocationData] = {
    "SB Launch Pad Secret Room #1 Chest": LocationData(91, "Septemburg Withered Farms Hills Maze", CanSpring()),
    "SB Launch Pad Secret Room #2 Kear": LocationData(89, "Septemburg Withered Farms Secret Springs", CanSpring()),
    "SB Kid Room Chest": LocationData(92, "Septemburg Withered Farms Kid Room 1", CanBurrow()),
    "SB Hidden Mandrake Room Chest": LocationData(93, "Septemburg Hidden Mandrake Room", CanJumpTiles(distance=2)),
    "SB Hidden Crop Thresher Room Chest": LocationData(90, "Septemburg Tractor Chase", CanSpring() & CanBurrow()),
    "SB Rotten Barn Chest": LocationData(94, "Septemburg Rotten Barn Kid Room", CanBurrow()),
    "SB Below Crow Town Bridge Chest": LocationData(98, "Septemburg Crow Town Tunnel Top", HasKear(kear=SingleKears.SEPTEMBURG_CROW_TOWN_TUNNEL_KEAR.value)),
    "SB Below Crow Town Gazeworm Eye": LocationData(104, "Septemburg Crow Town Tunnel Top", HasFishingRod()),
    "SB Crow Town Shop Repulsing Root": LocationData(102, "Septemburg Crow Town"),
    "SB Crow Town Shop Kear": LocationData(103, "Septemburg Crow Town"),
    "SB Crow Town Farmhouse Roof Chest": LocationData(99, "Septemburg Farm House Roof", CanBurrow() & CanCarry()),
    "SB Tangled Woods Hidden Grove Chest": LocationData(97, "Septemburg Tangled Woods Hidden Grove", CanBurrow()),
    "SB Galloway Room Chest": LocationData(100, "Septemburg Tangled Woods Kid Room", CanBurrow() & CanSpring()),
    "SB Stormwatch Way Chest": LocationData(101, "Septemburg Stormwatch Wind", CanBurrow()),
    "SB Carving Shack Health Rose": LocationData(95, "Septemburg Carving Shack Arena"),
    "SB Dark Deluxy Spark Container": LocationData(353, "Septemburg Windy Generator", CanBurrow() & HasRepairedWindyGenerator()),
    "SB Wastewater Canal Spincer": LocationData(108, "Septemburg Wastewater Canal Well Entrance", HasFishingRod()),
    "SB Wastewater Canal Slime Room Chest": LocationData(106, "Septemburg Wastewater Canal Slime Room", CanBurrow()),
    "SB Wastewater Canal Box Room Chest": LocationData(105, "Septemburg Wastewater Canal Boxes", CanBurrow()),
    "SB Wastewater Canal Well Entrance Chest": LocationData(107, "Septemburg Wastewater Canal Well Entrance"),
}


boss_locations: dict[str, LocationData] = {
    "SB The Carving Man": LocationData(None, "Septemburg Carving Shack Arena"),
    "SB Windy Generator Activated": LocationData(None, "Septemburg Windy Generator"),  # needs float, burrow,
    "SB Dark Deluxy": LocationData(None, "Septemburg Windy Generator"),  # needs burrow, pipes,
}