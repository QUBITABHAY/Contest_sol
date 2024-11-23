n,m=map(int,input().split())
x,y=map(int,input().split())
horizontal_cuts = list(map(int,input().split()))
vertical_cuts = list(map(int,input().split()))
horizontal_cuts.append(0)
horizontal_cuts.append(n)
vertical_cuts.append(0)
vertical_cuts.append(m)
horizontal_cuts.sort()
vertical_cuts.sort()
max_height=0
for i in range(1,len(horizontal_cuts)):
    max_height=max(max_height,horizontal_cuts[i]-horizontal_cuts[i-1])
max_width=0
for i in range(1, len(vertical_cuts)):
    max_width=max(max_width,vertical_cuts[i]-vertical_cuts[i-1])
max_area=max_height * max_width
print(max_area)
