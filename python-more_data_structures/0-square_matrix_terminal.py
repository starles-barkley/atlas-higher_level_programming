#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_sq = []
    for row in matrix:
        row_sq = []
        for num in row:
            row_sq.append(num ** 2)
        matrix_sq.append(row_sq)
    return matrix_sq
