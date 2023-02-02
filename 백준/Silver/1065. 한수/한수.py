def han(n):
    num_l = list(map(int, n))
    if len(num_l) <= 2:
        return True
    x = set()
    for i in range(1, len(num_l)):  # 각 자리수 차이 셋에 추가
        x.add(num_l[i-1] - num_l[i])
    if len(x) == 1:  # 한수면 값이 같아 중복이므로 셋 원소는 1개
        return True


N = int(input())
result = []
for num in range(1, N+1):
    if han(str(num)):
        result.append(num)

print(len(result))