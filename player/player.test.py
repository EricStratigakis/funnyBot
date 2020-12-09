import unittest
from player import Player

class PlayerTest(unittest.TestCase):

    def test_create_player_with(self):
        todd = Player("Todd", )
        self.assertEqual(todd.name, "Todd")
    

if __name__ == "__main__":
    unittest.main()