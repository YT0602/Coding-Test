import sys
input = sys.stdin.readline

N = int(input())
nodes = list(map(int, input().split()))
tree = [[] for _ in range(N)]


def inorder(s, e, h):
    if s == e:
        tree[h].append(nodes[s])
        return
    mid = (s+e)//2
    tree[h].append(nodes[mid])
    inorder(s, mid-1, h+1)
    inorder(mid+1, e, h+1)


inorder(0, len(nodes)-1, 0)
for i in tree:
    print(*i)