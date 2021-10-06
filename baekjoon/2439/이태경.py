# 백준_for문_별 찍기-2
# https://www.acmicpc.net/problem/2439

n = int(input())
for i in range(1, n + 1):           # 1부터 입력받은 수까지 돌림
    print(" " * (n - i) + "*" * i)
    # 공백을 " "로 설정 -> n - i 만큼 공백 생성 후 -> "*" * i로 별 생성
