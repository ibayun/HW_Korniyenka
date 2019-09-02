class Fraction:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def fraction(self, chisl, znam, max_number):
        while max_number != 1:
            if chisl % max_number == 0 and znam % max_number == 0:
                chisl = chisl / max_number
                znam = znam / max_number
            max_number -= 1
        return int(chisl), int(znam)

    def __add__(self, other):
        chisl = self.x * other.y + other.x * self.y
        znam = self.y * other.y
        max_number = max(chisl, znam)
        rez = self.fraction(chisl, znam, max_number)
        return "{} / {}".format(rez[0], rez[1])

    def __sub__(self, other):
        chisl = self.x * other.y - other.x * self.y
        znam = self.y * other.y
        max_number = max(chisl, znam)
        rez = self.fraction(chisl, znam, max_number)
        return "{} / {}".format(rez[0], rez[1])

    def __mul__(self, other):
        chisl = self.x * other.x
        znam = self.y * other.y
        max_number = max(self.x, self.y, other.x, other.y)
        rez = self.fraction(chisl, znam, max_number)
        return "{} / {}".format(rez[0], rez[1])

    def __truediv__(self, other):
        chisl = self.x * other.y
        znam = self.y * other.x
        max_number = max(self.x, self.y, other.x, other.y)
        rez = self.fraction(chisl, znam, max_number)
        return "{} / {}".format(rez[0], rez[1])

    def __str__(self):
        chisl = self.x
        znam = self.y
        max_number = max(chisl, znam)
        rez = self.fraction(chisl, znam, max_number)
        return "{} / {}".format(rez[0], rez[1])


if __name__ == "__main__":
    print("operation multiply:", Fraction(864, 832) * Fraction(864, 608))


    print("operation subtract:", Fraction(864, 836) - Fraction(864, 608))

    print("operation divide:", Fraction(864, 836) / Fraction(864, 608))

    fraction1 = Fraction(1, 5)
    print("operation add:", fraction1 + Fraction(4, 5))

    print("answer for result:", Fraction(864, 836))