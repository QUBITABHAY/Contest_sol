n = input().strip()
c = "a"
v = 0
for ca in n:
    p = ord(c) - ord("a")
    t = ord(ca) - ord("a")
    d = (t - p) % 26
    s = (p - t) % 26
    v += min(d, s)
    c = ca
print(v)