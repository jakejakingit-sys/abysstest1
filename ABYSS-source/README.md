# ABYSS

An original graphical side-scrolling adventure for TI-84 Plus CE, written in C for the CEdev v15.0 toolchain. The project includes twenty authored tile maps across four themed worlds, an animated pixel adventurer, platform movement, treasure, hazards, rune puzzles, guardian challenges, a Waystation with upgrades and stats, checksummed AppVar saving, and a final ending.

## Build

Install the official [CEdev v15.0 toolchain](https://github.com/CE-Programming/toolchain/releases/tag/v15.0), add its `bin` directory to `PATH`, and run:

```sh
python3 -m unittest discover -s tests -v
make clean all
```

CEdev creates `bin/ABYSS.8xp` and `bin/ABYSS.map`. The GitHub Actions workflow at `.github/workflows/main.yml` runs those checks, builds the executable, and uploads both outputs.

## Controls

Arrows move and select. `2nd` jumps, `Alpha` activates nearby runes, `Mode` uses the current special ability, `Enter` confirms/interacts, and `Clear` pauses or backs out. Ability unlocks are awarded as campaign progress is made.

## Status

Host-side tests validate the dimensions, distinctness, world placement, spawn, exit, hazards, collectibles and guardian runes of all campaign maps. A local calculator build and emulator or hardware play test have not been performed in this environment; the GitHub workflow provides the verified CEdev build path. Advanced movement, enemy/boss animation variety, sound, and richer world-specific mechanisms can be extended from the current playable foundation.
