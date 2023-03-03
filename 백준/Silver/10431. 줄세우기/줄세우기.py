P = int(input())
for tc in range(1, P+1):
    numbers = list(map(int, input().split()))
    T = numbers.pop(0)
    new = []
    cnt = 0
    while len(new) < 20:
        turn = numbers.pop(0)
        new.append(turn)
        for i in range(len(new)-1):
            if new[i] > turn:
                idx = i
                turn_idx = len(new)-1
                while turn_idx > idx:
                    new[turn_idx-1], new[turn_idx] = new[turn_idx], new[turn_idx - 1]
                    turn_idx -= 1
                    cnt += 1
                break
    print(T, cnt)