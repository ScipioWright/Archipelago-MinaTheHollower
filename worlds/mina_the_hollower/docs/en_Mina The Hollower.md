# Mina The Hollower

If you are reading this, you have either been invited to or are interested in helping alpha test Mina the Hollower Archipelago. This randomizer is still in ALPHA, so please play with the intention of reporting bugs and providing feedback.

- If you are unsure what is causing the issue, create an issue on the [AP World Issue Tracker](https://github.com/FyreDay/Archipelago-MinaTheHollower/issues).
- If you know the problem is with the mod itself, create an issue on the [Mod Issue Tracker](https://github.com/Axertin/mth-apclient/issues)

## Current State

The randomizer is currently believed to be completable. Below is an ever-changing list of implemented features and their current state. Please let us know how your experience goes!

Use [Universal Tracker](https://github.com/FarisTheAncient/Archipelago/releases?q=Tracker) to keep track of what you can access. There is also an in-progress map tracker built into UT that is actively being worked on.
- Game Breaking Bugs:
  - Legovich isn't able to be talked to after defeating Armand 
  - Backer code breaks any save created in AP. Remove backer code for AP.
  - Selling to pawnty is broken and can crash your game
  - some kears give you the vanilla item in addition to the AP item
  - You are forced to teleport to ossex if transitions take you to ropes without you having climb
  - Vitality Vest in Atelier doesnt send checks

- Ability randomization is implemented. Please test all abilities and report any bugs.
- Randomizing Burrow can make starts significantly more difficult. Be careful when enabling it, and please share any ideas for improving the experience.
- Randomizing starting items can cause funny starts. Feedback and suggestions Welcome.
- Kear randomization is implemented. Please report any locks that are not removed correctly or any progression issues you encounter.
- Goaling is implemented but still needs validation.
- Location logic still has many bugs. Please report anything that UT says is inaccessible that you can reach, or anything UT says is accessible that you cannot reach.
- Combat logic has been implemented. When reporting a boss that feels too difficult, please include your attack Bone Ups, defense Bone Ups, health, vials, and currently equipped combat trinkets. [Report Combat Issues Here](https://github.com/FyreDay/Archipelago-MinaTheHollower/issues/12)

### Tracker

The [Universal Tracker](https://github.com/FarisTheAncient/Archipelago/releases?q=Tracker) map tracker is currently complete for Train, Ossex, Loner's Landing, Southern Outskirts, and Eastern Hearth. Please limit map tracker feedback to these areas for now.

We would also appreciate feedback on how the map tracker is organized and whether you find it useful as development continues.

## Install Guide

Find more detailed setup instructions for the mod in the [Mod Readme](https://github.com/Axertin/mth-apclient#installing--running)

- [Latest Mod Release](https://github.com/Axertin/mth-apclient/releases/latest)

- [Latest AP World release](https://github.com/FyreDay/Archipelago-MinaTheHollower/releases/latest)

1. Download the latest version of the mod. it will be a version.dll for windows, or a libmthap.so for linux
2. copy the file into the games install folder in steam apps next to the application
3. If on linux, set a steam launch option ```LD_PRELOAD=libmthap.so %command%```
4. After launch if the login window is not there Press **F2** to toggle it
5. Connect To your AP Slot
6. Load into a NEW save OR a save already playing on the connected slot.

**NEVER CREATE A SAVE AND THEN CONNECT**

**NEVER LOAD INTO A SAVE AND THEN CONNECT**

**NEVER LOAD INTO A VANILLA SAVE YOU DONT WANT MODIFIED**

There is also a console you can access by presssing **F1**. type ```help``` to see commands

## What does randomization do to this game?

All chests, shops, trinkets, and large Bonestones are randomized.

The goal is to defeat Giga Lionel and repair the final generator

## Options

### Start In Ossex
- Skips Loner's Landing. You can still teleport there from the pause menu.

### Kear Rando
- **Vanilla**: Universal Kears are placed in the multiworld. Any Kear Lock opened before receiving every Kear will be **OUT OF LOGIC**
- **AP Items**: Each Kear Lock is removed by a unique AP item.

### Bone Up Caps
- **Per Upgrade**: Attack, defense, and sidearm upgrades are progressively limited separately.
- **All upgrade**: A single progressive cap applies to attack, defense, and sidearm upgrades.

### Randomize Starting Items
- Takes your 15 starting items and shuffles them. This increases difficulty and can cause some funny starts.

### Ability Rando
- Allows you to select which abilities become items from the list below. Burrow is disabled by default because it significantly limits your starting options.

**Burrow** - The ability to burrow. You will still be able to enter Underlabs, go into geysers, and go into pipes.

**Swim** - The ability to swim (burrow in deep water).

**Climb** - The ability to climb ropes.

**Bounce** - The ability to bounce on bounce plants and springboards.

**Spring** - The ability to be launched by springboards.

**Carry** - The ability to carry objects.

### Deathlink
- Sends a DeathLink every time you die.

(Planned change: only sparkless deaths will trigger DeathLink in the future.)