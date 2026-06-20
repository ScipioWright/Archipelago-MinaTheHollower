from collections import ChainMap

from ._generated import eastern_hearth_edges, mourners_mile_edges, ossex_edges, queensbury_crypt_edges, \
    southern_outskirts_edges, western_wilds_edges, ossex_train_edges, sandfalls_edges, loners_landing_edges, \
    backwaters_edges, bayou_edges, septemburg_edges, bone_beach_edges, kindlewood_edges, coltrane_peak_edges, \
    radiant_manor_edges, astral_orrery_edges
from .areas import astral_orrery, bayou, bone_beach, coltrane_peak, eastern_hearth, kindlewood, loners_landing, mourners_mile, ossex, queensbury_crypt, radiant_manor, sandfalls, septemburg, southern_outskirts, backwaters, western_wilds
from .. import LocationData, RegionConnection, Transition

all_collectables: ChainMap[str, LocationData] = ChainMap(
    astral_orrery.collectable_locations,
    bayou.collectable_locations,
    bone_beach.collectable_locations,
    coltrane_peak.collectable_locations,
    eastern_hearth.collectable_locations,
    kindlewood.collectable_locations,
    loners_landing.collectable_locations,
    mourners_mile.collectable_locations,
    ossex.collectable_locations,
    queensbury_crypt.collectable_locations,
    radiant_manor.collectable_locations,
    sandfalls.collectable_locations,
    septemburg.collectable_locations,
    southern_outskirts.collectable_locations,
    backwaters.collectable_locations,
    western_wilds.collectable_locations,
)

all_bosses: ChainMap[str, LocationData] = ChainMap(
    # astral_orrery.boss_locations,
    # bayou.boss_locations,
    # bone_beach.boss_locations,
    # coltrane_peak.boss_locations,
    eastern_hearth.boss_locations
    # kindlewood.boss_locations,
    # loners_landing.boss_locations,
    # mourners_mile.boss_locations,
    # ossex.boss_locations,
    # queensbury_crypt.boss_locations,
    # radient_manor.boss_locations,
    # sandfalls.boss_locations,
    # septemburg.boss_locations,
    # southern_outskirts.boss_locations,
    # backwaters.boss_locations,
    # western_wilds.boss_locations,
)

all_locations: ChainMap[str, LocationData] = ChainMap(
    all_collectables,
    all_bosses
)

temp_regions: set[str] = {
    "Radiant Manor Foyer",
    "Astral Orrey Mirror's End"
}

all_regions: set[str] = set.union(
    temp_regions,
    astral_orrery_edges.regions,
    bayou_edges.regions,
    bone_beach_edges.regions,
    coltrane_peak_edges.regions,
    eastern_hearth_edges.regions,
    kindlewood_edges.regions,
    loners_landing_edges.regions,
    mourners_mile_edges.regions,
    ossex_edges.regions,
    ossex_train_edges.regions,
    queensbury_crypt_edges.regions,
    radiant_manor_edges.regions,
    sandfalls_edges.regions,
    septemburg_edges.regions,
    southern_outskirts_edges.regions,
    backwaters_edges.regions,
    western_wilds_edges.regions,
)

all_internal_region_connections: ChainMap[str, RegionConnection] = ChainMap(
    astral_orrery_edges.connections,
    bayou_edges.connections,
    bone_beach_edges.connections,
    coltrane_peak_edges.connections,
    eastern_hearth_edges.connections,
    kindlewood_edges.connections,
    loners_landing_edges.connections,
    mourners_mile_edges.connections,
    ossex_edges.connections,
    ossex_train_edges.connections,
    queensbury_crypt_edges.connections,
    radiant_manor_edges.connections,
    sandfalls_edges.connections,
    septemburg_edges.connections,
    southern_outskirts_edges.connections,
    backwaters_edges.connections,
    western_wilds_edges.connections,
)

all_region_transitions: ChainMap[str, Transition] = ChainMap(
    astral_orrery_edges.transitions,
    bayou_edges.transitions,
    bone_beach_edges.transitions,
    coltrane_peak_edges.transitions,
    eastern_hearth_edges.transitions,
    kindlewood_edges.transitions,
    loners_landing_edges.transitions,
    mourners_mile_edges.transitions,
    ossex_edges.transitions,
    ossex_train_edges.transitions,
    queensbury_crypt_edges.transitions,
    radiant_manor_edges.transitions,
    sandfalls_edges.transitions,
    septemburg_edges.transitions,
    southern_outskirts_edges.transitions,
    backwaters_edges.transitions,
    western_wilds_edges.transitions,
)