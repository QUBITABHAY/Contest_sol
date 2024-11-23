T=int(input())
for i in range(T):
    n=int(input())
    s=input()
    lis=list(s)
    d=len(lis)
    unique=list(set(s))
    occurences=[]
    for i in unique:
        occurences.append(lis.count(i))
    def factorial(n):
        s=1
        for i in range(1,n+1):
            s*=i
        return s
    new_list=[]
    result=any(i%2!=0 for i in occurences)
    if result==True:
        print(0)
    else:
        for i in occurences:
            new_list.append(int(i//2))
        add=sum(new_list)
        inital=1
        for i in new_list:
            inital*=factorial(i)
        ans=factorial(add)/inital
        print(int(ans))