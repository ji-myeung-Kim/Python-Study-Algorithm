'''
문제 - 재귀
백준 9184 신나는 함수 실행
https://www.acmicpc.net/problem/9184
'''


import sys

input = sys.stdin.readline
memo = {}

def w(a, b, c):
  if (a, b, c) in memo:
    return memo[(a, b, c)]

  elif a <= 0 or b <= 0 or c <= 0:
    return 1
  
  elif a > 20 or b > 20 or c > 20:
    return w(20, 20, 20)

  elif a < b and b < c:
    w_num = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    memo[(a, b, c)] = w_num
    return w_num
  
  else: 
    w_num = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    memo[(a, b, c)] = w_num
    return w_num

while True:
  a, b, c = map(int, input().split())
  if a == -1 and b == -1 and c == -1:
    break

  print('w(%d, %d, %d) = %d' % (a, b, c, w(a, b, c)))


'''
풀이
from sys import stdin
read = stdin.readline
memo = {}
    # 해당 키값에 맞는 value를 memo라는 딕션너리에 저장

def w(a, b, c):
  if (a, b, c) in memo:
    return memo[(a, b, c)]
      # 만약에 memo 안에 같은 key가 있으면 value 리턴

  elif a <= 0 or b <= 0 or c <= 0:
    return 1
        # 셋 중 하나라도 0보다 작거나 같다면 1 리턴
  
  elif a > 20 or b > 20 or c > 20:
    return w(20, 20, 20)
        # 셋 중 하나라도 20보다 크다면 모두 20을 넣은 값을 리턴

  elif a < b and b < c:
    w_num = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    memo[(a, b, c)] = w_num
    return w_num
        # a보다 b가 크고 b보다 c가 크다면  
        # 새로운 key와 value를 메모에 저장하고 value를 리턴
  
  else: 
    w_num = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    memo[(a, b, c)] = w_num
    return w_num

while True:
  a, b, c = map(int, read().split())
  if a == -1 and b == -1 and c == -1:
    break
      # a, b, c 값 모두가 -1 일 때 입력을 마지막으로 해야하기 때문에 while loop을 break
      
  print('w(%d, %d, %d) = %d' % (a, b, c, w(a, b, c)))
      # %d를 사용해서 ''안에 필요한 지정값을 넣어줄 수 있음
'''