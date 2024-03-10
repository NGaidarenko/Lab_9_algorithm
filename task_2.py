dims = [3, 2, 2, 4]
print(dims)
n = len(dims)
cost = [[0 for i in range(n + 1)] for j in range((n + 1))]
print(cost)

for i in range(2, n):
    for j in range(1, n - i + 2):
        r = j + i - 1
        cost[j][r] = 10000000
        if r < n:
            for m in range(j, r):
                new_cost = cost[j][m] + cost[m + 1][r] + dims[j - 1] * dims[m] * dims[r]
                cost[j][r] = min(cost[j][r], new_cost)


print(cost[1][n - 1])
