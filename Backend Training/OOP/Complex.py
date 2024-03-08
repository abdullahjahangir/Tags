class Complex:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __str__(self) -> str:
        if self.imaginary < 0:
            return f"{self.real}{self.imaginary}i"
        else:
            return f"{self.real}+{self.imaginary}i"

    def __add__(self, other):
        return Complex(self.real+other.real, self.imaginary+other.imaginary)

    def __sub__(self, other):
        return Complex(self.real-other.real, self.imaginary-other.imaginary)

    def __mul__(self, other):
        real = (self.real*other.real) + (-1)*(self.imaginary*other.imaginary)
        imaginary = (self.real*other.imaginary) + (self.imaginary*other.real)
        return Complex(real, imaginary)

    def __truediv__(self, other):
        denominator = (other*other.conjulate()).real
        result = self*other.conjulate()
        result.real = round(result.real/denominator, 2)
        result.imaginary = round(result.imaginary/denominator, 2)
        return result

    def conjulate(self):
        return Complex(self.real, -1*self.imaginary)

    # @classmethod
    # def add(cls, c1, c2):
    #     return cls(c1.real+c2.real,c1.imaginary+c2.imaginary)

    @staticmethod
    def add(c1, c2):
        return Complex(c1.real+c2.real, c1.imaginary+c2.imaginary)


# c1 = Complex(3,2)
# c2 = Complex(4,-5)
# print(c1,c2,Complex.add(c1,c2))
# print(c1/c2)
# print(c1.conjulate())
# print(c1+c2)
# print(c1-c2)
# print(c1*c1.conjulate())


# -----------------------------------------------------------------------------------------

class MyClass:
    @staticmethod
    def static_method():
        print(f"This is a static method")

    def instance_method(self):
        print("Calling static method from instance method:")
        self.static_method()  # Calling static method using self
        MyClass.static_method()  # Calling static method using self

# Creating an instance of the class
# obj = MyClass()

# # Calling instance method
# obj.instance_method()
