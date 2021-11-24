# 백준_1차원 배열_최소, 최대
# https://www.acmicpc.net/problem/10818

# 내장함수 version
n = int(input())
n2 = list(map(int, input().split()))    # 인트형 숫자들을 공백(스플릿)으로 배열에 저장
print(min(n2), max(n2))                 # 파이썬 내장함수 mix, max 사용

# # 전통의 for문 version
# n = int(input())
# n2 = list(map(int, input().split()))
# min = n2[0]         # 배열의 첫 번째 수(index 0)
# max = n2[0]         # 배열의 첫 번째 수(index 0)
#
# for i in n2[1:]:    # 배열의 두 번째 수(index 1)부터 끝까지
#     if i > max:     # max보다 크면, max값을 바꿔 주고
#         max = i     # min보다 작으면, min값을 바꿔 줌
#     elif i < min:
#         min = i
#
# print(min, max)
