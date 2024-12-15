t = int(input())
for i in range(t):
    n = input().strip()
    l = []
    for j in reversed(n):
        if j == "p":
            l.append("q")
        elif j == "q":
            l.append("p")
        else:
            l.append("w")
    print("".join(l))