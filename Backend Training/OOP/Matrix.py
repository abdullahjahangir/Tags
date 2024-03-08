class Mat2by2:
    def __init__(self, a11, a12, a21, a22):
        self.a11 = a11
        self.a12 = a12
        self.a21 = a21
        self.a22 = a22

    def __str__(self):
        return f"<{self.a11} {self.a12} {self.a21} {self.a22}>"

    def add(self, other):
        if isinstance(other, Mat2by2):
            return Mat2by2(self.a11 + other.a11, self.a12 + other.a12,
                           self.a21 + other.a21, self.a22 + other.a22)
        else:
            raise ValueError("Cannot add a non-Mat2by2 object.")

    def subtract(self, other):
        if isinstance(other, Mat2by2):
            return Mat2by2(self.a11 - other.a11, self.a12 - other.a12,
                           self.a21 - other.a21, self.a22 - other.a22)
        else:
            raise ValueError("Cannot subtract a non-Mat2by2 object.")

    def scalar_multiply(self, scalar):
        return Mat2by2(self.a11 * scalar, self.a12 * scalar,
                       self.a21 * scalar, self.a22 * scalar)

    def multiply(self, other):
        if isinstance(other, Mat2by2):
            return Mat2by2(self.a11 * other.a11 + self.a12 * other.a21,
                           self.a11 * other.a12 + self.a12 * other.a22,
                           self.a21 * other.a11 + self.a22 * other.a21,
                           self.a21 * other.a12 + self.a22 * other.a22)
        else:
            raise ValueError("Cannot multiply by a non-Mat2by2 object.")

    def cofactor_matrix(self):
        # The cofactor matrix of a 2x2 matrix is obtained by swapping a11 and a22
        return Mat2by2(self.a22, -self.a12, -self.a21, self.a11)

    def determinant(self):
        # The determinant of a 2x2 matrix is calculated as a11*a22 - a12*a21
        return self.a11 * self.a22 - self.a12 * self.a21

    def is_singular(self):
        # A matrix is singular if its determinant is zero
        return self.determinant() == 0

    def inverse(self):
        det = self.determinant()
        if det != 0:
            # The inverse of a 2x2 matrix is obtained by dividing the adjugate by the determinant
            cofactor = self.cofactor_matrix()
            return cofactor.scalar_multiply(1 / det)
        else:
            raise ValueError("Matrix is singular; cannot find inverse.")

    def divide(self, other):
        # Division of matrices is equivalent to multiplying by the inverse
        if isinstance(other, Mat2by2):
            return self.multiply(other.inverse())
        else:
            raise ValueError("Cannot divide by a non-Mat2by2 object.")

    def is_null_matrix(self):
        # A matrix is null if all its components are zero
        return self.a11 == 0 and self.a12 == 0 and self.a21 == 0 and self.a22 == 0

    def is_identity_matrix(self):
        # An identity matrix is a square matrix with ones on the main diagonal and zeros elsewhere
        return self.a11 == 1 and self.a12 == 0 and self.a21 == 0 and self.a22 == 1

    def transpose(self):
        # Transposing a 2x2 matrix involves swapping the elements a12 and a21
        return Mat2by2(self.a11, self.a21, self.a12, self.a22)


# Example usage:
matrix1 = Mat2by2(1, 2, 3, 4)
matrix2 = Mat2by2(5, 6, 7, 8)

print("Matrix 1:", matrix1)
print("Matrix 2:", matrix2)

# Addition
result_addition = matrix1.add(matrix2)
print("Matrix Addition:", result_addition)

# Subtraction
result_subtraction = matrix1.subtract(matrix2)
print("Matrix Subtraction:", result_subtraction)

# Scalar Multiplication
scalar = 2
result_scalar_multiply = matrix1.scalar_multiply(scalar)
print(f"Scalar Multiplication by {scalar}:", result_scalar_multiply)

# Matrix Multiplication
result_multiplication = matrix1.multiply(matrix2)
print("Matrix Multiplication:", result_multiplication)

# Matrix Cofactor
cofactor_matrix = matrix1.cofactor_matrix()
print("Matrix Cofactor:", cofactor_matrix)

# Matrix Determinant
determinant_matrix = matrix1.determinant()
print("Matrix Determinant:", determinant_matrix)

# Matrix Singular
is_singular__matrix = matrix1.is_singular()
print("Matrix Singular:", is_singular__matrix)

# Matrix Inverse
inverse__matrix = matrix1.inverse()
print("Matrix Inverse:", inverse__matrix)

# Matrix Divide
divide__matrix = matrix1.divide(matrix2)
print("Matrix Divide:", divide__matrix)

# Matrix Is Null
is_null__matrix = matrix1.is_null_matrix()
print("Matrix is null:", is_null__matrix)

# Matrix Identity
is_identity_matrix = matrix1.is_identity_matrix()
print("Matrix is Identity:", is_identity_matrix)

# Matrix Transpose
transpose_matrix = matrix1.transpose()
print("Matrix Transpose:", transpose_matrix)
