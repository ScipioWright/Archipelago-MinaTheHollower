import dataclasses


def range_incl(a: int, b: int) -> range:
    return range(a, b+1)

#Images for a single map Id
loners_landing: dict[int, int] = {
    0: 1,
    17: 1,
    18: 1,
    11: 2,
    19: 3,
    3: 4,
    2: 4,
    8: 4,
    16: 4,
    6: 5,
    4: 5,
    9: 6,
    13: 7,
    14: 8,
    7: 8,
    10: 8,
    23: 9,
    22: 9,
    28: 9,
    21: 9,
    15: 10,
}

southern_outskirts: dict[int, int] = {
    15: 0,
    6: 1,
    4: 1,
    0: 1,
    7: 2,
    23: 2,
    22: 2,
    10: 3,
    11: 3,
    12: 3,
    14: 4,
    13: 5,
    18: 6,
    16: 7,
    19: 7,
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
}

@dataclasses.dataclass
class MapData():
    lookup: dict[int, int]
    start_index: int

area_id_to_map: dict[int, MapData] = {
    184: MapData(loners_landing, 0),
    59: MapData(southern_outskirts, 11),
    61: MapData(cave_network, 19),
    54: MapData(mining_passage, 20),

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