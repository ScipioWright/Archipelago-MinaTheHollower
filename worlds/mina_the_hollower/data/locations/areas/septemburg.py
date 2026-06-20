from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from ... import RegionConnection, Transition, LocationData
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanBounce, CanJumpTiles, CanClimb, CanCarry

collectable_locations: dict[str, LocationData] = {
    "SB Launch Pad Secret Room #1 Chest": LocationData(91, "Septemburg Withered Farms Hills Maze"),
    # needs canbounce(),
    "SB Launch Pad Secret Room #2 Kear": LocationData(89, "Septemburg Withered Farms Secret Springs"),
    # needs canbounce(),
    "SB Kid Room Chest": LocationData(92, "Septemburg Withered Farms Kid Room 1"),  # needs burrow,
    "SB Hidden Mandrake Room Chest": LocationData(93, "Septemburg Hidden Mandrake Room"),
    # needs canjumptiles(distance=2),
    "SB Hidden Crop Thresher Room Chest": LocationData(90, "Septemburg Tractor Chase"),
    # needs canburrow(), canbounce(),
    "SB Rotten Barn Chest": LocationData(94, "Septemburg Rotten Barn Kid Room"),  # needs burrow,
    "SB Below Crow Town Bridge Chest": LocationData(98, "Septemburg Crow Town Tunnel Top"),
    # needs has("septemburg crow town tunnel kear"),
    "SB Below Crow Town Gazeworm Eye": LocationData(104, "Septemburg Crow Town Tunnel Top"),  # needs fishing rod,
    "SB Crow Town Shop Repulsing Root": LocationData(102, "Septemburg Crow Town"),
    "SB Crow Town Shop Kear": LocationData(103, "Septemburg Crow Town"),
    "SB Crow Town Farmhouse Roof Chest": LocationData(99, "Septemburg Farm House Roof"),  # needs burrow, carry/throw,
    "SB Tangled Woods Hidden Grove Chest": LocationData(97, "Septemburg Tangled Woods Hidden Grove"),  # needs burrow,
    "SB Galloway Room Chest": LocationData(100, "Septemburg Tangled Woods Kid Room"),  # needs burrow, float,
    "SB Stormwatch Way Chest": LocationData(101, "Septemburg Stormwatch Wind"),  # needs burrow,
    "SB Carving Shack Health Rose": LocationData(95, "Septemburg Carving Shack Arena"),

    "SB Dark Deluxy Spark Container": LocationData(353, "Septemburg Windy Generator"),  # needs burrow, pipes,
    "SB Wastewater Canal Spincer": LocationData(108, "Septemburg Wastewater Canal Well Entrance"),  # needs fishing rod,
    "SB Wastewater Canal Slime Room Chest": LocationData(106, "Septemburg Wastewater Canal Slime Room"),
    # needs burrow,
    "SB Wastewater Canal Box Room Chest": LocationData(105, "Septemburg Wastewater Canal Boxes"),  # needs burrow,
    "SB Wastewater Canal Well Entrance Chest": LocationData(107, "Septemburg Wastewater Canal Well Entrance"),
}


boss_locations: dict[str, LocationData] = {
    "SB The Carving Man": LocationData(None, "Septemburg Carving Shack Arena"),
    "SB Windy Generator Activated": LocationData(None, "Septemburg Windy Generator"),  # needs float, burrow,
    "SB Dark Deluxy": LocationData(None, "Septemburg Windy Generator"),  # needs burrow, pipes,
}