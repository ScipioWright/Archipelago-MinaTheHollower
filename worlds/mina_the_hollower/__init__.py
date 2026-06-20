import json
from typing import ClassVar, Dict, Any, Optional

from BaseClasses import ItemClassification, Tutorial, Location
from Options import OptionError
from Utils import visualize_regions
from entrance_rando import randomize_entrances, bake_target_group_lookup
from rule_builder.rules import Has
from pathlib import Path
from . import locations, items, tracker
from .constants import MINA_THE_HOLLOWER
from .data import get_target_groups
from .items import MinaTheHollowerItem
from .data.items import all_filler_items, all_items
from .data.locations import all_locations
from .options import mina_the_hollower_option_groups

from .world_base import MinaTheHollowerBase

from ..AutoWorld import WebWorld


class MinaTheHollowerWeb(WebWorld):
    theme = "partyTime"
    setup_en = Tutorial(
        tutorial_name="Multiworld Setup Guide",
        description="A guide to setting up the Mina The Hollower randomizer connected to an Archipelago Multiworld.",
        language="English",
        file_name="setup_en.md",
        link="setup/en",
        authors=["FyreDay"]
    )
    option_groups = mina_the_hollower_option_groups
    tutorials = [setup_en]


def load_manifest():
    manifest_path = Path(__file__).parent / "archipelago.json"

    with manifest_path.open("r", encoding="utf-8") as f:
        return json.load(f)



class MinaTheHollowerWorld(MinaTheHollowerBase):

    manifest = load_manifest()

    game = MINA_THE_HOLLOWER
    web = MinaTheHollowerWeb()


    item_name_to_id: ClassVar[Dict[str, int]] = {item_name: item_data.item_id for item_name, item_data in
                                                 all_items.items()}
    location_name_to_id: ClassVar[Dict[str, int]] = {loc_name: loc_data.location_id for loc_name, loc_data in all_locations.items()}

    ut_can_gen_without_yaml = True

    tracker_world: ClassVar = {
        "map_page_folder": "tracker",
        "map_page_maps": "maps/maps.json",
        "map_page_locations": {
            "locations/eastern_hearth.json",
            "locations/ossex.json",
        },
        "map_page_index": tracker.map_page_index,
        "map_page_setting_key": "mina_the_hollower_map_{team}_{player}",
    }



    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        return slot_data

    def __init__(self, multiworld, player):
        self.regions = {}
        self.itempool = []
        self.entrance_rando = False
        self.hints = {}

        super().__init__(multiworld, player)

    def generate_early(self) -> None:
        print(self.options.excluded_areas.value)
        print(self.options.excluded_areas.value[0])
        raise OptionError("test")
        self.handle_ut_yamless(None)

    def create_regions(self):
        self.regions = locations.get_regions(self)
        locations.create_regions(self, self.regions)
        items.create_events(self)
        locations.create_entrances(self, self.regions)

    def connect_entrances(self) -> None:
        if self.entrance_rando:
            target_group_lookup = bake_target_group_lookup(self, get_target_groups)
            randomize_entrances(self, False, target_group_lookup)

    def create_item(self, item: str) -> MinaTheHollowerItem:
        if item in all_filler_items.keys():
            return MinaTheHollowerItem(item, ItemClassification.filler, self.item_name_to_id[item], self.player)
        return MinaTheHollowerItem(item, ItemClassification.progression, self.item_name_to_id[item], self.player)

    def create_items(self):
        starting_items = items.create_items(self)
        for item in starting_items:
            self.push_precollected(item)

    def set_rules(self):
        self.set_completion_rule(Has("TrainPass"))

    def generate_output(self, output_directory: str):
        print("Generating Output")
        visualize_regions(self.multiworld.get_region("Menu", self.player), f"Player{self.player}_output.puml",
                          show_entrance_names=True,
                          regions_to_highlight=self.multiworld.get_all_state(self.player).reachable_regions[
                              self.player])

    def fill_slot_data(self) -> id:
        #print("Filling Slot Data")
        return {
            "sem_ver": self.manifest["mod_version"],
            "goal" : self.options.goal.value,
            "essex_start": self.options.essex_start.value,
            "kear_rando": self.options.kear_rando.value,
            # "entrance_rando" : self.options.entrance_rando.value,
            "death_link" : self.options.death_link.value,

        }

    def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]]):
        hint_data[self.player] = self.hints


    def handle_ut_yamless(self, slot_data: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:

        if not slot_data \
                and hasattr(self.multiworld, "re_gen_passthrough") \
                and isinstance(self.multiworld.re_gen_passthrough, dict) \
                and self.game in self.multiworld.re_gen_passthrough:
            slot_data = self.multiworld.re_gen_passthrough[self.game]

        if not slot_data:
            return None

        self.options.goal.value = slot_data["goal"]
        self.options.death_link.value = slot_data["death_link"]
        self.options.kear_rando.value = slot_data["kear_rando"]
        self.options.essex_start.value = slot_data["essex_start"]
        # self.options.entrance_rando.value = slot_data["entrance_rando"]
        # self.options.shuffled_sidearms.value = slot_data["shuffled_sidearms"]
        # self.options.shuffle_enemy_level.value = slot_data["shuffle_enemy_level"]
        # self.options.shuffled_items.value = slot_data["shuffled_items"]

        return slot_data