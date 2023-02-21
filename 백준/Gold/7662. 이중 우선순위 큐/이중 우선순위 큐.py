import sys
import heapq

input = sys.stdin.readline

T = int(input())
for tc in range(T):
    # 최소 힙
    mn_H = []
    # 최대 힙
    mx_H = []
    # 삭제 된 원소인지 확인하기 위한 리스트
    visited = [0] * 1000001
    # 연산 횟수
    k = int(input())
    for i in range(k):
        text = list(input().split())
        # I면 몇번째 연산인지와 함께, 원소 추가
        if text[0] == 'I':
            heapq.heappush(mn_H, (int(text[1]), i))
            heapq.heappush(mx_H, (-int(text[1]), i))  # 최대이므로 - 붙여서 추가
            # 원소 추가됨
            visited[i] = 1

        elif text[0] == 'D':
            if text[1] == '-1' and len(mn_H) != 0:
                # 힙 맨 앞의 원소가 삭제되었던 원소라면 pop
                while mn_H and visited[mn_H[0][1]] == 0:
                    heapq.heappop(mn_H)
                # 아직 삭제 안됐으면 직접 삭제 처리
                if mn_H:
                    visited[mn_H[0][1]] = 0
                    heapq.heappop(mn_H)

            elif text[1] == '1' and len(mx_H) != 0:
                while mx_H and visited[mx_H[0][1]] == 0:
                    heapq.heappop(mx_H)
                if mx_H:
                    visited[mx_H[0][1]] = 0
                    heapq.heappop(mx_H)
    # 아직 남은 잉여 원소들 확인하고 삭제 처리
    while mn_H and visited[mn_H[0][1]] == 0:
        heapq.heappop(mn_H)
    while mx_H and visited[mx_H[0][1]] == 0:
        heapq.heappop(mx_H)
    # 원소 있으면 각각 맨 앞의 원소 출력
    if mn_H and mx_H:
        print(-mx_H[0][0], mn_H[0][0])
    else:
        print('EMPTY')