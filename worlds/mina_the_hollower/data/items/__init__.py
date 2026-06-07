from collections import ChainMap

from . import trinkets, incrementals, key_items, abilities, kears
from .. import MovementItemData, AnyItemData

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
    kears.kears
)

all_traps: ChainMap[str, AnyItemData] = ChainMap(
)