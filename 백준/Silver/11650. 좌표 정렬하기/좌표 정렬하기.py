import sys

N = int(sys.stdin.readline())
numbers = []
for test_case in range(N):
    num = tuple(map(int, sys.stdin.readline().split()))
    numbers.append(num)

numbers = sorted(numbers, key = lambda x: (x[0],x[1]))
for i in numbers:
    print(*i)