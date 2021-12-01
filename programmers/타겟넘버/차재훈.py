"""
프로그래머스 LEVEL2 타겟넘버
https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3
"""

# 명절 전에 참고해서 풀었으나 기억이 나질 않아 주석 못담
# def solution(numbers, target):
#     answer = 0
#     queue = [[numbers[0],0], [-1*numbers[0],0]]
#     n = len(numbers)
#     while queue:
#         temp, idx = queue.pop()
#         idx += 1
#         if idx < n:
#             queue.append([temp+numbers[idx], idx])
#             queue.append([temp-numbers[idx], idx])
#         else:
#             if temp == target:
#                 answer += 1
#     return answer

# print(solution([1, 1, 1, 1, 1], 3))

# 위의 코드보다 효율적인 풀이
def solution(numbers, target):
    result_list = [0] # 초기값 설정
    for number in numbers:
        sub_list = [] # 자식 노드를 생성하기 위한 빈 리스트
        for list_num in result_list: # 노드 하나하나에 더하고 뺸 값을 더하기 위한 반복문
            sub_list.append(list_num + number) # + 한 경우
            sub_list.append(list_num - number) # - 한 경우
        result_list = sub_list # 다음 숫자를 더하고 뺴기 위해 result_list에 sub_list를 대입
    answer = result_list.count(target) # 모든 경우의 수가 있는 result_list에서 타겟넘버의 개수 확인
    return answer

# 테스트 케이스
if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))