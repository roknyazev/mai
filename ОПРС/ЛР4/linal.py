class Matrix:
    def __init__(self, matrix):
        self.matrix = list(matrix)

    def determinant(self):
        return determinant(self.matrix)

    def transpose(self):
        final_matrix = []
        for i in range(len(self.matrix)):
            temp_column = []
            for j in range(len(self.matrix)):
                temp_column.append(self.matrix[j][i])
            final_matrix.append(temp_column)
        return final_matrix

    def inverse(self):
        final_matrix = []
        for i in range(len(self.matrix)):
            final_matrix_column = []
            for j in range(len(self.matrix)):
                co_factor = (-1) ** (i + j) * determinant(minor(self.matrix, j, i))  # Алгебраическое дополнение
                final_matrix_column.append(co_factor / determinant(self.matrix))
            final_matrix.append(final_matrix_column)
        return final_matrix

    def __add__(self, matrix_2):
        final_matrix = []
        for i in range(len(self.matrix)):
            temp_column = []
            for j in range(len(self.matrix[i])):
                temp_column.append(str(float(self.matrix[i][j]) + float(matrix_2[i][j])))
            final_matrix.append(temp_column)
        return final_matrix

    def __sub__(self, matrix_2):
        final_matrix = []
        for i in range(len(self.matrix)):
            temp_column = []
            for j in range(len(self.matrix[i])):
                temp_column.append(str(float(self.matrix[i][j]) - float(matrix_2[i][j])))
            final_matrix.append(temp_column)
        return final_matrix

    def __mul__(self, matrix_2):
        """
        Если matrix_1 и 2 - одномерные массивы, следует применить scalar_product
        """
        final_matrix = []
        for j in range(len(self.matrix[0])):
            temp_row = []
            temp_column = []
            for i in range(len(self.matrix)):
                temp_row.append(str(self.matrix[i][j]))
            for k in range(len(matrix_2)):
                temp_column.append(str(scalar_product(temp_row, matrix_2[k])))
            final_matrix.append(temp_column)
        return final_matrix

    def get_row_count(self):
        return len(self.matrix)

    def get_col_count(self):
        return len(self.matrix[0])

    def symmetric_matrix_inverse(self, matrix):
        pass


class Vector:
    def __init__(self, vector):
        self.vec = vector

    def vector_scalar_product(self, vec_2):
        scalar_product(self.vec, vec_2)

    def __mul__(self, vec_2):
        return [(self.vec[1] * vec_2[2] - self.vec[2] * vec_2[1]), (self.vec[2] * vec_2[0] - self.vec[0] * vec_2[2]),
                (self.vec[0] * vec_2[1] - self.vec[1] * vec_2[0])]

    def length(self):
        return self.vec[0] ** 2 + self.vec[1] ** 2 + self.vec[2] ** 2


def scalar_product(vec_1, vec_2):
    final_scalar = 0
    for i in range(len(vec_1)):
        final_scalar += float(vec_1[i]) * float(vec_2[i])
    return final_scalar


def minor(matrix, i, j):
    final_matrix = []
    for row in range(len(matrix)):
        if row != i:
            temp_column = []
            for column in range(len(matrix[row])):
                if column != j:
                    temp_column.append(float(matrix[row][column]))
            final_matrix.append(temp_column)
    return final_matrix


def determinant(matrix):
    m = list(matrix)
    det = 0
    if len(matrix) == 1:
        det += float(matrix[0][0])
    else:
        for i in range(len(matrix)):
            det += (-1) ** (i + 1) * determinant(minor(m, i, 1)) * float(matrix[i][1])
    return det


class SymmetricMatrix(Matrix):

    def __init__(self, matrix):
        super().__init__(matrix)

    def Inverse(self):
        n = self.get_row_count()
        L = self.lower_matrix()
        tmp = list(self.matrix)
        for i in range(n - 1, -1, -1):
            for j in range(i, -1, -1):
                if i == j:
                    tmp[i][j] = (1 / L[i][j]) * ((1 / L[i][j]) - sum(L[k][i] * tmp[k][i] for k in range(i + 1, n)))
                else:
                    tmp[i][j] = (-1 / L[j][j]) * sum(L[k][j] * tmp[k][i] for k in range(j + 1, n))
                    tmp[j][i] = tmp[i][j]
        return tmp

    def lower_matrix(self):
        tmp = list(self.matrix)
        for i in range(self.get_row_count()):
            for j in range(self.get_col_count()):
                if i == j:
                    tmp[i][j] = (self.matrix[i][j] - sum(tmp[i][k] ** 2 for k in range(i))) ** 0.5
                if i > j:
                    tmp[i][j] = (1 / tmp[j][j]) * (self.matrix[i][j] - sum(tmp[i][k] * tmp[j][k] for k in range(j)))
                if i < j:
                    tmp[i][j] = 0
        return tmp


m1 = SymmetricMatrix([[1, 2, 3], [2, 1, 4], [3, 4, 1]])
mi = m1.inverse()
mii = SymmetricMatrix(mi)
print(mii.inverse())
