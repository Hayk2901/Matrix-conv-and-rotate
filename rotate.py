matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
n = len(matrix)
new_matrix = []
for i in range(n):
    new_matrix.append([])
    for j in range(n):
        new_matrix[i].append(matrix[n - j - 1][i])
print(new_matrix)
