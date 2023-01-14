a = []
for i in range(10):
    number = int(input())
    x = number % 42
    if x not in a:
        a.append(x)
print(len(a))