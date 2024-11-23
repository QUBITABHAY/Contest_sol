s = input()
lcount=0
ucount=0
for i in s:
    if ord(i)>96:
        lcount+=1
    else:
        ucount+=1
if lcount < ucount :
    d = s.upper()
    print(d)
elif lcount == ucount :
    d = s.lower()
    print(d)
else:
    d = s.lower()
    print(d)