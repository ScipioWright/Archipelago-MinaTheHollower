from BaseClasses import Region, Location
from .data.locations import all_regions, all_region_transitions, all_internal_region_connections, all_locations
from .data import LocationData, RegionConnection, Transition, matching_transition_types


def create_region(world, name: str, hint: str = ""):
    region = Region(name, world.player, world.multiworld)

    valid_locations: dict[str, (Location, LocationData)] = {}
    #TODO: dont loop through all locations for each region
    for loc_name, data in all_locations.items():
        if data.region != name:
            continue
        location = Location(world.player, loc_name, data.location_id, region)
        location.progress_type = data.progress_type
        valid_locations[loc_name] = (location, data)
        region.locations.append(location)

    world.multiworld.regions.append(region)

    for loc_name, (location, data) in valid_locations.items():
        world.set_rule(location, data.rule)

def create_regions(world, regions: set[str]):
    for region in regions:
        create_region(world, region)

def get_regions(world) ->  set[str]:
    #TODO: logic to handle which regions are being created based on yaml
    return all_regions


def create_entrances(world, regions):
    for name, data in all_region_transitions.items():
        exiting_region = world.get_region(data.exiting_screen)
        entering_region = world.get_region(data.entering_screen)
        entrance = world.create_entrance(exiting_region, entering_region, rule=data.rule, name=name, force_creation=True)
        if data.entrance_group != 0 and world.options.entrance_rando.value > 0:
            entrance.randomization_group = data.entrance_group
            world.disconnect_entrance_for_randomization(entrance)
    for name, data in all_internal_region_connections.items():
        exiting_region = world.get_region(data.exiting_region)
        entering_region = world.get_region(data.entering_region)
        entrance = world.create_entrance(exiting_region, entering_region, rule=data.rule, name=name,
                                         force_creation=True)