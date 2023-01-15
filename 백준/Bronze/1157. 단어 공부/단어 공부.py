import string

a = input()
A = a.upper()
UP = [i for i in string.ascii_uppercase]
result = []
for i in UP:
    count = A.count(i)
    result.append(count)
max_index = result.index(max(result))
if result.count(max(result)) > 1:
    print('?')
else:
    print(UP[max_index])