import sys
import copy

input = sys.stdin.readline

# 궁수 3명 배치 조합
def comb(arr, n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)
    return result


# 적이 있는지 확인
def is_enemy(arr):
    for i in arr:
        if sum(i):
            return True
    else:
        return False


# 적이 한칸씩 이동
def move(arr):
    for i in range(N - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = [0] * M


# 디펜스 시작
def attack():
    # 잡은 적 리스트
    kill = []
    catch = 0

    for i in arch:
        # 궁수별 잡을 수 있는 적
        enemy = []
        for j in range(N):
            for k in range(M):
                # 배열 돌면서 적 찾으면 거리 계산 후 사정거리 안이면 리스트 추가
                if tmp[j][k] == 1:
                    dis = abs(j - N) + abs(k-i[1])
                    if dis <= D:
                        enemy.append([dis, j, k])
        # 거리, 왼쪽 열 순으로 정렬
        enemy.sort(key=lambda x: (x[0], x[2]))
        # 가장 우선순위 높은 적 잡기
        if enemy:
            kill.append(enemy[0])

    # 잡은 적 0 처리
    for road, x, y in kill:
        tmp[x][y] = 0
        catch += 1
    return catch


N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
mx_cnt = 0
# 궁수 배치 좌표
pos = []
for i in range(M):
    pos.append([N, i])

# 궁수 3명 배치하는 경우의 수
for arch in comb(pos, 3):
    cnt = 0
    # 시뮬레이션 위해 배열 복사
    tmp = copy.deepcopy(arr)
    # 적이 있다면 공격
    while is_enemy(tmp):
        cnt += attack()
        move(tmp)
    mx_cnt = max(cnt, mx_cnt)

print(mx_cnt)
