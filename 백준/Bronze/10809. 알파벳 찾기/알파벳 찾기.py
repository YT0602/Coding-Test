import string
lower = [i for i in string.ascii_lowercase]
N = input()
for i in lower:
    print(N.find(i), end=' ')