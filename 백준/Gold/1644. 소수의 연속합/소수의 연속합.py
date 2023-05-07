N = int(input())

ans = 0
arr = [True for i in range(N+1)]
# 에라토스테네스 체
for i in range(2, int(N**0.5)+1):
    if arr[i]:
        j = 2
        while i*j <= N:
            arr[i*j] = False
            j += 1

arr = [i for i in range(2, N+1) if arr[i]] + [0]

# 투 포인터
i = 0
j = 0
subtotal = arr[i]
count = 0

while j < len(arr) - 1:
    # 연속합이 N과 같으면 카운팅해주고
    # 왼쪽, 오른쪽 포인터 둘 다 한칸 진행
    # 왼쪽만 옮겼을 때, 연속합이 감소하므로
    # 반드시 N보다 작아진다. 즉, 오른쪽 포인터도 같이 한 칸 옮겨준다.
    if subtotal == N:
        count += 1
        subtotal -= arr[i]
        i += 1
        j += 1
        subtotal += arr[j]
    # 연속합이 N보다 작으면 값을 키워줘야하므로
    # 오른쪽 포인터를 진행
    elif subtotal < N:
        j += 1
        subtotal += arr[j]
    # 연속합이 N보다 크면 줄여줘야하므로
    # 왼쪽 포인터 진행
    else:
        subtotal -= arr[i]
        i += 1

print(count)