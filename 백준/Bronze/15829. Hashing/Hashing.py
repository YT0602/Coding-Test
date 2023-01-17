import string

L = int(input()) # 문자열 길이
s = list(map(str, input())) # 알파벳 리스트로 변환
r = 31 # r
alphabet = list(string.ascii_lowercase) # 소문자 리스트
xx = 0 # 거듭제곱 수
result = 0 # 결과
for i in s: # 입력 문자열 처음부터
    dex = alphabet.index(i) + 1 # 해당 문자의 알파벳 순서
    result += dex * (r**xx) # 해싱 계산
    xx += 1 # 거듭제곱 수 +1
print(result)