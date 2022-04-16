a = [1, 5, 1, 2, 3, 10, 4, 6]
"""
Сортировка пузырьком.
"""
n = len(a)
for i in range(n):
    for j in range(0, n - i - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)
