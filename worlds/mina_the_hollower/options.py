from dataclasses import dataclass

from Options import DeathLink, DefaultOnToggle, Toggle, OptionSet, OptionDict, Choice, OptionGroup, \
    PerGameCommonOptions, Range


class Goal(Choice):
    """
    Goal
    """
    display_name = "Goal"
    option_radientManorGenerator = 0
    default = 0

class BoneUpCap(Choice):
    """
    How do you want your Bone Up Cap Items. A progressive each for attack, defense and Sidearms OR One progressive item for all
    """
    display_name = "Goal"
    option_perUpgrade = 0
    option_allUpgrade = 1
    default = 0

class NumberOfGenerators(Range):
    """
    The number of generators required to go to radiant manor
    """
    display_name = "Generators Required"
    range_start = 1
    range_end = 6
    default = 6

class OssexStart(DefaultOnToggle):
    """
    Start In Ossex
    """
    display_name = "Ossex Start"

class RandomizeStartingItems(Toggle):
    """
    Take all starting health, spark, vials, Magic and randomize them
    """
    display_name = "Randomize Starting Items"

class AbilityRando(OptionSet):
    """
    Randomize abilities (You will not be able to perform the listed actions until sent them as items). You will always start in Ossex.

    Valid Options:
    - **Burrow** - The ability to burrow. You will still be able to enter Underlabs.
    - **Swim** - The ability to swim (burrow in deep water).
    - **Climb** - The ability to climb ropes.
    - **Bounce** - The ability to bounce on bounce plants and springboards.
    - **Carry** - The ability to carry objects.
    """
    display_name = "Abilty Rando"
    default = ["Burrow", "Swim", "Climb", "Bounce", "Carry"]
    valid_keys = ["Burrow", "Swim", "Climb", "Bounce", "Carry"]


ABILITY_RANDO_SLOT_KEYS = {
    "Burrow": ["burrow_rando"],
    "Swim": ["swim_rando"],
    "Climb": ["rope_rando"],
    "Bounce": ["puff_rando", "spring_rando"],
    "Carry": ["carry_rando"],
}

class RandomizeEntrances(OptionSet):
    """
    Currently there are no valid keys. Only give this []

    - **Doors** - Randomizes All Doors between eachother
    - **Stairs** - Randomizes All Stairs between eachother
    - **Area Transitions** - Randomizes All Screen transitions that change areas
    - **Screen Transitions** - Randomizes All Screen transitions
    """
    display_name = "Entrance Randomization"
    valid_keys = []

    # valid_keys = ["Doors", "Stairs", "Area Transitions", "Screen Transitions"]

class ExcludedAreas(OptionSet):
    """
    NOT IMPLEMENTED WILL NOT BE USED
    Each Region you add to this list will not have any location in them have any items. That generator will be marked complete

    Example value: ["Astral Orrery", "Queensbury Crypt"]

    Valid Area Names. Copy "NAME" into the brackets [] below. Seperate all names by Commas ,
    - **"Queensbury Crypt"** -
    - **"Nox's Bayou"** -
    - **"Bone Beach"** -
    - **"Queensbury Crypt"** -
    - **"Coltrane Peak"** -
    - **"Astral Orrery"** -
    """
    display_name = "Excluded Areas"
    default = []
    valid_keys = ["Astral Orrery", "Queensbury Crypt", "Coltrane Peak", "Septemburg", "Bone Beach", "Nox's Bayou"]

class KearRandomization(Choice):
    """
    Vanilla: Universal Kears are in the multiworld. Every Kear Lock you open before receiving every single Kear will be OUT OF LOGIC
    AP Items: Each Kear Lock is removed by a unique AP item
    Area AP Items: All Kear Locks in an area are removed by a single AP Item
    """
    option_vanilla = 0
    option_apItems = 1
    option_areaApItems = 2
    default = 1

class ShuffledSidearms(Toggle):
    """
    Sidearms are shuffled so each type always becomes the same other type
    """
    display_name = "Shuffled Sidearms"



mina_the_hollower_option_groups= [
    OptionGroup("AP Options", [
        Goal,
        BoneUpCap,
        OssexStart,
        KearRandomization,
        ExcludedAreas,
        RandomizeStartingItems,
        # RandomizeEntrances,
        AbilityRando,
        DeathLink,
    ]),
]

@dataclass
class MinaTheHollowerOptions(PerGameCommonOptions):
    goal: Goal
    ossex_start: OssexStart
    kear_rando: KearRandomization
    excluded_areas : ExcludedAreas
    bone_up_cap: BoneUpCap
    random_starting_items: RandomizeStartingItems
    # entrance_rando: RandomizeEntrances
    ability_rando: AbilityRando
    death_link: DeathLink
    # shuffled_sidearms: ShuffledSidearms
    # shuffle_enemy_level: ShuffleEnemyLevel
