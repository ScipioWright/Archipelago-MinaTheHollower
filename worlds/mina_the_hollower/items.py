from BaseClasses import Item, Location, ItemClassification
from .data import ItemData, AnyItemData
from .data.items import all_items, required_test_items
from .constants import MINA_THE_HOLLOWER
from .data.items.abilities import abilities
from .data.items.incrementals import filler
from .data.items.kears import kears
from .data.items.trinkets import movement_trinkets


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
    for item, data in movement_trinkets.items():
        create_item(world, item, data)
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



def create_events(world):


    starry = Location(world.player, "Repair Starry Generator", None, world.get_region("Astral Orrery Starry Generator"))
    frozen = Location(world.player, "Repair Frozen Generator", None, world.get_region("Coltrane Peak Frozen Generator"))
    windy = Location(world.player, "Repair Windy Generator", None, world.get_region("Septemburg Windy Generator"))
    Shoreline = Location(world.player, "Repair Shoreline Generator", None, world.get_region("Bone Beach Worms Back Generator"))
    Swampy = Location(world.player, "Repair Swampy Generator", None, world.get_region("Nox's Bayou Swampy Generator"))
    Solemn = Location(world.player, "Repair Solemn Generator", None, world.get_region("Queensbury Crypt Solemn Generator"))
    starry.place_locked_item(MinaTheHollowerItem("Repair Starry Generator", ItemClassification.progression, None, world.player))