# 양쪽 빌딩과의 거리 차이가 2 이상인 가구 수만 조망권 확보

T = 10
for tc in range(1, T + 1):
    N = int(input())  # 빌딩 수
    bd = list(map(int, input().split()))  # 빌딩 높이 리스트
    view = 0  # 조망권 확보 가구 수
    for i in range(2, N - 1):  # 양 끝 두 곳 제외
        new = bd[i - 2:i + 3]  # 5채만 뽑아서 비교
        mid = new[2]  # 기준 빌딩
        new = sorted(new)
        if mid == new[-1]:  # 기준 빌딩이 5채 중 가장 높은 경우
            view += mid - new[-2]  # 두번째 높은 빌딩과의 높이 차이만큼 조망권 확보

    print(f'#{tc} {view}')

#출력예시
# #1 691
# #2 9092
# #3 8998
# #4 9597
# #5 8757
# #6 10008
# #7 10194
# #8 10188
# #9 9940
# #10 8684