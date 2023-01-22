N = int(input())
count = 0
num = 666
while True:
    if '666' in str(num): # num에 666이 포함되어 있으면 count 1 증가
        count += 1
    if count == N: # count가 N이랑 같으면 프린트하고 종료
        print(num)
        break
    num += 1 # num 1씩 증가하면서 반복
