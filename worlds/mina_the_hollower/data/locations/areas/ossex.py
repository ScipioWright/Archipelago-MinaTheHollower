from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from .. import LocationData
from ... import RegionConnection, Transition
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanJumpTiles, CanBounce, HasVialsCount

regions: set[str] = {
    "Ossex City Center"
    "Ossex City Center"
}

transitions: dict[str, Transition] = {

}

collectable_locations: dict[str, LocationData] = {
    "OS Couple's Quarter Chest" : LocationData(146, "Ossex Couple's Quarter"),
    "OS Couple's Quarter Thermal Pack" : LocationData(147, "Ossex Couple's Quarter"),
    "Trinket_PocketTrebuchet" : LocationData(148, "Ossex"),
    "Ticket_Pass" : LocationData(149, "Ossex"),
    "OS Kear Institute Kear Completion" : LocationData(150, "Ossex"),
    # "Lock" : LocationData(151, "Ossex"),
    # "Lock" : LocationData(152, "Ossex"),
    "OS Music Hall Chest" : LocationData(153, "Ossex"),
    "Trinket_PlasmaSaver" : LocationData(154, "Ossex"),
    "OS Ossex Telescope Kear" : LocationData(155, "Ossex "),
    "OS Trinket Bazaar Kear" : LocationData(156,"Ossex Trinket Bazaar"),
    # "Lock" : LocationData(157, "Ossex"),
    "Trinket_BoneSaver" : LocationData(158, "Ossex"),
    "OS Bowery Upper Chest" : LocationData(159, "Ossex"),
    "OS City Center 2nd Race Kear" : LocationData(160, "Ossex", CanJumpOneTile() & CanBurrow()),
    "OS Courtyard East Deboning Wand" : LocationData(161, "Ossex"),
    "OS City Center Steady Soles": LocationData(162, "Ossex",
                                                Has("Steady Soles Kear") & CanJumpOneTile() & CanBurrow()),

    "Whip_Level_2" : LocationData(163, "Ossex"),
    "OS Gutterways Bonestone" : LocationData(164, "Ossex"),
    "OS High Street Sewer Chest" : LocationData(165, "Ossex"),
    "OS Strategy Center Chest" : LocationData(166, "Ossex"),
    "OS Strategy Center Ophidio Bonestone" : LocationData(167, "Ossex"),
"OS Hollower's Guild Back Room Kear Chest" : LocationData(168, "Guild Back Room", CanBurrow()),
    "OS Attic Chest" : LocationData(169, "Ossex"),
    "OS Atelier Chest" : LocationData(170, "Ossex"),
    "OS High Street Valor Medallion" : LocationData(171, "Ossex"),
    "OS Bowery Residence Bonestone" : LocationData(173, "Ossex"),
    "OS Legovich's Arms Whip" : LocationData(174, "Ossex Legovich's Arms"),
    "OS Legovich's Arms Hammer" : LocationData(175, "Ossex Legovich's Arms"),
    "OS Legovich's Arms Daggers" : LocationData(176, "Ossex Legovich's Arms"),
    "OS Legovich's Arms Battery Buster" : LocationData(177, "Ossex Legovich's Arms"),
    "OS Legovich's Arms Guardian Casket" : LocationData(178, "Ossex Legovich's Arms"),
    "Trinket_PlasmaFunnel" : LocationData(179, "Ossex Trinket Bazaar"),
    "Trinket_BurrowPulse" : LocationData(180, "Ossex Trinket Bazaar"),
    "Trinket_BriskBrew" : LocationData(181, "Ossex Trinket Bazaar"),
    "Trinket_AutoVial" : LocationData(182, "Ossex Trinket Bazaar"),
    "Trinket_ShockFlint" : LocationData(183, "Ossex Trinket Bazaar"),
    "Trinket_Shield" : LocationData(184, "Ossex Trinket Bazaar"),
    "Trinket_VialParry" : LocationData(185, "Ossex Trinket Bazaar"),
    "OS Emporium Health Rose #1" : LocationData(186, "Ossex Emporium"),
    "OS Emporium Health Rose #2" : LocationData(187, "Ossex Emporium"),
    "OS Emporium Health Rose #3" : LocationData(188, "Ossex Emporium"),
    "OS Emporium Vial Pouch #1" : LocationData(189, "Ossex Emporium"),
    "OS Emporium Vial Pouch #2" : LocationData(190, "Ossex Emporium"),
    "OS Emporium Vial Pouch #3" : LocationData(191, "Ossex Emporium"),
    "OS Emporium Spark Container" : LocationData(192, "Ossex Emporium"),
    "OS Emporium Joule Box #1" : LocationData(193, "Ossex Emporium"),
    "OS Emporium Joule Box #2" : LocationData(194, "Ossex Emporium"),
    "OS Emporium Joule Box #3" : LocationData(195, "Ossex Emporium"),
    "OS Emporium Trinket Bag #1" : LocationData(196, "Ossex Emporium"),
    "OS Emporium Trinket Bag #2" : LocationData(197, "Ossex Emporium"),
    "OS Emporium Trinket Bag #3" : LocationData(198, "Ossex Emporium"),
    "OS Kear Institute Kear #1" : LocationData(199, "Ossex Kear Institute"),
    "OS Kear Institute Kear #2" : LocationData(200, "Ossex Kear Institute"),
    "OS Kear Institute Kear #3" : LocationData(201, "Ossex Kear Institute"),
    "OS Kear Institute Kear #4" : LocationData(202, "Ossex Kear Institute"),
    "OS Kear Institute Kear #5" : LocationData(203, "Ossex Kear Institute"),
    "OS Kear Institute Kear #6" : LocationData(204, "Ossex Kear Institute"),
    "OS Kear Institute Kear #7" : LocationData(205, "Ossex Kear Institute"),
    "OS Kear Institute Kear #8" : LocationData(206, "Ossex Kear Institute"),
    "OS Kear Institute Kear #9" : LocationData(207, "Ossex Kear Institute"),
    "ArmorUpgrade_Health" : LocationData(208, "Ossex Atelier", HasVialsCount(count=1) & Has("Ossex Guild Kear")),
    "ArmorUpgrade_Custom" : LocationData(209, "Ossex Atelier", HasVialsCount(count=1) & Has("Ossex Guild Kear")),
    "Upgrade_JouleAlembic" : LocationData(210, "Ossex Guild Back Room", HasVialsCount(count=1) & Has("Ossex Guild Kear")),
    "Upgrade_WorldMap" : LocationData(211, "Ossex Guild Back Room", HasVialsCount(count=1) & Has("Ossex Guild Kear")),
    "Upgrade_EnhancedMap" : LocationData(212, "Ossex Guild Back Room", HasVialsCount(count=1) & Has("Ossex Guild Kear")),
    "Upgrade_RadarMap" : LocationData(213, "Ossex Guild Back Room", HasVialsCount(count=1) & Has("Ossex Guild Kear")),
    "Upgrade_SidearmKeeper" : LocationData(214, "Ossex Guild Back Room", HasVialsCount(count=1) & Has("Ossex Guild Kear")),
    "Upgrade_SidearmSaver" : LocationData(215, "Ossex Guild Back Room", HasVialsCount(count=1) & Has("Ossex Guild Kear")),
    "Upgrade_Phonograph" : LocationData(216, "Ossex Guild Back Room", HasVialsCount(count=1) & Has("Ossex Guild Kear")),
    "Upgrade_CandleVision" : LocationData(217, "Ossex Guild Back Room", HasVialsCount(count=1) & Has("Ossex Guild Kear")),
    "Upgrade_TrainingDummy" : LocationData(218, "Ossex Guild Back Room", HasVialsCount(count=1) & Has("Ossex Guild Kear")),
    "Upgrade_TwoSidearmsHUD" : LocationData(219, "Ossex"),
    "OS City Center Triple Flagellum" : LocationData(220, "Ossex", Has("Fishing Rod")),
}

connections: dict[str, RegionConnection] = {

    "Ossex_Southern Outskirts" : RegionConnection("Ossex", "Southern Outskirts"),
    "Ossex_Western Wilds Occupied Bridge" : RegionConnection("Ossex", "Western Wilds Occupied Bridge"),
    "Ossex_Western Wilds Occupied Bridge" : RegionConnection("Ossex", "Western Wilds Occupied Bridge"),

    "Ossex_Ossex Guild Back Room" : RegionConnection("Ossex", "Ossex Guild Back Room", CanBurrow() & CanJumpOneTile()),
    "Ossex Guild Back Room_Ossex" : RegionConnection("Ossex Guild Back Room","Ossex", CanBurrow() & CanJumpOneTile()),
    "Ossex_Ossex Kear Institute" : RegionConnection("Ossex", "Ossex Kear Institute"),
    "Ossex Kear Institute_Ossex" : RegionConnection("Ossex Kear Institute", "Ossex"),
    "Ossex Emporium_Ossex" : RegionConnection("Ossex Emporium", "Ossex"),
    "Ossex_Ossex Emporium" : RegionConnection("Ossex", "Ossex Emporium"),
    "Ossex_Ossex Legovich's Arms" : RegionConnection("Ossex", "Ossex Legovich's Arms"),
    "Ossex Legovich's Arms_Ossex" : RegionConnection("Ossex Legovich's Arms","Ossex"),
    "Ossex_Ossex Trinket Bazaar" : RegionConnection("Ossex", "Ossex Trinket Bazaar", CanBurrow() & CanJumpOneTile()),
    "Ossex Trinket Bazaar_Ossex" : RegionConnection("Ossex Trinket Bazaar", "Ossex", CanBurrow() & CanJumpOneTile()),
    "Ossex_Ossex Couple's Quarter" : RegionConnection("Ossex", "Ossex Couple's Quarter", CanBurrow() & CanJumpOneTile()),
    "Ossex Couple's Quarter_Ossex" : RegionConnection("Ossex Couple's Quarter","Ossex", CanBurrow() & CanJumpOneTile()),
}

