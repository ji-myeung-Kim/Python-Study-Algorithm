n = int(input())
number = 0
for i in range(1, n+1): # range로 for문이 돌 횟수를 지정
    number += 1         # for문을 돌면서 number에 1씩 추가
    print(number)

# 나중에 찾은 더 간단한 코드
# n = int(input())
# for i in range(1, n+1):
#     print(i)