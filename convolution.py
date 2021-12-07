p = [[0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
k = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
n, m = len(p), len(k)
pk = []
s = 0
for i in range(n - m + 1):
    pk.append([])
    for j in range(n - m + 1):
        for z in range(i, i + m):
            for x in range(j, j + m):
                s += p[z][x] * k[z-i][x-j]
        pk[i].append(s)
        s = 0
print(pk)
