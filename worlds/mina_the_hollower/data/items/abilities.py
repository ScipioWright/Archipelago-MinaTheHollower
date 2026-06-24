from BaseClasses import ItemClassification
from .. import ItemTypeEnum
from ...constants import ITEMS_OFFSET_ABILITIES


class Abilities(ItemTypeEnum):
    BURROW = ("Burrow",ITEMS_OFFSET_ABILITIES, ItemClassification.progression)
    SWIM = ("Swim", ITEMS_OFFSET_ABILITIES+1, ItemClassification.progression)
    CLIMB = ("Climb", ITEMS_OFFSET_ABILITIES+2, ItemClassification.progression)
    BOUNCE = ("Bounce", ITEMS_OFFSET_ABILITIES+3, ItemClassification.progression)
    SPRING = ("Spring", ITEMS_OFFSET_ABILITIES+4, ItemClassification.progression)
    CARRY = ("Carry", ITEMS_OFFSET_ABILITIES+5, ItemClassification.progression)
