n = int(input())
strin = input().lower()
if n < 26:
    print("NO")
else:
    u = set(strin)
    if len(u) >= 26 and all(chr in u for chr in "abcdefghijklmnopqrstuvwxyz"):
        print("YES")
    else:
        print("NO")