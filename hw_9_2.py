# Task 1

"""
Contains classes for our future MMORPG.
"""

from logging import Logger

class Character:
    """
    Represents a character in an MMORPG game.

    Attributes:
        name (str): The name of the character.
        hit_point (int): The character's health points.
        damage (int): The character's attack power.
        logger (Logger): Logger instance to track actions.

    """

    def __init__(self, name: str, hp: int, dmg: int, logger: Logger):
        self.name = name
        self.hit_point = hp
        self.damage = dmg
        self.logger = logger

    def is_alive(self) -> bool:
        alive = self.hit_point > 0
        if not alive:
            self.logger.info(f'{self.name} is Defeated')
        return alive

    def attack(self, enemy: "Character") -> None:

        if not enemy:
            raise ValueError("Missing enemy Character")
        
        enemy.hit_point -= self.damage
        self.logger.info(f"{self.name} attacked {enemy.name}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()


# Task 2


import unittest
from logging import getLogger, NullHandler
from src.character import Character

class TestCharacter(unittest.TestCase):
    """Unit tests for the Character class."""

    def setUp(self):
        self.logger = getLogger(__name__)
        self.logger.addHandler(NullHandler())
        self.hero = Character("Hero", 50, 10, self.logger)
        self.villain = Character("Villain", 30, 5, self.logger)

    def test_initial_health(self):
        self.assertEqual(self.hero.hit_point, 50)

    def test_is_alive(self):
        """Test if a character is correctly identified as alive or dead."""
        self.assertTrue(self.hero.is_alive())

        dead_char = Character("Ghost", 0, 10, self.logger)
        self.assertFalse(dead_char.is_alive())

    def test_attack(self):
        """Test if attack reduces enemy health correctly."""
        self.hero.attack(self.villain)
        self.assertEqual(self.villain.hit_point, 20)

    def test_attack_kills_enemy(self):
        """Test if attacking an enemy reduces health to zero or below."""
        hero = Character("Hero", 50, 30, self.logger)
        hero.attack(self.villain)
        self.assertFalse(self.villain.is_alive())

    def test_negative_health(self):
        """Test if a character with negative health is considered dead."""
        zombie = Character("Zombie", -10, 10, self.logger)
        self.assertFalse(zombie.is_alive())

    def test_attack_without_enemy(self):
        """Test if attacking without an enemy raises an error."""
        with self.assertRaises(ValueError):
            self.hero.attack(None)

if __name__ == "__main__":
    unittest.main()
