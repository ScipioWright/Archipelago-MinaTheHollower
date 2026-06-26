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

eastern_heath: dict[int, int] = {
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
cave_eastern_heath: dict[int, int] = {
    19: 0,
    20: 0
}
under_eastern_heath: dict[int, int] = {
    23:0,
    18:0,
    26:0,
    24:0,
    21:0
}

ossex_main: dict[int, int] = {
    10:0,
    11:0,
    12:0,
    20:0,
    4:1,

}

ossex_high_street: dict[int, int] = {
    6: 0
}

ossex_bowery: dict[int, int] = {
    5: 0
}

balcony: dict[int, int] = {
    10:0,
    15:0,
}
goddred_tomb: dict[int, int] = {
    0:0,
    1:0,
    2:0,
    3:0,
}

#ALl residence are the same area
high_street_r_bottom: dict[int, int] = {
    35:0,
    16:1,
    32: 2,
    31: 2,
    33: 2,
    38:2,
    39:2,
    24:2
}
high_street_r_top: dict[int, int] = {
    34:0,
}

atelier: dict[int, int] = {
    17:0,
    25:0,
}
training_center: dict[int, int] = {
    18:0,
}
os_sewers: dict[int, int] = {
    40:0,
}

os_burrowers: dict[int, int] = {
    14:0,
    19:0,
}
os_shop: dict[int, int] = {
    13:0,
}

os_kear: dict[int, int] = {
    22:0,
}
os_pawnty: dict[int, int] = {
    26:0,
}
os_weapons: dict[int, int] = {
    2:0,
}
os_trinket: dict[int, int] = {
    1:0,
}
os_couples: dict[int, int] = {
    23:0,
}
os_music: dict[int, int] = {
    3:0,
}
os_train_lower: dict[int, int] = {
    28:0,
}
os_train: dict[int, int] = {
    8:0,
}

train_caboose: dict[int, int] = {
    1:0,
}
train_interior: dict[int, int] = {
    5:0,
}
train_cabins: dict[int, int] = {
    6:0,
}
train_out: dict[int, int] = {
    3:0,
}
train_engine: dict[int, int] = {
    2:0,
}

@dataclasses.dataclass
class MapData:
    lookup: dict[int, int]
    start_index: int

area_id_to_map: dict[int, MapData] = {
    184: MapData(loners_landing, 0),
    59: MapData(southern_outskirts, 7),
    61: MapData(cave_network, 11),
    92: MapData(mining_passage, 12),
    54: MapData(eastern_heath, 13),
    53: MapData(under_eastern_heath, 16),
    52: MapData(cave_eastern_heath, 16),
    144: MapData(balcony, 17),
    153: MapData(ossex_main, 17),
    151: MapData(ossex_high_street, 18),
    163: MapData(ossex_bowery, 18),
    147: MapData(goddred_tomb, 19),
    161: MapData(high_street_r_bottom, 20),
    165: MapData(high_street_r_top, 20),
    162: MapData(atelier, 20),
    164: MapData(training_center, 20),
    152: MapData(os_sewers, 20),
    158: MapData(os_burrowers, 21),
    159: MapData(os_shop, 21),
    160: MapData(os_kear, 21),
    149: MapData(os_pawnty, 21),
    157: MapData(os_weapons, 21),
    155: MapData(os_trinket, 21),
    166: MapData(os_couples, 21),
    154: MapData(os_music, 22),
    150: MapData(os_train_lower, 22),
    148: MapData(os_train, 22),
    177: MapData(train_caboose, 23),
    176: MapData(train_interior, 23),
    178: MapData(train_cabins, 23),
    179: MapData(train_out, 23),
    180: MapData(train_engine, 23),
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