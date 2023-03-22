import sys

input = sys.stdin.readline


def dfs(num):
    global ans
    # N행까지 왔다면 완료
    if num == N:
        ans += 1
        return

    for j in range(N):
        # 열, 대각에 퀸 없다면
        if v1[j] == 0 and v2[j+num] == 0 and v3[j-num] == 0:
            # 체크하고 아래 행으로 재귀호출
            v1[j] = v2[j+num] = v3[j-num] = 1
            dfs(num + 1)
            # 탐색 끝났으면 체크 해제하고 다음 칸으로 이동
            v1[j] = v2[j + num] = v3[j - num] = 0


N = int(input())
ans = 0
# 열, 왼쪽 대각, 오른쪽대각 퀸 있는지 체크 배열
v1, v2, v3 = [[0] * (N * 2) for _ in range(3)]

dfs(0)
print(ans)

