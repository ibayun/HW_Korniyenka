class Fraction:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def fraction(self, numerator, denumerator, max_number):
        while max_number != 1:
            if numerator % max_number == 0 and denumerator % max_number == 0:
                numerator = numerator / max_number
                denumerator = denumerator / max_number
            max_number -= 1
        return int(numerator), int(denumerator)

    def __add__(self, other):
        numerator = self.x * other.y + other.x * self.y
        denumerator = self.y * other.y
        max_number = max(numerator, denumerator)
        rez = self.fraction(numerator, denumerator, max_number)
        return "{} / {}".format(rez[0], rez[1])

    def __sub__(self, other):
        numerator = self.x * other.y - other.x * self.y
        denumerator = self.y * other.y
        max_number = max(numerator, denumerator)
        rez = self.fraction(numerator, denumerator, max_number)
        return "{} / {}".format(rez[0], rez[1])

    def __mul__(self, other):
        numerator = self.x * other.x
        denumerator = self.y * other.y
        max_number = max(self.x, self.y, other.x, other.y)
        rez = self.fraction(numerator, denumerator, max_number)
        return "{} / {}".format(rez[0], rez[1])

    def __truediv__(self, other):
        numerator = self.x * other.y
        denumerator = self.y * other.x
        max_number = max(self.x, self.y, other.x, other.y)
        rez = self.fraction(numerator, denumerator, max_number)
        return "{} / {}".format(rez[0], rez[1])

    def __str__(self):
        numerator = self.x
        denumerator = self.y
        max_number = max(numerator, denumerator)
        rez = self.fraction(numerator, denumerator, max_number)
        return "{} / {}".format(rez[0], rez[1])


if __name__ == "__main__":
    print("operation multiply:", Fraction(864, 832) * Fraction(864, 608))


    print("operation subtract:", Fraction(864, 836) - Fraction(864, 608))

    print("operation divide:", Fraction(864, 836) / Fraction(864, 608))

    fraction1 = Fraction(1, 5)
    print("operation add:", fraction1 + Fraction(4, 5))

    print("answer for result:", Fraction(864, 836))
