import math


class Warrior:
    RANGES = [
        'Pushover', 'Novice', 'Fighter', 'Warrior',
        'Veteran', 'Sage', 'Elite', 'Conqueror',
        'Champion', 'Master', 'Greatest'
    ]
    warrior_achievement = []

    def __init__(self, experience):
        self.experience = 10000 if experience > 10000 else experience

    def level(self):
        level_warrior = int(math.floor(self.experience / 100))
        return level_warrior

    def get_rank(self, level):
        rank = self.RANGES[int(level/1000)]
        return rank

    def rank(self):
        rank_warrior = self.get_rank(self.level())
        return "Hey, amigo. Your rank - {}".format(rank_warrior)

    def achievements(self):
        return self.warrior_achievement
        pass

    def training(self, training):
        if int(training[2]) <= self.level():
            self.experience += int(training[1])
            self.warrior_achievement = training[0]
            return training[0]
        return "Not strong enough"

    @staticmethod
    def commentator(level_warrior, level_ai):
        if level_warrior >= level_ai + 2:
            return "Easy fight"
        elif level_warrior >= level_ai + 1:
            return "A good fight"
        else:
            return "An intense fight"

    def battle(self, level_ai):
        rank_ai = self.get_rank(int(level_ai))
        if rank_ai == self.rank():
            print(self.commentator(self.level(), level_ai))
            if self.level() == level_ai:
                self.experience += 10
            elif self.level() <= level_ai:
                self.experience += 20 * ((level_ai - self.level())**2)
            elif self.level() == level_ai + 1:
                self.experience += 5
            else:
                self.experience += 0
        else:
            if self.level() <= level_ai + 5:
                return "You've been defeated"
            else:
                return "You win, but you don\'t have experience"


if __name__ == "__main__":
    bruce_lee = Warrior(122)
    print("Your level - {}".format(bruce_lee.level()))
    print("your experience - ", bruce_lee.experience)
    print(bruce_lee.rank())
    print(bruce_lee.achievements())
    print(bruce_lee.training(["Defeated Chuck Norris", 90, 1]))
    print("your experience - ", bruce_lee.experience)
    print(bruce_lee.achievements())
    print(bruce_lee.training(["Jan-Jan", 90, 4]))
    print(bruce_lee.achievements())
    print(bruce_lee.rank())
    print("your experience - ", bruce_lee.experience)
