# n = int(input())
# for i in range(1, n+1):
#     for j in range(n-i):
#         print(" ", end="")
#     for k in range(i, 0, -1):
#         print(k, end="")
#     print()


# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

n = int(input())

# for i in range(1, n+1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(i, 0, -1):
#         print("*", end="")
#     print()


# for i in range(n, -1, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()


for i in range(1, 2 * n):
    for j in range(1, 2 * n):
        if i == j or i == 1 or j == (2 * n) - i or i == (2 * n) -1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()