from collections import ChainMap

from . import incrementals, key_items, abilities, kears
from .. import AnyItemData

all_filler_items: ChainMap[str, AnyItemData] = ChainMap(
    incrementals.junk,
    incrementals.BoneStone
)

all_key_items: ChainMap[str, AnyItemData] = ChainMap(
    key_items.weapons,
    key_items.key_items,
    abilities.astral_platforms,
    key_items.underlab_upgrades,
)

all_items: ChainMap[str, AnyItemData] = ChainMap(
    all_filler_items,
    key_items.weapons,
    key_items.side_arms,

    key_items.base_items,
    key_items.key_items,
    abilities.abilities,
    abilities.astral_platforms,
    kears.area_kears,
    kears.unique_kears,
    kears.single_kear,
)

all_traps: ChainMap[str, AnyItemData] = ChainMap(
)