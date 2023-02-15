import sys
input = sys.stdin.readline

def back():
    if len(result) == M+1:
        print(' '.join(map(str, result[1:])))
        return
    for i in range(1, N+1):
        if i not in result:
            if i >= result[len(result)-1]:
                result.append(i)
                back()
                result.pop()


N, M = map(int, input().split())
result = [0]

back()