# 백준_for문_A+B 8
# https://www.acmicpc.net/problem/11022

t = int(input()) # int형으로 입력 받음
for i in range(1, t+1): # 1부터 입력받은 수까지
    a, b = map(int, input().split()) # 입력받은 두 수를 스플릿으로 쪼갬
    print(f"Case #{i}: {a} + {b} = {a+b}")
    # f-string 문법을 사용(파이썬 3.6버전 이상)