a=input()
count=0
for i in range(97,123):
    ch=chr(i)
    if ch in a:
        count+=1
if count%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")