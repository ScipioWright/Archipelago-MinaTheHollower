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

class AbilityRando(Toggle):
    """
    Randomize abilities. You will always start in Ossex
    """
    display_name = "Abilty Rando"

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



