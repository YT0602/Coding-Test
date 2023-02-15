import sys
input = sys.stdin.readline


def back():
    # 리스트 원소개수가 M개면 재귀 탈출하고 출력
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    # s: [1] -> [1, 2] -> [1] -> [1, 3] -> [1] -> [1, 4] 로 진행
    for i in range(1, N+1):
        if i not in result:
            # 리스트에 없으면 추가하고 다음 자리로 넘어가기 위해 재귀호출
            result.append(i)
            back()
            # 개수 다 채우고 출력하고 난 뒤 다음 숫자 추가하기 위해 pop
            result.pop()


N, M = map(int, input().split())
# 출력 숫자 저장할 리스트
result = []

back()