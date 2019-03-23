a = [int(i) for i in input('Введите последовательность чисел через пробел: ').split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])
