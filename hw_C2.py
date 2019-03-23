a = [int(i) for i in input('Введите последовательность чисел через пробел: ').split()]
summ = 0
product = 1
for i in a :
    summ += i
    product *= i
print(f'Сумма чисел = {summ}' , f'Произведение чисел = {product}' , sep = '\n')
