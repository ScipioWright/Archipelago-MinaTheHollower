from BaseClasses import ItemClassification
from .. import ItemData
from ...constants import OFFSET_ABILITY_ITEMS

abilities: dict[str, ItemData] = {
    "Burrow" : ItemData(OFFSET_ABILITY_ITEMS, ItemClassification.progression),
    "Swim" : ItemData(OFFSET_ABILITY_ITEMS+1, ItemClassification.progression),
    "Bounce" : ItemData(OFFSET_ABILITY_ITEMS+2, ItemClassification.progression),
    "Carry" : ItemData(OFFSET_ABILITY_ITEMS+3, ItemClassification.progression),
    "Climb" : ItemData(OFFSET_ABILITY_ITEMS+4, ItemClassification.progression),
}