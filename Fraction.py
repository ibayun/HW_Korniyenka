class Fraction:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def fraction(nominator, denominator, max_number):
        while max_number != 1:
            if nominator % max_number == 0 and denominator % max_number == 0:
                nominator = nominator / max_number
                denominator = denominator / max_number
            max_number -= 1
        return int(nominator), int(denominator)

    def __add__(self, other):
        nominator = self.x * other.y + other.x * self.y
        denominator = self.y * other.y
        nominator, denominator = self.fraction(
            nominator, denominator, max(nominator, denominator)
        )
        return "{} / {}".format(nominator, denominator)

    def __sub__(self, other):
        nominator = self.x * other.y - other.x * self.y
        denominator = self.y * other.y
        nominator, denominator = self.fraction(
            nominator, denominator, max(nominator, denominator)
        )
        return "{} / {}".format(nominator, denominator)

    def __mul__(self, other):
        nominator = self.x * other.x
        denominator = self.y * other.y
        nominator, denominator = self.fraction(
            nominator, denominator, max(nominator, denominator)
        )
        return "{} / {}".format(nominator, denominator)

    def __truediv__(self, other):
        nominator = self.x * other.y
        denominator = self.y * other.x
        nominator, denominator = self.fraction(
            nominator, denominator, max(self.x, self.y, other.x, other.y)
        )
        return "{} / {}".format(nominator, denominator)

    def __str__(self):
        nominator = self.x
        denominator = self.y
        nominator, denominator = self.fraction(
            nominator, denominator, max(nominator, denominator)
        )
        return "{} / {}".format(nominator, denominator)


if __name__ == "__main__":
    print("operation multiply:", Fraction(864, 832) * Fraction(864, 608))
    print("operation subtract:", Fraction(864, 836) - Fraction(864, 608))
    print("operation divide:", Fraction(864, 836) / Fraction(864, 608))
    fraction1 = Fraction(1, 5)
    print("operation add:", fraction1 + Fraction(4, 5))
    print("answer for result:", Fraction(864, 836))
