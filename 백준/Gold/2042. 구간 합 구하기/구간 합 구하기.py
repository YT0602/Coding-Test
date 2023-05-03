# 세그먼트 트리 생성
def segment(start, end, idx):
    if start == end:
        tree[idx] = numbers[start]
        return tree[idx]
    mid = (start+end) // 2
    tree[idx] = segment(start, mid, idx*2) + segment(mid+1, end, idx*2+1)
    return tree[idx]


# 세그먼트 트리 구간 합
def segment_sum(start, end, idx, find_s, find_e):
    # 범위 밖
    if end < find_s or start > find_e:
        return 0
    elif start >= find_s and end <= find_e:
        return tree[idx]
    mid = (start+end)//2
    return segment_sum(start, mid, idx*2, find_s, find_e) + segment_sum(mid+1, end, idx*2+1, find_s, find_e)


# 값 변경
def segment_change(start, end, idx, ch_idx, value):
    if start == end:
        tree[idx] = value
    else:
        mid = (start+end)//2
        if start <= ch_idx <= mid:
            segment_change(start, mid, idx*2, ch_idx, value)
        else:
            segment_change(mid+1, end, idx * 2+1, ch_idx, value)
        tree[idx] = tree[idx*2] + tree[idx*2+1]


N, M, K = map(int, input().split())
numbers = [0]
tree = [0] * (N*4)
for _ in range(N):
    num = int(input())
    numbers.append(num)

segment(1, N, 1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        segment_change(1, N, 1, b, c)
    elif a == 2:
        print(segment_sum(1, N, 1, b, c))