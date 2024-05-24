a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(a[0])):
    for j in range(len(a)):
        print(a[i][j])

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a)):
        if i == j:
            a[i][j] = 0
        elif i > j:
            a[i][j] = 1
        else:
            a[i][j] = 2
for i in range(len(a)):
    for j in range(len(a)):
        print(a[i][j], end=" ")
    print()
array = [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
]
