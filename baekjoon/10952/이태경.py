# 백준_while문_A+B -5
# https://www.acmicpc.net/problem/10952

while True: # True로 무한루프(대소문자 'T' 주의)
    a, b = map(int, input().split())
    if a == 0 and b == 0:   # a와 b가 둘다 0이라면
        break               # break로 while문 탈출
    else:
        print(a + b)        # 아니라면 a와 b를 더함