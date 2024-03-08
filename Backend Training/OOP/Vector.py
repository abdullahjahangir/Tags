import math


class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"< {self.x}i, {self.y}j, {self.z}k > "

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def add(self, v):
        return Vector(self.x + v.x, self.y + v.y, self.z + v.z)

    def unit_vector(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError(
                "Cannot compute the unit vector of the zero vector.")
        x = self.x / mag
        y = self.y / mag
        z = self.z / mag
        return Vector(x, y, z)

    def scalar_multiply(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        z = self.z * scalar
        return Vector(x, y, z)

    def dot_product(self, v):
        x = self.x * v.x
        y = self.y * v.y
        z = self.z * v.z
        return x+y+z

    def cross_product(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    @staticmethod
    def equals(v1, v2):
        if v1.magnitude() == v2.magnitude():
            # Using Direction Cosines: ( x/ ∣V∣, y/∣V∣​, z / ∣V∣
            if ((v1.x/v1.magnitude() == v2.x/v2.magnitude()) and (v1.y/v1.magnitude() == v2.y/v2.magnitude()) and (v1.z/v1.magnitude() == v2.z/v2.magnitude())):
                return True
        return False
