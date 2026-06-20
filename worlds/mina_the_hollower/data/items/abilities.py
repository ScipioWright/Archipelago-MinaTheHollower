from BaseClasses import ItemClassification
from .. import ItemData
from ...constants import OFFSET_ABILITY_ITEMS

astral_platforms: dict[str, ItemData] = {
    "Green Astral Platforms": ItemData(500, ItemClassification.progression),
    "Red Astral Platforms": ItemData(501, ItemClassification.progression),
    "Blue Astral Platforms": ItemData(502, ItemClassification.progression),
    "Yellow Astral Platforms": ItemData(503, ItemClassification.progression),
    "Purple Astral Platforms": ItemData(504, ItemClassification.progression),
}
abilities: dict[str, ItemData] = {
    "Burrow" : ItemData(OFFSET_ABILITY_ITEMS, ItemClassification.progression),
    "Swim" : ItemData(OFFSET_ABILITY_ITEMS+1, ItemClassification.progression),
    "Bounce" : ItemData(OFFSET_ABILITY_ITEMS+2, ItemClassification.progression),
    "Carry" : ItemData(OFFSET_ABILITY_ITEMS+3, ItemClassification.progression),
    "Climb" : ItemData(OFFSET_ABILITY_ITEMS+4, ItemClassification.progression),
}

