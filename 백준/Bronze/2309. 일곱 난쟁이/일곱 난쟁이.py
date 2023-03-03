lst = []
for i in range(9):
    lst.append(int(input()))

lst.sort()

def solve():
    for i in range(9):
        for j in range(i+1, 9):
            if 100 == sum(lst) - (lst[i] + lst[j]):
                lst.pop(j)
                lst.pop(i)
                return lst


result = solve()
for a in result:
    print(a)