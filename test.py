from unittest import TestCase
from unittest.mock import patch
from models import Player
import settings


class EnemyTest(TestCase):
    @patch('models.Enemy.select_attack', return_value=1)
    def test_enemy_attack(self, select_attack):
        self.assertEqual(select_attack(), 1)


class PlayerTest(TestCase):
    def setUp(self):
        self.player = Player('name', settings.LIVES, 3, 1)



    def test_fight_player(self):
        self.assertEqual(self.player.fight(1, 1), 0)
        self.assertEqual(self.player.fight(1, 2), 1)
        self.assertEqual(self.player.fight(2, 3), 1)
        self.assertEqual(self.player.fight(3, 1), 1)
        self.assertEqual(self.player.fight(2, 1), -1)
        self.assertEqual(self.player.fight(1, 3), -1)
        self.assertEqual(self.player.fight(3, 2), -1)

    def test_valid_attack(self):
        self.assertTrue(self.player.validation_attack())

    def test_validate_name(self):
        self.assertTrue(self.player.validate_name(self.player.name))








