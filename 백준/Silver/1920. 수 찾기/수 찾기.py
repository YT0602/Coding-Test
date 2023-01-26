import sys

N = int(sys.stdin.readline())
A_list = list(map(int, sys.stdin.readline().split()))
A_list.sort()
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
# 이진탐색
def binary_search(x, A_list):
    start = 0 # 시작지점 인덱스
    end = len(A_list)-1 # 끝지점 인덱스
    while start <= end:
        mid = (start + end) //2 # 중간지점 인덱스
        if A_list[mid] == i:
            return 1
        elif A_list[mid] < i: # 중간점보다 원소가 크면 오른쪽 범위로 다시 탐색
            start = mid + 1 # 시작지점 = 중간점 다음
        elif A_list[mid] > i: # 중간점보다 원소가 작으면 왼쪽 범위로 다시 탐색
            end = mid - 1 # 끝지점 = 중간점 이전
    return 0 # 범위 다 찾아도 없으면 0 반환

for i in M_list:
    print(binary_search(i, A_list))