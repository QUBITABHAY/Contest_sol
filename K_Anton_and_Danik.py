n = int(input())
s = input()
a = []
d = []
for i in s:
    if i == "A":
        a.append(i)
    else:
        d.append(i)
        
if len(a) > len(d):
    print("Anton")
elif len(d) > len(a):
    print("Danik")
else:
    print("Friendship")