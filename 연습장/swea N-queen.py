def queen(num):
    global cnt
    # N행까지 내려왔으면 카운트
    if num == N:
        cnt += 1
        return

    for i in range(N):
        # 각 배열의 모든 칸이 비어있으면 배치 하고 재귀
        if arr1[i] == arr2[num] == arr3[num-i] == arr4[num+i] == 0:
            arr1[i] = arr2[num] = arr3[num-i] = arr4[num+i] = 1
            queen(num+1)
            arr1[i] = arr2[num] = arr3[num - i] = arr4[num+i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    # 열 체크
    arr1 = [0] * N
    # 행 체크
    arr2 = [0] * N
    # 우하향 대각선 체크
    arr3 = [0] * (2*N-1)
    # 우상향 대각선 체크
    arr4 = [0] * (2*N-1)
    queen(0)
    print(f'#{tc} {cnt}')