from BaseClasses import Item, Location, ItemClassification
from .data import AnyItemData
from .data.items import all_key_items, all_filler_items,kears
from .constants import MINA_THE_HOLLOWER
from .data.items.key_items import base_items
from .data.items.abilities import abilities


class MinaTheHollowerItem(Item):
    game: str = MINA_THE_HOLLOWER

def create_item(world, name: str, item: AnyItemData):
    print(f"count: {item.amount} name: {name} class: {item.classification}")
    for i in range(item.amount):
        world.itempool.append(Item(name, item.classification, item.item_id, world.player))


def create_items(world):
    #TODO: create logic for what items are in the world
    for item, data in all_key_items.items():
        create_item(world, item, data)
    if world.options.kear_rando.value == 0:
        create_item(world,"Kear",kears.single_kear["Kear"])
    elif world.options.kear_rando.value == 1:
        for item, data in kears.unique_kears.items():
            create_item(world, item, data)
    elif world.options.kear_rando.value == 2:
        for item, data in kears.area_kears.items():
            create_item(world, item, data)

    total_location_count = len(world.multiworld.get_unfilled_locations(world.player))
    print(f"total locs at start {total_location_count}")
    print(f"total Itempool at start {len(world.itempool)}")
    remaining = total_location_count - len(world.itempool)
    for x in range(remaining):
        name, data = world.random.choice(list(all_filler_items.items()))
        create_item(world, name, data)
    world.multiworld.itempool += world.itempool
    starting_items = []
    for item, data in abilities.items():
        for i in range(data.amount):
            starting_items.append(Item(item, data.classification, data.item_id, world.player))
    for item, data in base_items.items():
        for i in range(data.amount):
            starting_items.append(Item(item, data.classification, data.item_id, world.player))
    return starting_items



def create_events(world):
    region_gen = {
        "Astral Orrery" : "Starry",
        "Queensbury Crypt" : "Solemn",
        "Coltrane Peak": "Frozen",
        "Septemburg": "Windy",
        "Bone Beach": "Shoreline",
        "Nox's Bayou": "Swampy"
    }
    starting_region = world.get_region(
        "Ossex City Center Main") if world.options.ossex_start.value else world.get_region(
        "Loner's Landing Shipwreck")
    for area, name in region_gen.items():

        if area in world.options.excluded_areas.value:
            region = starting_region
        else:
            region = world.get_region(area + " " + name + " Generator")
        event_loc = Location(world.player, "Repair" + area + "Generator", None, region)
        event_loc.place_locked_item(MinaTheHollowerItem("Repair " + name + " Generator", ItemClassification.progression, None, world.player))
        region.locations.append(event_loc)