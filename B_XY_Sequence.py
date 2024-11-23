t=int(input())
for i in range(t):
    n,B,x,y=map(int,input().split())
    add=0
    vab=1
    caa=0
    while vab<=n:
        if add+x<=B:
            add+=x
        else:
            add-=y
        vab+=1
        caa+=add
    print(caa)