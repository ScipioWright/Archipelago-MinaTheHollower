from BaseClasses import ItemClassification
from .. import ItemData

BoneStone: dict[str, ItemData] = {
    "BoneDust" : ItemData(50, ItemClassification.filler),
    "Bonestone" : ItemData(51, ItemClassification.filler),
    "Bonestone01" : ItemData(52, ItemClassification.filler),
    "Bonestone02" : ItemData(53, ItemClassification.filler),
    "Bonestone03" : ItemData(54, ItemClassification.filler),
    "Bonestone04" : ItemData(55, ItemClassification.filler),
    "Bonestone05" : ItemData(56, ItemClassification.filler),
    "Bonestone06" : ItemData(57, ItemClassification.filler),
    "Bonestone07" : ItemData(58, ItemClassification.filler),
    "Bonestone08" : ItemData(59, ItemClassification.filler),
    "Bonestone09" : ItemData(60, ItemClassification.filler),
    "Bonestone10" : ItemData(61, ItemClassification.filler),
}

junk: dict[str, ItemData] = {
    "HealingVial" : ItemData(17, ItemClassification.progression),
    "HealingVialPickup" : ItemData(19, ItemClassification.progression),
    "HealingVialPackPickup" : ItemData(20, ItemClassification.progression),

    "HealthRecovery" : ItemData(35, ItemClassification.progression),
    "FishHealthRecovery" : ItemData(36, ItemClassification.progression),
    "MagicSmall" : ItemData(37, ItemClassification.progression),
    "MagicMedium" : ItemData(38, ItemClassification.progression),
    "MagicLarge" : ItemData(39, ItemClassification.progression),
    "TreasureSmallest" : ItemData(40, ItemClassification.progression),
    "TreasureSmall" : ItemData(41, ItemClassification.progression),
    "TreasureMedium" : ItemData(42, ItemClassification.progression),
    "TreasureLarge" : ItemData(43, ItemClassification.progression),
    "TreasureLargest" : ItemData(44, ItemClassification.progression),
    "TreasureBoss" : ItemData(45, ItemClassification.progression),
    "TreasureGoldLarge" : ItemData(46, ItemClassification.progression),
    "TreasureGoldLargest" : ItemData(47, ItemClassification.progression),
    "TreasureJewelLarge" : ItemData(48, ItemClassification.progression),
    "TreasureJewelLargest" : ItemData(49, ItemClassification.progression),
    # "BonestoneTower" : ItemData(62, ItemClassification.progression),
}
