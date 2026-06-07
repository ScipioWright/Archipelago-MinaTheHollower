from BaseClasses import Item
from .data import ItemData
from .data.items import all_items
from .constants import MINA_THE_HOLLOWER


class MinaTheHollowerItem(Item):
    game: str = MINA_THE_HOLLOWER

def create_item(world, name: str, item: ItemData):
    print(f"count: {item.amount} name: {name} class: {item.classification}")
    for i in range(item.amount):
        world.itempool.append(Item(name, item.classification, item.item_id, world.player))


def create_items(world):
    #TODO: create logic for what items are in the world
    #TODO: calculate how much filler needs to go in the world
    #TODO: calculate traps
    for item, data in all_items.items():
        create_item(world, item, data)
    total_location_count = len(world.multiworld.get_unfilled_locations(world.player))
    print(f"total locs at start {total_location_count}")
    print(f"total Itempool at start {len(world.itempool)}")
    world.multiworld.itempool += world.itempool
    starting_items = {}
    return starting_items
