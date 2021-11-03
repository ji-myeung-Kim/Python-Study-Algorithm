# 백준_1차원 배열_숫자의 개수
# https://www.acmicpc.net/problem/2577

a = int(input())             # 150
b = int(input())             # 266
c = int(input())             # 427

# result = list("17037300")
# result = [1, 7, 0, 3, 7, 3, 0, 0]
# 안에 들어있는 문자열(str)은 list를 사용해서
# 리스트로 변형해주면, 0부터 각각의 index로 저장 됨
mul = list(str(a * b * c))

for i in range(10):          # i = 0 ~ 9
    print(mul.count(str(i)))
    # i를 문자열(str)로 바꿔서 몇 개 있는지 count 함
