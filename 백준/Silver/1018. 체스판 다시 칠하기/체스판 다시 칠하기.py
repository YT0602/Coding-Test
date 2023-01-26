import sys

N, M = map(int, sys.stdin.readline().split()) # 행, 열 입력
chess = [] # 체스판 리스트
count_list = [] # 횟수 리스트
for i in range(N): # 행 수 만큼 입력
    BW_row = input()
    chess.append(BW_row)

for i in range(N-7): # 범위 벗어나지 않게 반복
    for j in range(M-7):
        W = 0 # 처음 시작이 흰색일때 횟수
        B = 0 # 처음 시작이 검은색일때 횟수
        for k in range(i, i + 8): # 8x8이므로 8번째까지 반복
            for l in range(j, j+8):
                # 짝수인 경우 일정한 색 가지고, 홀수인 경우 색이 다 같으므로
                # 행+열 = 홀, 짝 확인으로 체크무늬 확인할 수 있다
                # 행,열로 나타낸 체스판, 처음이 흰색인 경우
                # (0,0)흰 (0,1)검 (0,2)흰 (0,3)검 (0,4)흰
                # (1,0)검 (1,1)흰 (1,2)검 (1,3)흰 (1,4)검
            
                # 처음이 검이면  검흰검흰검
                #              흰검흰검흰
                if (l + k) % 2 == 0: # 행+열이 짝수일때
                    if chess[k][l] != 'W': # W가 아니면
                        W += 1 # 처음 시작이 흰색인 경우 횟수 추가
                    if chess[k][l] != 'B': # B가 아니면
                        B += 1 # 처음 시작이 검은색인 경우 횟수 추가
                else: # 행+열이 홀수일때
                    if chess[k][l] != 'B':
                        W += 1
                    if chess[k][l] != 'W':
                        B += 1
        count_list.append(W) # 총 횟수 리스트에 추가
        count_list.append(B)

print(min(count_list)) # 최솟값 출력