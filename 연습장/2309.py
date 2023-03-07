# from itertools import combinations
# h = []
# for i in range(9):
#     h.append(int(input()))
#
# ans = []
# for i in combinations(h, 7):
#     if sum(i) == 100:
#         i = list(i)
#         i.sort()
#         for num in i:
#             print(num)

lst = []
for i in range(9):
    lst.append(int(input()))

lst.sort()

# for a in range(9):
#     for b in range(a+1, 9):
#         for c in range(b + 1, 9):
#             for d in range(c + 1, 9):
#                 for e in range(d + 1, 9):
#                     for f in range(e + 1, 9):
#                         for g in range(f + 1, 9):
#                             if lst[a] + lst[b] + lst[c] + lst[d] + lst[e] + lst[f] + lst[g] == 100:
#                                 print(lst[a])
#                                 print(lst[b])
#                                 print(lst[c])
#                                 print(lst[d])
#                                 print(lst[e])
#                                 print(lst[f])
#                                 print(lst[g])

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