t = int(input())
for i in range(t):
    m, a, b, c = map(int, input().split())
    r1 = min(m, a)
    r2 = min(m, b)
    rr1 = m - r1
    rr2 = m - r2
    s = min(c, rr1 + rr2)
    total = r1 + r2 + s
    print(total)