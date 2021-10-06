# 백준_while문_A+B -5
# https://www.acmicpc.net/problem/11021

t = int(input())
for i in range(1, t+1): # 1부터 t까지
    a, b = map(int, input().split())
    print(f"Case #{i}: {a+b}")
    # f-string: 파이썬 3.6에 추가된 최신 문법
    # f-string을 사용하면 {}안은 변수나, 변수를 연산한 값을 입력할 수 있음
    # {}이외에는 일반 문자열처럼 고정된 값으로 출력 됨
