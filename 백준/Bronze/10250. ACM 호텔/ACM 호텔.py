T = int(input())
for test_case in range(T):
    H, W, N = list(map(int, input().split())) # 층, 호실, 몇번째
    a = [] # 배정순서 리스트
    for i in range(1, W+1): # 층수돌고 층별로배정
        for j in range(1, H+1): # 1호실부터 채우므로 층수부터 시작
            if i < 10: # 한자리수 층이면 중간에 0 넣기
                a.append(str(j) + '0' +str(i))
            else:
                a.append((j*100 + i))
    print(a[N-1])