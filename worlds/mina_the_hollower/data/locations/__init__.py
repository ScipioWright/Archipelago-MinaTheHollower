from collections import ChainMap

from ._generated import eastern_hearth_edges, mourners_mile_edges, ossex_edges, queensbury_crypt_edges, \
    southern_outskirts_edges, western_wilds_edges, ossex_train_edges, sandfalls_edges
from .areas import astral_orrery, bayou, bone_beach, coltrane_peak, eastern_hearth, kindlewood, loners_landing, mourners_mile, ossex, queensbury_crypt, radient_manor, sandfalls, septemburg, southern_outskirts, backwaters, western_wilds
from .. import LocationData, RegionConnection, Transition

all_collectables: ChainMap[str, LocationData] = ChainMap(
# astral_orrery.collectable_locations,
# bayou.collectable_locations,
# bone_beach.collectable_locations,
# coltrane_peak.collectable_locations,
eastern_hearth.collectable_locations,
# kindlewood.collectable_locations,
# loners_landing.collectable_locations,
mourners_mile.collectable_locations,
ossex.collectable_locations,
queensbury_crypt.collectable_locations,
# radient_manor.collectable_locations,
# sandfalls.collectable_locations,
# septemburg.collectable_locations,
southern_outskirts.collectable_locations,
# backwaters.collectable_locations,
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
    "Loners Landing ???",
    "Kindlewood Overgrowth entry region from WW",
    "Swamp ???",
    "Sandfalls ???? Bone junction)",
    "Astral Orrey Mirror's End"
}

all_regions: set[str] = set.union(
    temp_regions,
    # astral_orrery.regions,
    # bayou.regions,
    # bone_beach.regions,
    # coltrane_peak.regions,
    eastern_hearth_edges.regions,
    # kindlewood.regions,
    # loners_landing.regions,
    mourners_mile_edges.regions,
    ossex_edges.regions,
    ossex_train_edges.regions,
    queensbury_crypt_edges.regions,
    # radient_manor.regions,
    sandfalls_edges.regions,
    # septemburg.regions,
    southern_outskirts_edges.regions,
    # backwaters.regions,
    western_wilds_edges.regions,
)

all_internal_region_connections: ChainMap[str, RegionConnection] = ChainMap(
    # astral_orrery.connections,
    # bayou.connections,
    # bone_beach.connections,
    # coltrane_peak.connections,
    eastern_hearth_edges.connections,
    # kindlewood.connections,
    # loners_landing.connections,
    mourners_mile_edges.connections,
    ossex_edges.connections,
    ossex_train_edges.connections,
    queensbury_crypt_edges.connections,
    # radient_manor.connections,
    sandfalls_edges.connections,
    # septemburg.connections,
    southern_outskirts_edges.connections,
    # backwaters.connections,
    western_wilds_edges.connections,
)

all_region_transitions: ChainMap[str, Transition] = ChainMap(
    # astral_orrery.transitions,
    # bayou.transitions,
    # bone_beach.transitions,
    # coltrane_peak.transitions,
    eastern_hearth_edges.transitions,
    # kindlewood.transitions,
    # loners_landing.transitions,
    mourners_mile_edges.transitions,
    ossex_edges.transitions,
    ossex_train_edges.transitions,
    queensbury_crypt_edges.transitions,
    # radient_manor.transitions,
    sandfalls_edges.transitions,
    # septemburg.transitions,
    southern_outskirts_edges.transitions,
    # backwaters.transitions,
    western_wilds_edges.transitions,
)