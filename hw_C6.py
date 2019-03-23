s = input()
t = input()
result = []
length = len(t)

for i in range(len(s) - length):
    if s[i:i+length] == t:
        result.append(i + 1)

for i in result:
    print(i, end = ' ')
