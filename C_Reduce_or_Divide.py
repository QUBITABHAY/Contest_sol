def solve(s):
    return int(s[::-1], 2)
for j in range(int(input())):
    input()
    n=solve(input().strip())
    if n==0:
        print("DRAW")
    elif n%2==0:
        print("ALICE")
    else:
        print("BOB")