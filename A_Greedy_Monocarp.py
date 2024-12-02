# It's wrong

t = int(input())
for i in range(t):  
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    total_sum = sum(l)
    coin = 0
    if total_sum >= k:
        taken = 0
        for i in range(n):
            taken +=l[i]
            if taken >= 0:
                break
        coin += (k - taken)
        print(coin)
    else:
        taken = 0
        for i in range(n):
            taken += l[i]
            if taken >= k:
                break
        r = k - taken
        coin += r
        print(coin)