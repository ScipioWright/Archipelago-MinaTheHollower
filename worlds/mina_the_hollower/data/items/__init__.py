from collections import ChainMap

from BaseClasses import ItemClassification
from . import trinkets, incrementals, key_items, abilities, kears
from .. import MovementItemData, AnyItemData, ItemData
from ...constants import OFFSET_ABILITY_ITEMS

all_movement_items: ChainMap[str, MovementItemData] = ChainMap(
    trinkets.movement_trinkets
)

all_filler_items: ChainMap[str, AnyItemData] = ChainMap(
    incrementals.filler
)

all_items: ChainMap[str, AnyItemData] = ChainMap(
    incrementals.filler,
    key_items.key_items,
    abilities.abilities,
    kears.kears,
)

all_traps: ChainMap[str, AnyItemData] = ChainMap(
)

required_test_items: dict[str, AnyItemData] = {
    "SparkUpgrade" : ItemData(70, ItemClassification.progression, 5),
    "TrainPass" : ItemData(94, ItemClassification.progression),
    "HUBTicket" : ItemData(95, ItemClassification.progression),
    "BayouTicket" : ItemData(96, ItemClassification.progression),
    "SeptemburgTicket" : ItemData(97, ItemClassification.progression),
    "BoneBeachTicket" : ItemData(98, ItemClassification.progression),
    "FrozenTrainyardTicket" : ItemData(99, ItemClassification.progression),
    "HealingVial": ItemData(17, ItemClassification.progression),
    "HealingVialFirst": ItemData(18, ItemClassification.progression),
    "HealingVialPickup": ItemData(19, ItemClassification.progression),
    "HealingVialPackPickup": ItemData(20, ItemClassification.progression),
    "VialUpgrade": ItemData(71, ItemClassification.progression, 5),
    "ThrowingAxe": ItemData(21, ItemClassification.progression),
    "ThrowingKnife": ItemData(22, ItemClassification.progression),
    "Burrow" : ItemData(OFFSET_ABILITY_ITEMS, ItemClassification.progression),
    "Swim" : ItemData(OFFSET_ABILITY_ITEMS+1, ItemClassification.progression),
    "Bounce" : ItemData(OFFSET_ABILITY_ITEMS+2, ItemClassification.progression),
    "Carry" : ItemData(OFFSET_ABILITY_ITEMS+3, ItemClassification.progression),
    "Climb" : ItemData(OFFSET_ABILITY_ITEMS+4, ItemClassification.progression),
    "FishingRod" : ItemData(34, ItemClassification.progression),
    "TractionTreads" : ItemData(149, ItemClassification.progression),
    "WallowersGauntlets": ItemData(181, ItemClassification.progression),

    "Green Astral Platforms" : ItemData(500, ItemClassification.progression),
    "Red Astral Platforms" : ItemData(501, ItemClassification.progression),
    "Blue Astral Platforms" : ItemData(502, ItemClassification.progression),
    "Yellow Astral Platforms" : ItemData(503, ItemClassification.progression),
    "Purple Astral Platforms" : ItemData(504, ItemClassification.progression),
}