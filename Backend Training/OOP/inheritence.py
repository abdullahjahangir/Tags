class A:
    def __init__(self):
        print("A")

    def hello_world(self):
        print("Hello from class A")


class B(A):
    def __init__(self):
        super().__init__()
        print("B")

    def hello_world(self):
        print("Hello from class B")


class C(A):
    def __init__(self):
        super().__init__()
        print("C")

    def hello_world(self):
        print("Hello from class C")


class D(C, B):
    def __init__(self):
        super().__init__()
        print("D")

    def hello_world(self):
        C.hello_world(self)  # Call hello_world method of class C


# Create object of class D
d_obj = D()

# Call hello_world method of class D
d_obj.hello_world()  # Output: Hello from class C
