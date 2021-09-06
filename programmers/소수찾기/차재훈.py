"""
프로그래머스 LEVEL2 - 소수 찾기
https://programmers.co.kr/learn/courses/30/lessons/42839
"""

# itertools 사용
import itertools

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = []

    for i in range(1, len(numbers)+1):
        perlist = list(map(''.join, itertools.permutations(numbers, i)))

        for j in set(map(int, perlist)):
            if is_prime(int(j)):
                answer.append(j)
    return len(set(answer))


# 테스트케이스
print(solution("17"))
print(solution("011"))
