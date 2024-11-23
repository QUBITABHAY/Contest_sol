n, k = map(int,input().split())
s = input()
g = s.index("G")
t = s.index("T")
q = [g]
v = [False] * n
v[g] = True
while q:
    c = q.pop(0)
    if c == t:
        print("Yes")
        break
    for i in [c + k, c - k]:
        if 0 <= i < n and not v[i] and s[i] != "#":
            v[i] = True
            q.append(i)
else:
    print("NO")