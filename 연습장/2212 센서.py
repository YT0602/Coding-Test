N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
sensor.sort()
if K >= N:
    print(0)
else:
    # 센서 사이의 거리 리스트
    dis_s = []
    for i in range(1, N):
        dis_s.append(sensor[i]-sensor[i-1])
    dis_s.sort()
    # 가장 멀리 떨어진 센서사이를 기준으로 분리
    # 기준점은 K-1개
    for i in range(K-1):
        dis_s.pop()

    print(sum(dis_s))