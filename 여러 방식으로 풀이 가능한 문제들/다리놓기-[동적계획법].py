T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    d = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for j in range(m + 1):
        d[1][j] = j
    # print(d)

    for j in range(2, n + 1):
        for k in range(j, m + 1):
            for l in range(k, j - 1, -1):
                d[j][k] += d[j - 1][l - 1]
                # print('j={}, k={}, l={}, d={}'.format(j, k, l, d))

    print(d[n][m])