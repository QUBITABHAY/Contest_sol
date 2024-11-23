guest = input()
host = input()
pile = input()

master =sorted(guest + host)
o = sorted(pile)

if master == o:
    print("YES")
else:
    print("NO")