from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from ... import RegionConnection, Transition, LocationData
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanBounce, CanJumpTiles, CanClimb, CanCarry


collectable_locations: dict[str, LocationData] = {
    "SF Hobo Holdout Puffer Beak" : LocationData(82, "Sandfalls Mining Outlook"), #needs fishing rod,
    "SF Sifted Sands Snake Bomb Chest" : LocationData(326, "Sandfalls Sifted Sands"), #needs burrow, carry,
    "SF Sifted Sands Kear" : LocationData(319, "Sandfalls Sifted Sands"), #needs completesandfallsgenerator,
    "SF Guiding Grains Niter Belt" : LocationData(330, "Sandfalls Pachinko"),
    "SF Guiding Grains Bonestone Left" : LocationData(329, "Sandfalls Pachinko"),
    "SF Guiding Grains Bonestone Right" : LocationData(328, "Sandfalls Pachinko"),
    "SF Hidden Cave Vial Pouch" : LocationData(323, "Sandfalls Sifted Sands Hidden Cave"), #needs burrow, kear,
    "SF Ring Dive Parlor Tunneler's Codex" : LocationData(317, "Sandfalls Ring Dive Parlor"), #needs burrow,
    "SF Shifty Seclusion Chest" : LocationData(327, "Sandfalls Shifty Seclusion"),
    "SF Payload Passage Chest" : LocationData(332, "Sandfalls Payload Passage Chest"), #needs burrow, carry,
    "SF Bone Junction Chest" : LocationData(356, "Sandfalls Bone Junction"), #needs burrow, carry,
    "SF Train Vita's Shop" : LocationData(333, "Sandfalls Sandy Station"), #needs burrow,
    "BB Sandwater Junction Angler's Raft" : LocationData(325, "Sandfalls Sandwater Junction"), #needs 2 tiles of air movement or swim,
}

boss_locations: dict[str, LocationData] = {
    "SF Miner's Den Major Miner": LocationData(None, "Sandfalls Miners Den"),
    # needs 3 vials && burrow && (spike spurs || carry/throw),
    "SF Shoreline Generator Activated": LocationData(None, "Bone Beach Shoreline Generator"),  # needs burrow,
}

