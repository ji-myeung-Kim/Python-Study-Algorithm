# 백준_for문_별 찍기-1
# https://www.acmicpc.net/problem/2438

n = int(input())        # 1부터 n까지
for i in range(1, n+1):
    print("*" * i)      # 1부터 n까지 for문이 돌면서 별 생성
