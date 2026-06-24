import dataclasses


def range_incl(a: int, b: int) -> range:
    return range(a, b+1)

#Images for a single map Id
loners_landing: dict[int, int] = {
    0: 1,
    17: 1,
    18: 1,
    11: 1,
    19: 2,
    3: 3,
    2: 3,
    8: 3,
    16: 3,
    6: 4,
    4: 4,
    9: 4,
    13: 4,
    14: 5,
    15: 5,
    7: 5,
    10: 5,
    23: 6,
    22: 6,
    28: 6,
    21: 6,
}

southern_outskirts: dict[int, int] = {
    15: 0,
    6: 0,
    4: 0,
    0: 0,
    7: 0,
    23:0,
    22: 0,
    10: 1,
    11: 1,
    12: 1,
    14: 1,
    13: 1,
    16: 2,
    19: 3,
}

so_poppit: dict[int, int] = {
    18:0
}
cave_network: dict[int, int] = {
    9: 0,
    17: 0,
}

mining_passage: dict[int, int] = {
    8: 0,
    7: 0,
    6: 0,
    9: 0,
    15: 0,
}

eastern_hearth: dict[int, int] = {
    0: 0,
    1: 0,
    3: 0,
    5: 0,
    6: 0,
    8: 0,
    15: 0,
    16: 0,
    17: 0,
    4: 1,
    7: 1,
    11: 2,
}
cave_eastern_hearth: dict[int, int] = {
    19: 0,
    20: 0
}
under_eastern_hearth: dict[int, int] = {
    23:0,
    18:0,
    26:0,
    24:0,
    21:0
}

@dataclasses.dataclass
class MapData():
    lookup: dict[int, int]
    start_index: int

area_id_to_map: dict[int, MapData] = {
    184: MapData(loners_landing, 0),
    59: MapData(southern_outskirts, 7),
    61: MapData(cave_network, 11),
    92: MapData(mining_passage, 12),
    54: MapData(eastern_hearth, 13),
    53: MapData(under_eastern_hearth, 16),
    52: MapData(cave_eastern_hearth, 16),

}


def map_page_index(data: int) -> int:
    if data is None or data == "":
        return 0

    data = int(data)
    area = (data >> 16) & 0xFFFF
    screen = data & 0xFFFF

    if area not in area_id_to_map:
        return 0

    map_data = area_id_to_map[area]

    if screen not in map_data.lookup:
        return 0
    return map_data.start_index + map_data.lookup[screen]