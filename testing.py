def sorting(k):
    l = list(k)
    for i in range(0, len(k)+1):
        for j in range(i+1, len(k)):
            if l[i] >= l[j]:
                l[i], l[j] = l[j], l[i]
    return l

def anagram(n, k):
    if len(n) == len(k):
        v = 0
        for i in range(len(n)):
            for j in range(len(n)):
                if i == j:
                    v += 1
                else:
                    v += 0
            if v == len(n):
                return "Yes"
            else:
                return "No"
    else:
        return "No"
        
n = int(input())
k = int(input())

a = sorting(str(n))
b = sorting(str(k))

z = anagram((a), (b))


print(z)