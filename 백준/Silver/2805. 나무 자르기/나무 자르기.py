import sys
input = sys.stdin.readline


def binary_tree(S, E, M):
    cut_tree = 0  # 자른 나무 길이
    mid = (S + E) // 2
    for i in trees:
        if i > mid:
            cut_tree += i - mid
    if S > E:
        return E
    if cut_tree >= M:
        S = mid + 1
        return binary_tree(S, E, M)
    else:
        E = mid - 1
        return binary_tree(S, E, M)


N, M = map(int, input().split())
trees = list(map(int, input().split()))
start = 0
end = max(trees)

print(binary_tree(start, end, M))
