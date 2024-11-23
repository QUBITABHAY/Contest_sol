def solve(n):
    for i in range(n // 11 + 1):
        if (n-11*i)%111 == 0:
            return "YES"
    return "NO"

t=int(input())
for j in range(t):
    n=int(input())
    print(solve(n))