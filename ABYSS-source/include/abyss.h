#ifndef ABYSS_H
#define ABYSS_H
#include <stdint.h>
#define LEVEL_COUNT 20
#define MAP_W 44
#define MAP_H 15
#define TILE 16
typedef struct { const char *name; uint8_t world; const char *rows[MAP_H]; } LevelDef;
extern const LevelDef abyss_levels[LEVEL_COUNT];
#endif
