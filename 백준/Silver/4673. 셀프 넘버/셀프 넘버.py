def d(n):
    # 각 자릿수를 더하는 과정
    total = sum([int(i) for i in str(n)]) + n
    return total


no_self_num = set()  # 생성자 셋
for i in range(1, 10001):
    no_self_num.add(d(i))
    
for num in range(1, 10001):  # 생성자 셋에 없는 수 = 셀프넘버
    if num not in no_self_num:
        print(num)