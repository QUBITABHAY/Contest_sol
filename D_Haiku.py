l = ["a", "e", "i", "o", "u"]
i = input()
j = input()
k = input()
count1 = 0
count2 = 0
count3 = 0
for a in i:
    if a in l:
        count1+=1
    else:
        count1+=0
for a in j:
    if a in l:
        count2+=1
    else:
        count2+=0
for a in k:
    if a in l:
        count3+=1
    else:
        count3+=0
        
if count1==5 and count2==7 and count3==5:
    print("YES")
else:
    print("NO")