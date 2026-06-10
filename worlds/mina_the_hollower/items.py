from BaseClasses import Item
from .data import ItemData, AnyItemData
from .data.items import all_items, required_test_items
from .constants import MINA_THE_HOLLOWER
from .data.items.abilities import abilities
from .data.items.incrementals import filler
from .data.items.kears import kears


class MinaTheHollowerItem(Item):
    game: str = MINA_THE_HOLLOWER

def create_item(world, name: str, item: AnyItemData):
    print(f"count: {item.amount} name: {name} class: {item.classification}")
    for i in range(item.amount):
        world.itempool.append(Item(name, item.classification, item.item_id, world.player))


def create_items(world):
    #TODO: create logic for what items are in the world
    #TODO: calculate how much filler needs to go in the world
    #TODO: calculate traps
    for item, data in kears.items():
        create_item(world, item, data)
    for item, data in required_test_items.items():
        create_item(world, item, data)
    total_location_count = len(world.multiworld.get_unfilled_locations(world.player))
    print(f"total locs at start {total_location_count}")
    print(f"total Itempool at start {len(world.itempool)}")
    remaining = total_location_count - len(world.itempool)
    for x in range(remaining):
        create_item(world, "BoneDust", filler["BoneDust"])
    world.multiworld.itempool += world.itempool
    starting_items = {}
    return starting_items
