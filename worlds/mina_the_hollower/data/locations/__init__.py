from collections import ChainMap
from .areas import astral_orrery, bayou, bone_beach, coltrane_peak, eastern_hearth, kindlewood, loners_landing, mourners_mile, ossex, queensbury_crypt, radient_manor, sandfalls, septemburg, southern_outskirts, shanty_swamp, western_wilds
from .. import LocationData, RegionConnection, Transition
from .game_locations import collectable_locations

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
radient_manor.collectable_locations,
sandfalls.collectable_locations,
septemburg.collectable_locations,
southern_outskirts.collectable_locations,
shanty_swamp.collectable_locations,
western_wilds.collectable_locations,
)

all_bosses: ChainMap[str, LocationData] = ChainMap(
    astral_orrery.bosses,
    bayou.bosses,
    bone_beach.bosses,
    coltrane_peak.bosses,
    eastern_hearth.bosses,
    kindlewood.bosses,
    loners_landing.bosses,
    mourners_mile.bosses,
    ossex.bosses,
    queensbury_crypt.bosses,
    radient_manor.bosses,
    sandfalls.bosses,
    septemburg.bosses,
    southern_outskirts.bosses,
    shanty_swamp.bosses,
    western_wilds.bosses,
)

all_locations: ChainMap[str, LocationData] = ChainMap(
    all_collectables,
    all_bosses
)

all_regions: set[str] = set.union(
    astral_orrery.regions,
    bayou.regions,
    bone_beach.regions,
    coltrane_peak.regions,
    eastern_hearth.regions,
    kindlewood.regions,
    loners_landing.regions,
    mourners_mile.regions,
    ossex.regions,
    queensbury_crypt.regions,
    radient_manor.regions,
    sandfalls.regions,
    septemburg.regions,
    southern_outskirts.regions,
    shanty_swamp.regions,
    western_wilds.regions,
)

all_internal_region_connections: ChainMap[str, RegionConnection] = ChainMap(
    astral_orrery.connections,
    bayou.connections,
    bone_beach.connections,
    coltrane_peak.connections,
    eastern_hearth.connections,
    kindlewood.connections,
    loners_landing.connections,
    mourners_mile.connections,
    ossex.connections,
    queensbury_crypt.connections,
    radient_manor.connections,
    sandfalls.connections,
    septemburg.connections,
    southern_outskirts.connections,
    shanty_swamp.connections,
    western_wilds.connections,
)

all_region_transitions: ChainMap[str, Transition] = ChainMap(
    astral_orrery.transitions,
    bayou.transitions,
    bone_beach.transitions,
    coltrane_peak.transitions,
    eastern_hearth.transitions,
    kindlewood.transitions,
    loners_landing.transitions,
    mourners_mile.transitions,
    ossex.transitions,
    queensbury_crypt.transitions,
    radient_manor.transitions,
    sandfalls.transitions,
    septemburg.transitions,
    southern_outskirts.transitions,
    shanty_swamp.transitions,
    western_wilds.transitions,
)


