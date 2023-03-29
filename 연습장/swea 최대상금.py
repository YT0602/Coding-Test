def DFS(num, cnt):
    if cnt == 0:
        v[cnt].add(int(''.join(num)))
        return
    # 가지치기
    # set에 있으면 중단, 없으면 추가
    if int(''.join(num)) in v[cnt]:
        return
    v[cnt].add(int(''.join(num)))

    for i in range(len(num)):
        for j in range(i+1, len(num)):
            num[i], num[j] = num[j], num[i]
            DFS(num, cnt-1)
            num[i], num[j] = num[j], num[i]


T = int(input())
for tc in range(1, T+1):
    num, cnt = map(int, input().split())
    # cnt 단계마다 가지치기위해 cnt만큼 set 생성
    v = [set() for _ in range(cnt + 1)]

    DFS(list(str(num)), cnt)
    print(f'#{tc} {max(v[0])}')