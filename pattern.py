def spy_num(n):
    t=n
    sum_n=0
    product=1
    while n>0:
        digit=n%10
        sum_n+=digit
        product*=digit
        n//=10
    if sum_n==product:
        return (t,"is SPY NUMBER")
    else:
        return (t,"is NOT spy number")