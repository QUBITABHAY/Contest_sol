t=int(input())
for i in range(t):
    l,r=map(int,input().split())
    a=1
    count=0
    while l<=r:
        l+=a
        count+=1
        a+=1
    print(count)