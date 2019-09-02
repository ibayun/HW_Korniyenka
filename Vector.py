class Vector:
    def __init__(self, *x):
        self.x = x

    def check_size(self, first_vector, second_vector):
        if len(first_vector) != len(second_vector):
            raise TypeError(
                'TypeError: Unsupported operands error '
                '- Vectors must be the same dimension'
            )
        else:
            return first_vector, second_vector

    def __sub__(self, other):
        self.check_size(self.x, other.x)
        vector = str([self.x[i] - other.x[i] for i in range(len(self.x))])
        return "New vector:", "{}".format(vector[1:-1])

    def __add__(self, other):
        self.check_size(self.x, other.x)
        vector = str([self.x[i] + other.x[i] for i in range(len(self.x))])
        return "New vector:", "{}".format(vector[1:-1])

    def __mul__(self, other):
        if isinstance(self, int):
            return "New vector :", [el*self for el in other.x]
        elif isinstance(other, int):
            vector = str([el*other for el in self.x])
            return "New vector:", "{}".format(vector[1:-1])

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
            return "New vctor {} , {}, {}".format(rez[0], rez[1], rez[2])


    def __matmul__(self, other):
        self.check_size(self.x, other.x)
        list = [self.x[i] * other.x[i] for i in range(len(self.x))]
        vector = str(sum(list))
        return "New skaljar:", "{}".format(vector)


print(Vector(5, 6, 8, 40) @ Vector(5, 6, 3, 8))
print(Vector(5, 6, 8) + Vector(5, 6, 3))

print(Vector(5, 6, 8, 7) + Vector(5, 6, 3, 8))

print(Vector(5, 6, 8) * Vector(5, 6, 3))


print(Vector(5, 6, 8) * 3)
