N, C = map(int, input().split())
home = []
for _ in range(N):
    home.append(int(input()))
home.sort()

start = 1
# 최대거리
end = home[-1] - home[0]
ans = 0
# 이분탐색
while start <= end:
    # 최대 - 최소 // 2 = 중앙값
    mid = (start + end) // 2
    cur = home[0]
    cnt = 1
    for i in range(1, N):
        # 시작값 + 거리보다 크면 공유기 설치
        if home[i] >= cur + mid:
            cnt += 1
            cur = home[i]
    # 주어진 공유기 갯수보다 설치한 수가 이상이면 차이 키우기
    if cnt >= C:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)