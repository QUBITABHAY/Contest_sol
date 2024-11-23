t = int(input())

for i in range(t):
    n,m = map(int,input().split())
    a=list(map(int,input().split()))
    
    for j in range(n):
        if a[j]==-1:
            if j>0:
                a[j]=(a[j-1]+1)%m
    for k in range(n-1,-1,-1):
        if a[k]==-1:
            if k<n-1:
                a[k]=(a[k + 1]-1+m)%m

    for l in a:
        print(l,end=' ')
    print()