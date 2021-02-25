"""templates"""
import random
from exceptions import GameOver, EnemyDown



class Enemy:
    def __init__(self, level, lives):
        self.level = level
        self.lives = lives

    @staticmethod
    def select_attack():
        return random.randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown



class Player:
    def __init__(self, name, lives, score, allowed_attacks):
        self.name = name
        self.lives = lives
        self.score = 0
        self.allowed_attacks = allowed_attacks

    @staticmethod
    def fight(attack, defense):
        if attack == defense:
            return 0
        elif attack == 1 and defense == 2:
            return 1
        elif attack == 2 and defense == 3:
            return 1
        elif attack == 3 and defense == 1:
            return 1
        else:
            return -1

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver

    def attack(self, enemy_obj):
        self.fight(self.allowed_attacks, enemy_obj.select_attack())
        if self.fight(self.allowed_attacks, enemy_obj.select_attack()) == 0:
            print("It's a draw!")
        elif self.fight(self.allowed_attacks, enemy_obj.select_attack()) == 1:
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
        elif self.fight(self.allowed_attacks, enemy_obj.select_attack()) == -1:
            print("You missed!")

    def defense(self, enemy_obj):
        self.fight(enemy_obj.select_attack(), self.allowed_attacks)
        if self.fight(enemy_obj.select_attack(), self.allowed_attacks) == 0:
            print("It's a draw!")
        elif self.fight(enemy_obj.select_attack(), self.allowed_attacks) == 1:
            print("You missed!")
            self.decrease_lives()
        elif self.fight(enemy_obj.select_attack(),self.allowed_attacks) == -1:
            print("You attacked successfully!")
            self.score += 1

    def validation_attack(self):
        return self.allowed_attacks in [1,2,3]


    @classmethod
    def validate_name(cls, name):
        with open("scores.txt", "r") as file:
            for i in file.readlines():
                if name in i.split()[0]:
                    return False
        return True


