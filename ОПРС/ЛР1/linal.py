import numpy as np


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
    det = 0
    if len(matrix) == 1:
        det += float(matrix[0][0])
    else:
        for i in range(len(matrix)):
            det += (-1) ** (i + 1) * determinant(minor(matrix, i, 1)) * float(matrix[i][1])
    return det


def transpose(matrix):
    final_matrix = []
    for i in range(len(matrix)):
        temp_column = []
        for j in range(len(matrix)):
            temp_column.append(matrix[j][i])
        final_matrix.append(temp_column)
    return final_matrix


def inverse(matrix):
    final_matrix = []
    for i in range(len(matrix)):
        final_matrix_column = []
        for j in range(len(matrix)):
            co_factor = (-1) ** (i + j) * determinant(minor(matrix, j, i))  # Алгебраическое дополнение (трансп.)
            final_matrix_column.append(co_factor / determinant(matrix))
        final_matrix.append(final_matrix_column)
    return final_matrix


def matrix_sum(matrix_1, matrix_2):
    final_matrix = []
    for i in range(len(matrix_1)):
        temp_column = []
        for j in range(len(matrix_1[i])):
            temp_column.append(str(float(matrix_1[i][j]) + float(matrix_2[i][j])))
        final_matrix.append(temp_column)
    return final_matrix


def scalar_product(vec_1, vec_2):
    final_scalar = 0
    for i in range(len(vec_1)):
        final_scalar += float(vec_1[i]) * float(vec_2[i])
    return final_scalar


def matrix_product(matrix_1, matrix_2):
    """
    Если matrix_1 и 2 - одномерные массивы, следует применить scalar_product
    """
    final_matrix = []
    for j in range(len(matrix_1[0])):
        temp_row = []
        temp_column = []
        for i in range(len(matrix_1)):
            temp_row.append(str(matrix_1[i][j]))
        for k in range(len(matrix_2)):
            temp_column.append(str(scalar_product(temp_row, matrix_2[k])))
        final_matrix.append(temp_column)
    return final_matrix


def vector_product(vec_1, vec_2):
    return [(vec_1[1] * vec_2[2] - vec_1[2] * vec_2[1]), (vec_1[2] * vec_2[0] - vec_1[0] * vec_2[2]),
            (vec_1[0] * vec_2[1] - vec_1[1] * vec_2[0])]


def vector_len(vec):
    return vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2


def symmetric_matrix_inverse(matrix):
    pass


"""c = [[1, 0], [0, 1]]
b = [7]
a = [[5, 6], [4, 9]]
m = np.array([[6, 7, 2], [7, -7, 5], [3, 1, 2]])
n = np.array([[56, 7, 2], [7, 47, 45], [3, 41, 2]])

print(m)
print(determinant(m))
inverse(m)
print(np.array(inverse(m)))
print(np.array(matrix_product(m, np.array(inverse(m)))))
print(np.linalg.inv(m))"""
