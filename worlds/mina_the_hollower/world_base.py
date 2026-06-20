from worlds.AutoWorld import World
from .options import MinaTheHollowerOptions



class MinaTheHollowerBase(World):
    options_dataclass = MinaTheHollowerOptions
    options: MinaTheHollowerOptions

    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)