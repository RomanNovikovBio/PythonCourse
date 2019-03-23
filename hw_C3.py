a = [str(i) for i in input('Введите слова через пробелы: ').split()]
minlength = min(len(s) for s in a)
print(minlength)
     
