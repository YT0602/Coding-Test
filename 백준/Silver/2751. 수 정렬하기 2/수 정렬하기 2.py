import sys

N = int(sys.stdin.readline())
n_list = []
for i in range(N):
    num = int(sys.stdin.readline())
    n_list.append(num)

n_list.sort()
for i in n_list:
    print(i)