# 백준_for문_X보다 작은 수
# https://www.acmicpc.net/problem/10871

n, x = map(int, input().split())    # n과 x의 숫자를 int형으로 받아서 split으로 쪼갬
a = list(map(int, input().split())) # 리스트 안에 숫자들을 int형으로 받아서 split으로 쪼갬
for i in range(n):  # n이 10이라면, 리스트 안에 index들을 0~9까지 입력됨
    if a[i] < x:    # x보다 작은 수를 솎아 낸다
            print(a[i], end=" ")    # 솎아진 수를 줄바꿈 없이 " " 한칸 공백으로 출력
