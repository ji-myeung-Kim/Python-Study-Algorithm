# 백준_1차원 배열_나머지
# https://www.acmicpc.net/problem/3052

n = []                  # 리스트 생성

for i in range(10):     # 0부터 9까지 반복
    a = int(input())    # 변수로 정수 입력 받음
    b = a % 42          # 입력 받은 정수를 42로 나눈 나머지 값
    n.append(b)         # 위에서 나온 나머지 값을 리스트에 저장

s = set(n)              # set은 중복을 허용하지 않음(걸러짐)
print(len(s))           # 리스트의 남은 길이를 len으로 출력
