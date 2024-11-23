def min_dis(d1,d2,d3):
    a=d1+d2+d3
    b=2*(d1+d2)
    c=2*(d2+d3)
    d=2*(d1+d3)
    return min(a,b,c,d)
d1,d2,d3=map(int,input().split())
x=min_dis(d1,d2,d3)
print(x)