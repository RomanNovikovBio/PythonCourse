import random
number = random.randint(0, 100)
print('Я загадал число от 0 до 100, попробуй отгадать')
answer = None
while answer!=number:
    answer = int(input())
    if answer > number:
        print('А вот и не верно! Мое число меньше твоего.')
    elif answer < number:
        print('А вот и не верно! Мое число больше твоего.')
print('Правильно! Ты угадал!')
