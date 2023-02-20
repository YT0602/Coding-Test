from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
cards = deque(i for i in range(1, N+1))
while len(cards) != 1:
    print(cards.popleft(), end=' ')
    cards.append(cards.popleft())
print(*cards)