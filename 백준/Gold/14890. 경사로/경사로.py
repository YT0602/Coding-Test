N, L = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(N)]
arr2 = list(map(list, zip(*arr1)))
ans = 0


def road(line):
    for i in range(1, N):
        x = line[0]
        # 숫자 모두 같으면 길 완성
        if line.count(x) == N:
            return True
        # 높이 차 1 넘으면 실패
        if abs(line[i] - line[i-1]) > 1:
            return False
        # 오르막
        if line[i] > line[i-1]:
            # 경사로 길이만큼 뒤로 탐색
            for j in range(L):
                # 높이 다르거나, 경사로 이미 있거나, 범위 넘어가면 실패
                if i-j-1 < 0 or line[i-1] != line[i-j-1] or slope[i-j-1]:
                    return False
                # 경사로 구간
                if line[i-1] == line[i-j-1]:
                    slope[i-j-1] = True
        # 내리막
        elif line[i] < line[i-1]:
            # 경사로 길이만큼 앞으로 탐색
            for j in range(L):
                # 높이 다르거나, 경사로 이미 있거나, 범위 넘어가면 실패
                # 인덱스 안벗어나게 범위판단부터 해야함
                if i+j >= N or line[i] != line[i+j] or slope[i+j]:
                    return False
                # 경사로 구간
                if line[i] == line[i+j]:
                    slope[i+j] = True
    return True


for i in range(N):
    slope = [False] * N
    if road(arr1[i]):
        ans += 1
for i in range(N):
    slope = [False] * N
    if road(arr2[i]):
        ans += 1

print(ans)
