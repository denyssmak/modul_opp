"""game"""
from exceptions import GameOver, EnemyDown
from models import Player, Enemy
import settings

player_list = [0]
"""play_logic"""


def play():
    while True:
        command = input("введите команду /start, /help, /exit, /show scores ")
        if command == "/start":
            levels = 1
            name = input("введите имя: ")
            while True:
                if Player.validate_name(name) is False:
                    print("Имя уже занято!")
                    name = input("введите имя: ")
                else:
                    player = Player(name, settings.LIVES, 3, 0)
                    break
            enemy = Enemy(1, 1)
            while True:
                try:
                    while True:
                        player.allowed_attacks = int(input("введите атаку: "))
                        if player.validation_attack() is False:
                            print("Такого героя нет")
                            continue
                        else:
                            player.attack(enemy)
                            break
                    while True:
                        player.allowed_attacks = int(input("введите защиту: "))
                        if player.validation_attack() is False:
                            print("Такого героя нет")
                            continue
                        else:
                            player.defense(enemy)
                            break
                except EnemyDown:
                    levels += 1
                    player.score += 5
                    enemy = Enemy(1 + levels, 1 + levels)
                    player_list.append(player)

        if command == "/show scores":
            with open("scores.txt", "r") as file:
                print(file.read())
        if command == "/help":
            print(settings.setting)
        if command == "/exit":
            raise KeyboardInterrupt


if __name__ == "__main__":
    try:
        play()
    except GameOver:
        GameOver.account_counting(player_list[-1].name, player_list[-1].score)
    except KeyboardInterrupt:
        pass
    finally:
        print("Good bye!")
