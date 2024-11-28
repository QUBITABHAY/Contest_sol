n = int(input())
sum = 0
d = {"Tetrahedron": 4, "Cube": 6, "Octahedron": 8, "Dodecahedron": 12, "Icosahedron": 20}
for i in range(n):
    a = input()
    if a in d:
        sum += d[a]
    else:
        sum += 0
print(sum)