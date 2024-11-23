a,b=map(int,input().split())
l=list(map(int,input().split()))
mx=5-b
res=sum(1 for i in l if i<=mx)
ress=res//3
print(ress)