def preorder(n):
    if n:
        pre.append(n)
        preorder(left[par.index(n)])
        preorder(right[par.index(n)])


def inorder(n):
    if n:
        inorder(left[par.index(n)])
        in_order.append(n)
        inorder(right[par.index(n)])


def postorder(n):
    if n:
        postorder(left[par.index(n)])
        postorder(right[par.index(n)])
        post.append(n)


N = int(input())
par = [0] * (N+1)
left = [0] * (N+1)
right = [0] * (N+1)
pre = []
in_order = []
post = []
for i in range(1, N+1):
    nodes = list(input().split())
    if nodes[1] != '.':
        left[i] = nodes[1]
    if nodes[2] != '.':
        right[i] = nodes[2]
    par[i] = nodes[0]


preorder('A')
inorder('A')
postorder('A')
print(''.join(pre))
print(''.join(in_order))
print(''.join(post))