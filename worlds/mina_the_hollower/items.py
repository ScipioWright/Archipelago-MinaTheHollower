from BaseClasses import Item, Location, ItemClassification
from .constants import MINA_THE_HOLLOWER
from .data import ItemData, ItemTypeEnum, ItemFiller
from .data.items import Kear, SingleKears, AreaKears, base_items, Abilities, BoneUps, GenericBoneUp, all_filler_items, \
    PermanentUpgrades, Sidearms, PlayerUpgrades, AstralPlatforms, upgrade_items, Trinkets


class MinaTheHollowerItem(Item):
    game: str = MINA_THE_HOLLOWER

def create_item(world, item: ItemData):
    for i in range(item.amount):
        world.itempool.append(Item(item.type.value, item.type.classification, item.type.item_id, world.player))

def create_single_item(world, item_type: ItemTypeEnum):
    world.itempool.append(Item(item_type.value, item_type.classification, item_type.item_id, world.player))

def create_items(world):
    starting_items = []
    #starting items
    for item in base_items:
        if world.options.random_starting_items.value:
            create_item(world, item)
        else:
            for i in range(item.amount):
                starting_items.append(Item(item.type.value, item.type.classification, item.type.item_id, world.player))
    for item_type in Abilities:
        # Spring is folded into Bounce for now
        # TODO: Add Spring as a seperate ability and account for it in logic
        if item_type is Abilities.SPRING:
            continue
        if item_type.value in world.options.ability_rando.value:
            create_single_item(world, item_type)
        else:
            starting_items.append(Item(item_type.value, item_type.classification, item_type.item_id, world.player))


    for item_type in PermanentUpgrades:
        create_single_item(world, item_type)

    for item in upgrade_items:
        create_item(world, item)

    for item_type in Trinkets:
        create_single_item(world, item_type)

    if world.options.kear_rando.value == 0:
        create_item(world,ItemData(Kear.UNIVERSAL_KEAR, 50))
    elif world.options.kear_rando.value == 1:
        for item_type in SingleKears:
            create_single_item(world, item_type)
    elif world.options.kear_rando.value == 2:
        for item_type in AreaKears:
            create_single_item(world, item_type)

    if world.options.bone_up_cap.value == 0:
        for item_type in BoneUps:
            create_item(world, ItemData(item_type, 9))
    else:
        create_item(world, ItemData(GenericBoneUp.ALL_BONE_UP_CAP, 9))


    total_location_count = len(world.multiworld.get_unfilled_locations(world.player))
    print(f"total locs at start {total_location_count}")
    print(f"total Itempool at start {len(world.itempool)}")
    remaining = total_location_count - len(world.itempool)

    filler: list[ItemFiller] = world.random.choices(
        all_filler_items,
        weights=[item.weight for item in all_filler_items],
        k=remaining
    )
    for item_filler in filler:
        create_single_item(world, item_filler.type)

    world.multiworld.itempool += world.itempool


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

    for item_type in Sidearms:
        event_loc = Location(world.player, "Start " + item_type.value, None, starting_region)
        event_loc.place_locked_item(
            MinaTheHollowerItem(item_type.value, ItemClassification.progression, None, world.player))
        starting_region.locations.append(event_loc)
        # starting_items.append(Item(item_type.value, item_type.classification, item_type.item_id, world.player))

    for area, name in region_gen.items():

        # if area in world.options.excluded_areas.value:
        #     region = starting_region
        # else:
        region = world.get_region(area + " " + name + " Generator")


        event_loc = Location(world.player, "Repair" + area + "Generator", None, region)
        event_loc.place_locked_item(MinaTheHollowerItem("Repair " + name + " Generator", ItemClassification.progression, None, world.player))
        region.locations.append(event_loc)

    blue_region = world.get_region("Astral Orrery Queensbury Mirror")
    event_loc_blue = Location(world.player, "Blue Switch", None, blue_region)
    event_loc_blue.place_locked_item(
        MinaTheHollowerItem(AstralPlatforms.BLUE_ASTRAL_PLATFORMS.value, ItemClassification.progression, None, world.player))
    blue_region.locations.append(event_loc_blue)

    green_region = world.get_region("Astral Orrery Bayou Mirror")
    event_loc_green = Location(world.player, "Green Switch", None, green_region)
    event_loc_green.place_locked_item(
        MinaTheHollowerItem(AstralPlatforms.GREEN_ASTRAL_PLATFORMS.value, ItemClassification.progression, None,
                            world.player))
    green_region.locations.append(event_loc_green)

    red_region = world.get_region("Astral Orrery Bone Beach Mirror")
    event_loc_red = Location(world.player, "Red Switch", None, red_region)
    event_loc_red.place_locked_item(
        MinaTheHollowerItem(AstralPlatforms.RED_ASTRAL_PLATFORMS.value, ItemClassification.progression, None,
                            world.player))
    red_region.locations.append(event_loc_red)

    yellow_region = world.get_region("Astral Orrery Septemburg Mirror")
    event_loc_yellow = Location(world.player, "Yellow Switch", None, yellow_region)
    event_loc_yellow.place_locked_item(
        MinaTheHollowerItem(AstralPlatforms.YELLOW_ASTRAL_PLATFORMS.value, ItemClassification.progression, None,
                            world.player))
    yellow_region.locations.append(event_loc_yellow)

    purple_region = world.get_region("Astral Orrery Coltrane Peak Mirror")
    event_loc_purple = Location(world.player, "Purple Switch", None, purple_region)
    event_loc_purple.place_locked_item(
        MinaTheHollowerItem(AstralPlatforms.PURPLE_ASTRAL_PLATFORMS.value, ItemClassification.progression, None,
                            world.player))
    purple_region.locations.append(event_loc_purple)


    goal_region = world.get_region("Radiant Manor Prime Generator")
    goal_event = Location(world.player, "Defeat Giga Lionel", None, goal_region)
    goal_event.place_locked_item(
        MinaTheHollowerItem("Victory", ItemClassification.progression, None,
                            world.player))
    purple_region.locations.append(goal_event)
