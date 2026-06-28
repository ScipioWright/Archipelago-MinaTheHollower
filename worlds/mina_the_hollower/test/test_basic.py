from BaseClasses import ItemClassification
from collections import Counter

from .. import options, MinaTheHollowerWorld
from .bases import MinaTestBase


class TestBasic(MinaTestBase):
    options = {}
    world: MinaTheHollowerWorld

    def test_can_beat_game(self):
        self.collect_all_but([])
        self.assertBeatable(True)
