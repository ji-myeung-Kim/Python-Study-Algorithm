# 백준_1차원 배열_최댓값
# https://www.acmicpc.net/problem/2562

n = []                      # 숫자들을 저장할 리스트
for _ in range(9):          # index 0부터 8까지 9번 반복
    i = int(input())
    n.append(i)             # 리스트에 숫자들을 담기

print(max(n))               # 최댓값 출력(max 함수)
print(n.index(max(n)) + 1)  # index는 0부터 시작하기 떄문에 1을 더해줌

# 위의 for문 코드를 list comprehension 표현식으로 작성 가능
# n = [int(input()) for _ in range(9)]