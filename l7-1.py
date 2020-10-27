class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        res = ''
        for r in self.matrix:
            for c in r:
                res = res + str(c) + ' '
            res = res + '\n'
        return f'{res}'

    def __add__(self, other):
        res = []
        for r1 in range(len(self.matrix)):
            temp_row = []
            for c1 in range(len(self.matrix[r1])):
                temp_row.append(self.matrix[r1][c1] + other.matrix[r1][c1])
            res.append(temp_row)
        return Matrix(res)


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])

print(matrix_1 + matrix_2)
