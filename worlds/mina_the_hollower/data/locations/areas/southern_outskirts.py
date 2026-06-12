from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from ... import RegionConnection, Transition, LocationData, TransitionType, DirectionType
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanJumpTiles, CanBounce, HasVialsCount, CanClimb

collectable_locations: dict[str, LocationData] = {
    "SO Commons Ossex Entry Left Chest" : LocationData(270, "SO Commons Ossex Entry", CanBurrow() & (CanJumpTiles(distance=6) | CanBounce()) ),
    "SO Commons Ossex Entry Right Chest" : LocationData(266, "SO Commons Ossex Entry", Has("Ossex High Street SE Garden Kear")),
    "SO Commons Chest" : LocationData(264, "SO Commons Main", CanBurrow() & CanBounce()),
    "SO Commons Crumblefin Head" : LocationData(274, "SO Commons Cliff", Has("FishingRod")),
    "SO Cave Network Chest" : LocationData(265, "SO Cave Network Deep"),
    "SO Cave Network Side Room Chest" : LocationData(268, "SO Cave Network Deep"),
    "SO Poppit Keri" : LocationData(272, "SO Poppit"),
    "SO Poppit Kear" : LocationData(273, "SO Poppit"),
    "SO Southern Pit Room Bonestone" : LocationData(261, "SO Commons Southern Pit Room", CanJumpTiles(distance=5)),
    "SO Western Pit Room Chest" : LocationData(267, "SO Commons Western Pit Room Main"),
    "SO Residence Primed Vial Pouch" : LocationData(269, "SO Residence Basement"),
    "SO Mining Passage Chest" : LocationData(331, "SO Mining Passage Secret"),
    "SO Moonbath Lace Glove" : LocationData(263, "SO Moonbath"),
    "SO Four Flowers Chest" : LocationData(271, "SO Four Flowers", CanBounce()),
}

bosses: dict[str, LocationData] = {
}

regions: set[str] = {
    "SO Commons Ossex Entry",
    "SO Commons Main",
    "SO Commons Upper",
    "SO Commons Burned",
    "SO Commons Cliff",
    "SO Commons Cave Entrance",
    "SO Commons Rooftop",
    "SO Commons Rebel",
    "SO Commons Residence Roof",
    "SO Rebel Barracks",
    "SO Rebel Barracks West",
    "SO Rebel Barracks Gauntlet",
    "SO Rebel Barracks Prison",
    "SO Rebel Barracks Companion Start",
    "SO Rebel Barracks Companion End",
    "SO Rebel Barracks Fight",
    "SO Commons East Ossex",
    "SO Commons West Ossex",
    "SO Moonbath",
    "SO Residence Main",
    "SO Residence Top",
    "SO Residence Basement",
    "SO Commons Southern Pit Room Main",
    "SO Commons Southern Pit Room Roof",
    "SO Commons Western Pit Room Main",
    "SO Commons Western Pit Room Pit",
    "SO Cave Network Main",
    "SO Cave Network Deep",
    "SO Cave Network Deep Exit",
    "SO Cave Network End",
    "SO Cave Network Mining Passage Entrance",
    "SO Cave Network Deep Entrance",
    "SO Cave Network Deep Arena",
    "SO Cave Network Deep Exit Region",
    "SO Poppit",
    "SO Mining Passage Entrance Entrance",
    "SO Mining Passage Entrance Main",
    "SO Mining Passage Entrance Exit",
    "SO Mining Passage Fence",
    "SO Mining Passage Empty",
    "SO Mining Passage Exit",
    "SO Mining Passage Secret",
    "SO Four Flowers Sandfall",
    "SO Four Flowers Shortcut",
}

connections: dict[str, RegionConnection] = {
    # --- SO Commons Main sub-regions ---
    "SO Commons Main_Cave Entrance":
        RegionConnection("SO Commons Main","SO Commons Cave Entrance", CanBounce()),
    "SO Commons Main_Burned":
        RegionConnection("SO Commons Main","SO Commons Burned",
                   CanJumpTiles(distance=4)),
    "SO Commons Main_Cliff":
        RegionConnection("SO Commons Main", "SO Commons Cliff",
                    CanBurrow() & CanBounce() & CanClimb()),
    "SO Commons Main_Rooftop":
        RegionConnection("SO Commons Main","SO Commons Rooftop",
                    Has("SO Rooftop Kear")),

    # --- SO Commons Cave Entrance ---
    "SO Commons Cave Entrance_Main":
        RegionConnection("SO Commons Cave Entrance","SO Commons Main", CanBounce()),

    # --- SO Commons Upper ---
    "SO Commons Upper_Burned":
        RegionConnection("SO Commons Upper","SO Commons Burned"),

    # --- SO Commons Burned ---
    "SO Commons Burned_Main":
        RegionConnection("SO Commons Burned","SO Commons Main"),
    "SO Commons Burned_Cliff":
        RegionConnection("SO Commons Burned","SO Commons Cliff",
                    CanBurrow() & CanBounce()),

    # --- SO Commons Cliff ---
    "SO Commons Cliff_Main":
        RegionConnection("SO Commons Cliff","SO Commons Main", CanClimb()),

    # --- SO Commons Rooftop ---
    "SO Commons Rooftop_Main":
        RegionConnection("SO Commons Rooftop","SO Commons Main", CanBurrow()),

    # --- SO Commons Rebel ---
    "SO Commons Rebel_Rooftop":
        RegionConnection("SO Commons Rebel","SO Commons Rooftop", CanClimb()),

    # --- SO Rebel Barracks Companion Start <-> End ---
    "SO Rebel Barracks Companion Start_End":
        RegionConnection("SO Rebel Barracks Companion Start", "SO Rebel Barracks Companion End",
                CanBurrow()),
    "SO Rebel Barracks Companion End_Start":
        RegionConnection( "SO Rebel Barracks Companion End", "SO Rebel Barracks Companion Start",
                CanBurrow()),

    # --- SO Residence Main <-> Top ---
    "SO Residence Top_Main":
        RegionConnection("SO Residence Top","SO Residence Main"),

    # --- SO Commons Western Pit Room Main <-> Pit ---
    # "Jump 4 tiles OR Burrow" to get from Main into Pit
    "SO Commons Western Pit Room Main_Pit":
        RegionConnection( "SO Commons Western Pit Room Main", "SO Commons Western Pit Room Pit",
                CanJumpTiles(distance=4) | CanBurrow()),
    "SO Commons Western Pit Room Pit_Main":
        RegionConnection("SO Commons Western Pit Room Pit", "SO Commons Western Pit Room Main",
                CanJumpTiles(distance=4)),

    # --- SO Cave Network Main <-> End ---
    "SO Cave Network Main_End":
        RegionConnection("SO Cave Network Main","SO Cave Network End", CanBounce()),
    "SO Cave Network End_Main":
        RegionConnection("SO Cave Network End","SO Cave Network Main"),

    # --- SO Cave Network Main <-> Deep ---
    "SO Cave Network Main_Deep":
        RegionConnection("SO Cave Network Main","SO Cave Network Deep",
                        Has("SO Cave Network Kear") & CanBounce() & CanBurrow()),
    "SO Cave Network Deep_Main":
        RegionConnection("SO Cave Network Deep","SO Cave Network Main",
                         Has("SO Cave Network Kear") & CanBounce()),

    # --- SO Cave Network Deep Exit ---
    "SO Cave Network Deep Exit_Main":
        RegionConnection("SO Cave Network Deep Exit","SO Cave Network Main",
                       Has("SO Cave Network Kear") & CanBounce()),

    # --- SO Cave Network Deep Arena ---
    "SO Cave Network Deep Entrance_Arena":
        RegionConnection("SO Cave Network Deep Entrance", "SO Cave Network Deep Arena",
                        CanBurrow() & CanBounce()),
    "SO Cave Network Deep Arena_Exit":
        RegionConnection("SO Cave Network Deep Arena","SO Cave Network Deep Exit Region",
                        CanBurrow() & CanBounce()),

    # --- SO Mining Passage Entrance sub-regions ---
    "SO Mining Passage Entrance Entrance_Main":
        RegionConnection( "SO Mining Passage Entrance Entrance", "SO Mining Passage Entrance Main",
                        HasVialsCount(count=2)),  # "2 Vials"
    "SO Mining Passage Entrance Main_Entrance":
        RegionConnection( "SO Mining Passage Entrance Main", "SO Mining Passage Entrance Entrance"),
    "SO Mining Passage Entrance Main_Exit":
        RegionConnection("SO Mining Passage Entrance Main", "SO Mining Passage Entrance Exit"),

    "SO Mining Passage Entrance Exit_Main": RegionConnection( "SO Mining Passage Entrance Exit", "SO Mining Passage Entrance Main"),

    # --- SO Four Flowers Sandfall <-> Shortcut ---
    "SO Four Flowers Sandfall_Shortcut":
        RegionConnection("SO Four Flowers Sandfall","SO Four Flowers Shortcut",
                       CanBounce()),
    "SO Four Flowers Shortcut_Sandfall":
        RegionConnection("SO Four Flowers Shortcut","SO Four Flowers Sandfall",
                       CanBounce()),
}



transitions: dict[str, Transition] = {
    # --- SO Commons Ossex Entry ---
    "SO Commons Ossex Entry Area South":
        Transition("SO Commons Ossex Entry","Ossex City Center Main", DirectionType.NORTH, TransitionType.AREA_SCREENS),
    "SO Commons Ossex Entry South Commons":
        Transition("SO Commons Ossex Entry","SO Commons Main", DirectionType.SOUTH, TransitionType.SCREENS),
    "SO Commons Ossex Entry East":
        Transition( "SO Commons Ossex Entry","SO Commons East Ossex",DirectionType.EAST, TransitionType.SCREENS),
    "SO Commons Ossex Entry West":
        Transition("SO Commons Ossex Entry","SO Commons West Ossex",DirectionType.WEST, TransitionType.SCREENS),

    # --- SO Commons Main ---
    "SO Commons Main North Ossex Entry":
        Transition("SO Commons Main","SO Commons Ossex Entry", DirectionType.NORTH, TransitionType.SCREENS),
    "SO Commons Main Door North Residence":
        Transition( "SO Commons Main","SO Residence Main", DirectionType.NORTH, TransitionType.DOORS),
    "SO Commons Main Area North Loners":
        Transition( "SO Commons Main","Loners Landing ???", DirectionType.NORTH,TransitionType.AREA_SCREENS),
    # target is "Loners Landing ???"; left as-is, fill in when known
    "SO Commons Main East Pit Room":
        Transition("SO Commons Main","SO Commons Southern Pit Room Main",DirectionType.EAST, TransitionType.SCREENS),

    # --- SO Commons Cave Entrance ---
    "SO Commons Cave Entrance Stair North Cave":
        Transition("SO Commons Cave Entrance","SO Cave Network Main", DirectionType.NORTH, TransitionType.STAIRS),

    # --- SO Commons Upper ---
    "SO Commons Upper NR East Ossex":
        Transition("SO Commons Upper","SO Commons East Ossex",DirectionType.EAST,TransitionType.DO_NOT_RANDOMIZE_ENTRANCE,
                   CanBounce()),

    "SO Commons Upper Stair North Cave Network":
        Transition("SO Commons Upper","SO Cave Network Mining Passage Entrance", DirectionType.NORTH, TransitionType.STAIRS),

    # --- SO Commons Cliff ---
    "SO Commons Cliff Burrow South Poppit":
        Transition("SO Commons Cliff","SO Poppit", DirectionType.SOUTH, TransitionType.BURROW,
                       CanBurrow()),

    "SO Commons Cliff Stairs North Residence":
        Transition("SO Commons Cliff","SO Residence Main", DirectionType.NORTH, TransitionType.STAIRS),

    # --- SO Commons Rooftop ---
    "SO Commons Rooftop Door North Rebel Barracks":
        Transition("SO Commons Rooftop","SO Rebel Barracks", DirectionType.NORTH, TransitionType.DOORS,
                   HasVialsCount(count=1)),

    # --- SO Commons Residence Roof ---
    "SO Commons Residence Roof Geyser Drop Residence Top":
        Transition("SO Commons Residence Roof", "SO Residence Top", DirectionType.OVERWORLD,TransitionType.GEYSER_DOWN,
                   CanBurrow()),

    # --- SO Rebel Barracks ---
    "SO Rebel Barracks Door South Rooftop":
        Transition( "SO Rebel Barracks","SO Commons Rooftop", DirectionType.SOUTH, TransitionType.DOORS, HasVialsCount(count=1)),
    "SO Rebel Barracks West":
        Transition("SO Rebel Barracks", "SO Rebel Barracks West", DirectionType.WEST,TransitionType.SCREENS),
    "SO Rebel Barracks North Gauntlet":
        Transition("SO Rebel Barracks","SO Rebel Barracks Gauntlet",DirectionType.NORTH, TransitionType.SCREENS),

    # --- SO Rebel Barracks West ---
    "SO Rebel Barracks West East":
        Transition("SO Rebel Barracks West","SO Rebel Barracks", DirectionType.EAST,TransitionType.SCREENS),
    # --- SO Rebel Barracks Gauntlet ---
    "SO Rebel Barracks Gauntlet South Barracks":
        Transition("SO Rebel Barracks Gauntlet","SO Rebel Barracks", DirectionType.SOUTH, TransitionType.SCREENS),
    "SO Rebel Barracks Gauntlet South Prison":
        Transition("SO Rebel Barracks Gauntlet", "SO Rebel Barracks Prison", DirectionType.SOUTH, TransitionType.SCREENS),

    # --- SO Rebel Barracks Prison ---
    "SO Rebel Barracks Prison Stair North Companion Start":
        Transition( "SO Rebel Barracks Prison", "SO Rebel Barracks Companion Start",DirectionType.NORTH, TransitionType.STAIRS),

    # --- SO Rebel Barracks Companion Start ---
    "SO Rebel Barracks Companion Start Stair North Prison":
        Transition( "SO Rebel Barracks Companion Start", "SO Rebel Barracks Prison", DirectionType.NORTH, TransitionType.STAIRS),

    # --- SO Rebel Barracks Companion End ---
    "SO Rebel Barracks Companion End Stair North Fight":
        Transition("SO Rebel Barracks Companion End", "SO Rebel Barracks Fight",DirectionType.NORTH, TransitionType.STAIRS),

    # --- SO Rebel Barracks Fight ---
    "SO Rebel Barracks Fight Stair North Companion End":
        Transition("SO Rebel Barracks Fight","SO Rebel Barracks Companion End", DirectionType.NORTH, TransitionType.STAIRS),
    "SO Rebel Barracks Fight Stair North To Rebel":
        Transition("SO Rebel Barracks Fight","SO Commons Rebel", DirectionType.NORTH, TransitionType.STAIRS),
    # --- SO Commons East Ossex ---
    "SO Commons East Ossex West Ossex Entry":
        Transition("SO Commons East Ossex","SO Commons Ossex Entry", DirectionType.WEST, TransitionType.SCREENS),
    "SO Commons East Ossex East Moonbath":
        Transition( "SO Commons East Ossex", "SO Moonbath", DirectionType.EAST, TransitionType.SCREENS),
    "SO Commons East Ossex NR Upper":
        Transition("SO Commons East Ossex","SO Commons Upper", DirectionType.NORTH,TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, CanBounce()),

    # --- SO Commons West Ossex ---
    "SO Commons West Ossex East Ossex Entry":
        Transition("SO Commons West Ossex", "SO Commons Ossex Entry", DirectionType.EAST, TransitionType.SCREENS),
    "SO Commons West Ossex West Pit Room":
        Transition("SO Commons West Ossex", "SO Commons Western Pit Room Main", DirectionType.WEST, TransitionType.SCREENS),

    # --- SO Moonbath ---
    "SO Moonbath West East Ossex":
        Transition("SO Moonbath","SO Commons East Ossex", DirectionType.WEST, TransitionType.SCREENS),
    "SO Moonbath Area North Eastern Hearth":
        Transition("SO Moonbath","Eastern Hearth Bush Room", DirectionType.NORTH, TransitionType.AREA_SCREENS),

    # --- SO Residence Main ---
    "SO Residence Main Door South Commons":
        Transition("SO Residence Main","SO Commons Main", DirectionType.SOUTH, TransitionType.DOORS),

    # --- SO Residence Top ---
    "SO Residence Top Stairs North Basement":
        Transition("SO Residence Top", "SO Residence Basement", DirectionType.NORTH, TransitionType.STAIRS),


    # --- SO Residence Basement ---
    "SO Residence Basement Stairs North Top": 
        Transition("SO Residence Basement", "SO Residence Top", DirectionType.NORTH, TransitionType.STAIRS),

    "SO Residence Basement Burrow South Commons": 
        Transition("SO Residence Basement", "SO Commons Main", DirectionType.SOUTH, TransitionType.BURROW, CanBurrow()),

    # --- SO Commons Southern Pit Room Main ---
    "SO Commons Southern Pit Room Main East Commons": 
        Transition( "SO Commons Southern Pit Room Main", "SO Commons Main", DirectionType.EAST, TransitionType.SCREENS),
    "SO Commons Southern Pit Room Main North West Pit": 
        Transition( "SO Commons Southern Pit Room Main", "SO Commons Western Pit Room Main", DirectionType.NORTH, TransitionType.SCREENS),

    # --- SO Commons Southern Pit Room Roof ---
    "SO Commons Southern Pit Room Roof North West Pit Pit": 
        Transition("SO Commons Southern Pit Room Roof", "SO Commons Western Pit Room Pit",DirectionType.NORTH, TransitionType.SCREENS),
    "SO Commons Southern Pit Room Roof East Residence Roof": 
        Transition( "SO Commons Southern Pit Room Roof", "SO Commons Residence Roof", DirectionType.EAST, TransitionType.SCREENS),

    # --- SO Commons Western Pit Room Main ---
    "SO Commons Western Pit Room Main South Pit Room": 
        Transition( "SO Commons Western Pit Room Main", "SO Commons Southern Pit Room Main", DirectionType.SOUTH, TransitionType.SCREENS),
    "SO Commons Western Pit Room Main Area North": 
        Transition( "SO Commons Western Pit Room Main", "Western Wilds Overgrown Path", DirectionType.NORTH,TransitionType.AREA_SCREENS),

    # --- SO Commons Western Pit Room Pit ---
    "SO Commons Western Pit Room Pit East West Ossex": 
        Transition("SO Commons Western Pit Room Pit", "SO Commons West Ossex", DirectionType.EAST, TransitionType.SCREENS),

    "SO Commons Western Pit Room Pit South":
        Transition("SO Commons Western Pit Room Pit", "SO Commons Southern Pit Room Roof", DirectionType.SOUTH, TransitionType.SCREENS),
    # --- SO Cave Network Main ---
    "SO Cave Network Main Stair North Commons Cave Entrance": 
        Transition( "SO Cave Network Main", "SO Commons Cave Entrance", DirectionType.NORTH, TransitionType.STAIRS),

    # --- SO Cave Network Deep ---
    "SO Cave Network Deep West Deep Entrance": 
        Transition("SO Cave Network Deep","SO Cave Network Deep Entrance", DirectionType.WEST, TransitionType.SCREENS),

    # --- SO Cave Network Deep Exit ---
    "SO Cave Network Deep Exit South Deep Exit Region": 
        Transition("SO Cave Network Deep Exit","SO Cave Network Deep Exit Region", DirectionType.SOUTH, TransitionType.SCREENS),

    # --- SO Cave Network End ---
    "SO Cave Network End Stair North Commons Upper": 
        Transition("SO Cave Network End","SO Commons Upper", DirectionType.NORTH, TransitionType.STAIRS),

    # --- SO Cave Network Mining Passage Entrance ---
    "SO Cave Network Mining Passage Entrance Stair North Commons Upper": 
        Transition("SO Cave Network Mining Passage Entrance", "SO Commons Upper", DirectionType.NORTH, TransitionType.STAIRS),
    "SO Cave Network Mining Passage Entrance South Mining Entrance":
        Transition("SO Cave Network Mining Passage Entrance", "SO Mining Passage Entrance Entrance", DirectionType.SOUTH, TransitionType.SCREENS),

    # --- SO Cave Network Deep Entrance ---
    "SO Cave Network Deep Entrance East Cave Network Deep":
        Transition("SO Cave Network Deep Entrance", "SO Cave Network Deep", DirectionType.EAST, TransitionType.SCREENS),

    # --- SO Cave Network Deep Exit Region ---
    "SO Cave Network Deep Exit Region East Cave Network Deep Exit":
        Transition( "SO Cave Network Deep Exit Region", "SO Cave Network Deep Exit", DirectionType.EAST, TransitionType.SCREENS),

    # --- SO Poppit ---
    "SO Poppit Burrow South Commons Cliff": Transition( "SO Poppit","SO Commons Cliff", DirectionType.NORTH, TransitionType.BURROW,
                                                        CanBurrow()),

    # --- SO Mining Passage Entrance Exit ---
    "SO Mining Passage Entrance Exit East Fence":
        Transition( "SO Mining Passage Entrance Exit","SO Mining Passage Fence", DirectionType.EAST, TransitionType.SCREENS),

    # --- SO Mining Passage Fence ---
    "SO Mining Passage Fence West Entrance Exit":
        Transition("SO Mining Passage Fence","SO Mining Passage Entrance Exit", DirectionType.WEST, TransitionType.SCREENS),
    "SO Mining Passage Fence East Empty":
        Transition( "SO Mining Passage Fence","SO Mining Passage Empty", DirectionType.EAST, TransitionType.SCREENS,
                    CanBurrow()),

    # --- SO Mining Passage Empty ---
    "SO Mining Passage Empty West Fence":
        Transition( "SO Mining Passage Empty", "SO Mining Passage Fence", DirectionType.WEST, TransitionType.SCREENS),
    "SO Mining Passage Empty North Exit":
        Transition( "SO Mining Passage Empty","SO Mining Passage Exit", DirectionType.NORTH, TransitionType.SCREENS),

    # --- SO Mining Passage Exit ---
    "SO Mining Passage Exit South Empty":
        Transition("SO Mining Passage Exit", "SO Mining Passage Empty", DirectionType.SOUTH, TransitionType.SCREENS),
    "SO Mining Passage Exit Stair North Sandfalls":
        Transition( "SO Mining Passage Exit","Sandfalls Mining Passage Entrance", DirectionType.NORTH, TransitionType.STAIRS),

    "SO Mining Passage Exit West Secret":
        Transition( "SO Mining Passage Exit","SO Mining Passage Secret", DirectionType.WEST, TransitionType.SCREENS),

    # --- SO Mining Passage Secret ---
    "SO Mining Passage Secret East Exit":
        Transition( "SO Mining Passage Secret","SO Mining Passage Exit", DirectionType.EAST, TransitionType.BURROW),

    # --- SO Four Flowers Sandfall ---
    "SO Four Flowers Sandfall Area East Sandfalls":
        Transition("SO Four Flowers Sandfall","Sandfalls Mining Passage Entrance", DirectionType.EAST, TransitionType.AREA_SCREENS),

    # --- SO Four Flowers Shortcut ---
    "SO Four Flowers Shortcut NR Commons Upper":
        Transition( "SO Four Flowers Shortcut","SO Commons Upper", DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE),

    "SO Four Flowers Shortcut NR Commons West Ossex":
        Transition("SO Four Flowers Shortcut", "SO Commons West Ossex", DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE),
}
