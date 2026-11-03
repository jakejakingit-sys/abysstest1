# Memory report

- Active room map: 44 × 15 characters = 660 bytes.
- All twenty compact maps are stored as read-only program data; only the current map is copied into the active room buffer.
- No game-owned 320 × 240 framebuffer is allocated. GraphX uses the calculator's graphics/video memory.
- Dynamic allocation is not used in the game loop.
- Final code/data/BSS and stack usage require the generated CEdev `bin/ABYSS.map`; it is not measured until a successful toolchain build.
- The CEdev runtime documentation describes roughly 4 KiB stack and a shared 60 KiB BSS/heap region; check actual linker output for the build.
