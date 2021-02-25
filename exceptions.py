"""end game"""


class GameOver(Exception):
    @classmethod
    def account_counting(cls, name, scores):
        with open('scores.txt', 'a') as file:
            file.write(name + " " + str(scores) + "\n")


class EnemyDown(Exception):
    pass
