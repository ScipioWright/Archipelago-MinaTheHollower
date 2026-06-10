from enum import Enum, IntEnum
from typing import NamedTuple, Any, Union

from BaseClasses import ItemClassification, LocationProgressType, CollectionState, CollectionRule
from rule_builder.rules import Rule, True_
from ..world_base import MinaTheHollowerBase




class TransitionType(IntEnum):
    DO_NOT_RANDOMIZE_ENTRANCE = 0
    SCREENS = 1 << 3
    AREA_SCREENS = 2 << 3
    DOORS = 3 << 3
    MIRRORS = 4 << 3
    STAIRS = 5 << 3
    GEYSER_UP = 6 << 3
    GEYSER_DOWN = 7 << 3
    BURROW = 8 << 3
    TRANSITION_MASK = 1 << 3


class DirectionType(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    ASTRAL = 4
    OVERWORLD = 5
    DIRECTION_MASK = (1 << 2) | (1 << 1) | 1

matching_transition_types = {
    TransitionType.SCREENS | DirectionType.NORTH: [TransitionType.SCREENS | DirectionType.SOUTH],
    TransitionType.SCREENS | DirectionType.EAST: [TransitionType.SCREENS | DirectionType.WEST],
    TransitionType.SCREENS | DirectionType.SOUTH: [TransitionType.SCREENS | DirectionType.NORTH],
    TransitionType.SCREENS | DirectionType.WEST: [TransitionType.SCREENS | DirectionType.EAST],

    TransitionType.AREA_SCREENS | DirectionType.NORTH: [TransitionType.AREA_SCREENS | DirectionType.SOUTH],
    TransitionType.AREA_SCREENS | DirectionType.EAST: [TransitionType.AREA_SCREENS | DirectionType.WEST],
    TransitionType.AREA_SCREENS | DirectionType.SOUTH: [TransitionType.AREA_SCREENS | DirectionType.NORTH],
    TransitionType.AREA_SCREENS | DirectionType.WEST: [TransitionType.AREA_SCREENS | DirectionType.EAST],

    TransitionType.DOORS | DirectionType.NORTH: [TransitionType.DOORS | DirectionType.SOUTH,
                                                 TransitionType.STAIRS | DirectionType.SOUTH,
                                                 TransitionType.STAIRS | DirectionType.NORTH],

    TransitionType.DOORS | DirectionType.EAST: [TransitionType.DOORS | DirectionType.WEST,
                                                TransitionType.STAIRS | DirectionType.WEST,
                                                TransitionType.STAIRS | DirectionType.EAST],

    TransitionType.DOORS | DirectionType.SOUTH: [TransitionType.DOORS | DirectionType.NORTH,
                                                 TransitionType.STAIRS | DirectionType.NORTH,
                                                 TransitionType.STAIRS | DirectionType.SOUTH],

    TransitionType.DOORS | DirectionType.WEST: [TransitionType.DOORS | DirectionType.EAST,
                                                TransitionType.STAIRS | DirectionType.EAST,
                                                TransitionType.STAIRS | DirectionType.WEST],

    TransitionType.MIRRORS | DirectionType.ASTRAL: [TransitionType.MIRRORS | DirectionType.OVERWORLD],
    TransitionType.MIRRORS | DirectionType.OVERWORLD: [TransitionType.MIRRORS | DirectionType.ASTRAL],

    TransitionType.STAIRS | DirectionType.NORTH: [TransitionType.DOORS | DirectionType.SOUTH,
                                                TransitionType.DOORS | DirectionType.NORTH,
                                                TransitionType.STAIRS | DirectionType.SOUTH,
                                                TransitionType.STAIRS | DirectionType.NORTH],

    TransitionType.STAIRS | DirectionType.EAST: [TransitionType.DOORS | DirectionType.WEST,
                                                TransitionType.DOORS | DirectionType.EAST,
                                                TransitionType.STAIRS | DirectionType.WEST,
                                                TransitionType.STAIRS | DirectionType.EAST],

    TransitionType.STAIRS | DirectionType.SOUTH: [TransitionType.DOORS | DirectionType.NORTH,
                                                TransitionType.DOORS | DirectionType.SOUTH,
                                                TransitionType.STAIRS | DirectionType.NORTH,
                                                TransitionType.STAIRS | DirectionType.SOUTH],

    TransitionType.STAIRS | DirectionType.WEST: [TransitionType.DOORS | DirectionType.EAST,
                                                TransitionType.DOORS | DirectionType.WEST,
                                                TransitionType.STAIRS | DirectionType.EAST,
                                                TransitionType.STAIRS | DirectionType.WEST],

}


def get_target_groups(group: int) -> list[int]:
    return matching_transition_types[group]

class ItemData(NamedTuple):
    item_id: int
    classification: ItemClassification
    amount: int = 1

class MovementItemData(NamedTuple):
    item_id: int
    distance: int
    classification: ItemClassification
    amount: int = 1

class KeyItemData(NamedTuple):
    item_id: int
    key_id: int
    classification: ItemClassification
    amount: int = 1

class RegionConnection(NamedTuple):
    exiting_region: str
    entering_region: str
    rule: CollectionRule | Rule[MinaTheHollowerBase] = True_()

class Transition(NamedTuple):
    name: str # Human-readable name
    exiting_screen: str
    entering_screen: str
    direction: int
    entrance_group: int = TransitionType.SCREENS
    rule: CollectionRule | Rule[MinaTheHollowerBase] = True_()

class LocationData(NamedTuple):
    location_id: int
    region: str
    rule: CollectionRule | Rule[MinaTheHollowerBase] = True_()
    progress_type: LocationProgressType = LocationProgressType.DEFAULT

AnyItemData: type = Union[ItemData, MovementItemData, KeyItemData]