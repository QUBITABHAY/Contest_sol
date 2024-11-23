import itertools as comb
t=int(input())
power=10**9+7
for p in range(t):
    n=int(input())
    l=list(map(int, input().split()))
    total_sum=0
    for i in range(1,n+1):
        for j in comb.combinations(l,i):
            r=max(j)
            total_sum=(total_sum+r)%power
    print(total_sum)