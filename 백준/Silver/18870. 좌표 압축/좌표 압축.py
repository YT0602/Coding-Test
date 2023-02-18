import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
new = set(numbers)
new2 = sorted(list(new))
idx_dict = {}
for i in range(len(new2)):
    idx_dict[new2[i]] = i
for i in numbers:
    print(idx_dict[i], end=' ')