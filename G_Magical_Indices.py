t=int(input())

for i in range(1,t+1):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    lap=0
    ans=0
    for x in range(1,n):
        for k in range(0,x-1):
            if a[k]<=a[x-1]:
                count=count+1
            if count==x-1:
                for j in range(x,n):
                    if a[j]>=a[x-1]:
                        lap=lap+1
                    if lap==n-j:
                        ans=ans+1
    print(ans)