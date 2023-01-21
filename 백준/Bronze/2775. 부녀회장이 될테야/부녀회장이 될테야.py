T = int(input())
for test_case in range(T):
    floor = int(input())
    ho = int(input())
    room = [i for i in range(1, ho+1)] # 0층에 사는 사람 수 리스트
    for i in range(floor):
        for j in range(1, ho): # 현재 수에 바로 앞의 수를 더해서 반복
            room[j] += room[j-1]
    print(room[-1])
