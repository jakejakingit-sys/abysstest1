"""Campaign data and CEdev source checks; run with unittest discovery."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
NAMES = [
    "The Entrance", "Forgotten Halls", "Burial Grounds", "Bone Chambers", "Bone King's Throne",
    "Mine Entrance", "Crystal Caverns", "Collapsing Tunnels", "Deep Shafts", "Broodmother's Nest",
    "Ashen Path", "Burning Halls", "Magma Bridge", "Furnace Chambers", "Inferno's Arena",
    "Forgotten Gate", "Shattered Reality", "Lost Kingdom", "Abyssal Core", "The Forgotten One",
]


class CampaignTests(unittest.TestCase):
    def test_all_campaign_maps(self):
        maps = []
        for world in range(1, 5):
            for n in range((world - 1) * 5 + 1, world * 5 + 1):
                path = ROOT / "levels" / f"world{world}" / f"level{n:02}.map"
                rows = path.read_text(encoding="ascii").splitlines()
                self.assertEqual(len(rows), 15, path)
                self.assertTrue(all(len(row) == 44 for row in rows), path)
                self.assertEqual(sum(row.count("S") for row in rows), 1, path)
                self.assertEqual(sum(row.count("d") for row in rows), 1, path)
                self.assertTrue(any(c in "ck" for c in "".join(rows)), path)
                self.assertTrue(any(c == "^" for c in "".join(rows)), path)
                self.assertTrue(all(set(row) <= set(".#=^crkdS") for row in rows), path)
                self.assertEqual(rows[12][1], "S", path)
                self.assertIn(rows[13][1], "#=", path)
                if n % 5 == 0:
                    self.assertGreaterEqual("".join(rows).count("r"), 3, path)
                maps.append(tuple(rows))
        self.assertEqual(len(set(maps)), 20)

    def test_ce_entrypoint_and_graphics(self):
        source = (ROOT / "src" / "main.c").read_text(encoding="utf-8")
        self.assertIn("int main(void)", source)
        self.assertIn("gfx_Begin", source)
        self.assertIn("kb_Scan", source)


if __name__ == "__main__":
    unittest.main()
