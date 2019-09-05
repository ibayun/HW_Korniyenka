class Vector:
    def __init__(self, *x):
        self.x = x

    @staticmethod
    def check_size(first_vector, second_vector):
        if len(first_vector) != len(second_vector):
            raise TypeError(
                'TypeError: Unsupported operands error '
                '- Vectors must be the same dimension'
            )
        else:
            return first_vector, second_vector

    def __str__(self):
        return "result of operation - {}".format(self.x)

    def __sub__(self, other):
        self.check_size(self.x, other.x)
        self.x = tuple([self.x[i] - other.x[i] for i in range(len(self.x))])
        return self

    def __add__(self, other):
        self.check_size(self.x, other.x)
        self.x = tuple([self.x[i] + other.x[i] for i in range(len(self.x))])
        return self

    def __mul__(self, other):
        if isinstance(self, int):
            return [el * self for el in other.x]
        elif isinstance(other, int):
            self.x = [el * other for el in self.x]
            return self
        elif len(self.x) != len(other.x):
            raise TypeError(
                'TypeError: Unsupported operands error '
                '- Vectors must be the same dimension'
            )
        else:
            rez = (
                (self.x[1] * other.x[2]) - (self.x[2] * other.x[1]),
                (self.x[2] * other.x[0]) - (self.x[0] * other.x[2]),
                (self.x[0] * other.x[1]) - (self.x[1] * other.x[0])
            )
            return f"New vector* {rez[0]} , {rez[1]}, {rez[1]}"

    def __matmul__(self, other):
        self.check_size(self.x, other.x)
        self.x = sum([self.x[i] * other.x[i] for i in range(len(self.x))])
        return self


if __name__ == "__main__":
    print("Operation @: ", Vector(5, 6, 8, 40) @ Vector(5, 6, 3, 8))
    print("Operation +: ", Vector(5, 6, 8) + Vector(5, 6, 3))
    print(
        "Operation +, + - : ",
        Vector(5, 6, 8, 7) + Vector(5, 6, 3, 8) +
        Vector(5, 6, 8, 7) - Vector(5, 6, 3, 8)
    )
    print("Operation *: ", Vector(5, 6, 8) * Vector(5, 6, 3))
    print("Operation *(with num): ", Vector(5, 6, 8) * 3)
    print("Operation + - *(with num): ",
          Vector(1, 4) + Vector(6, 8) - Vector(5, 1) * 3)
