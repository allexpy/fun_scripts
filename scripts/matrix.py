matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix_product = [[sum([ai*bi for ai, bi in zip(row_a, col_b)])
                   for col_b in zip(*matrix_b)]
                  for row_a in matrix_a]
print(matrix_product)
