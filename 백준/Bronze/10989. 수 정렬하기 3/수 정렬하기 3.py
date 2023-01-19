import sys
input = sys.stdin.readline # 입력 시간 줄이기
N = int(input())
result = [0]*10001 # 최대 입력 수만큼 0 리스트 생성
for i in range(1, N+1): # 입력된 수(중복가능)의 인덱스에 1 추가
    num = int(input())
    result[num] += 1

for i in range(1, 10001): # 다시 전체 돌면서 0이 아니면
    if result[i] != 0:
        for j in range(result[i]): # 카운트된 수만큼 그 숫자 출력(계수정렬)
            print(i)