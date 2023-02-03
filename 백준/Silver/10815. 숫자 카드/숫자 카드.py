import sys

input = sys.stdin.readline


# 이분탐색
def bi(num):
    S = 0
    E = len(cards) -1
    while S <= E:
        mid = (S + E) // 2
        if i == cards[mid]:
            return 1
        elif i < cards[mid]:
            E = mid - 1
        elif i > cards[mid]:
            S = mid + 1
    else:
        return 0


N = int(input())
cards = list(map(int, input().strip().split()))
cards.sort()
M = int(input())
numbers = list(map(int, input().strip().split()))

result = []

for i in numbers:
    result.append(bi(i))

print(*result)