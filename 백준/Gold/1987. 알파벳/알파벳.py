# import sys
# from string import ascii_uppercase
# input = sys.stdin.readline
#
# R, C = map(int, input().split())
# # 배열
# arr = [list(input().strip()) for _ in range(R)]
# # 딕셔너리로 방문처리
# alphabet = list(ascii_uppercase)
# alpha_dict = dict()
# for i in alphabet:
#     alpha_dict.setdefault(i, 0)
# # 사방탐색
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# # 최대 방문횟수
# mx_cnt = 1
#
#
# def DFS(cx, cy, cnt):
#     # 최대 방문 갱신
#     global mx_cnt
#     if cnt > mx_cnt:
#         mx_cnt = cnt
#     for i in range(4):
#         nx = cx + dx[i]
#         ny = cy + dy[i]
#         if 0 <= nx < R and 0 <= ny < C:
#             # 다음 칸 알파벳 방문 안했다면 value 1로 바꾸고 재귀 호출
#             if alpha_dict[arr[nx][ny]] == 0:
#                 alpha_dict[arr[nx][ny]] = 1
#                 DFS(nx, ny, cnt+1)
#                 # 돌아오면 해당 알파벳 value 0
#                 alpha_dict[arr[nx][ny]] = 0
#
#
# DFS(0, 0, 1)
# print(mx_cnt)
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
# 배열
arr = [list(input().strip()) for _ in range(R)]
# 방문한 알파벳
v = set(arr[0][0])
# 사방탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 최대 방문횟수
mx_cnt = 1


def DFS(cx, cy, cnt):
    # 최대 방문 갱신
    global mx_cnt
    if cnt > mx_cnt:
        mx_cnt = cnt
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            # 다음 칸 알파벳이 set에 없다면 추가하고 재귀 호출
            if arr[nx][ny] not in v:
                v.add(arr[nx][ny])
                DFS(nx, ny, cnt+1)
                # 돌아오면 해당 알파벳 제거
                v.remove(arr[nx][ny])


DFS(0, 0, 1)
print(mx_cnt)
