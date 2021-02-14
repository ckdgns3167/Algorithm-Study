import math

T = int(input())

# 1
for _ in range(T):
    n, m = map(int, input().split())
    base = 1
    if m != n:
        for i in range(m, m - n, -1):
            base *= i

        print(base // math.factorial(n))
    else:
        print(base)

# 2
for _ in range(T):
    n, m = map(int, input().split())
    print(math.comb(m, n))
