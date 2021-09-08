# 프로그래머스 소수찾기 https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3

import math
from itertools import permutations

def check_primenum(num):
    if num == 0 or num == 1:                            # 0이나 1은 소수가 아니다.
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):     # 인수로 받은 num의 sqrt(제곱근) 까지만 조회해보면 됨
            if num % i == 0:                            # 조회 결과 0으로 나누어 떨어지는 즉시 False반환 후 종료
                return False
        return True

def solution(numbers):
    answer = []
    for i in range(1, len(numbers) + 1):                # 1부터 numbers의 길이까지
        arr = list(permutations(numbers, i))            # 순열로 뽑아내기
        for j in range(len(arr)):
            num = int(''.join(map(str, arr[j])))        # tuple 형태의 데이터(arr[j])를 join하여 int형으로 변환
            if check_primenum(num):                     # 소수체크
                answer.append(num)

    answer = list(set(answer))
    return len(answer)

print(solution("17"))
print(solution("011"))