"""
프로그래머스 LEVEL2 H-Index
https://programmers.co.kr/learn/courses/30/lessons/42747
어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
"""

# 1차 시도
# def solution(citations):
#     temp = dict()
#     answer = list()
#     for i in range(len(citations)):
#         h = 0
#         for j in citations:
#             if citations[i] <= j:
#                 h += 1
#         temp[citations[i]] = h

#     for k, v in temp.items():
#         print(f'-------------k: {k}, v: {v}')
#         if k <= v:
#             answer.append(k)

#     if not answer:
#         return len(citations)

#     return max(answer)
"""
9, 11, 16만 통과 18점
print(solution([20, 19, 18, 1])) # 3
위의 테스트 케이스같은 경우 조건문에 1이 들어가서 1로 나옴
"""

# 2차 시도
# def solution(citations):
#     temp = dict()
#     answer = list()
#     for i in range(max(citations)+1):
#         h = 0
#         for j in citations:
#             if j >= i:
#                 h += 1
#         temp[i] = h

#     for k, v in temp.items():
#         print(f'-------------k: {k}, v: {v}')
#         if k <= v:
#             answer.append(k)

#     if not answer:
#         return len(citations)

#     return max(answer)
"""
2차 시도 중 for문 조건을 
range(len(citations))으로 설정했더니
print(solution([100, 20, 20, 99])) #4
같은 테스트케이스를 통과하지 못하여
max값 부터 모든 숫자를 탐색하도록 변경하여 통과
해당 방법은 citations의 값이 크고 리스트 길이가 길어질 경우 시간이 오래걸리며, 메모리관련 에러로 불통과될 가능성이 있음
"""

# 리팩토링 버전
def solution(citations):
    # 내림차순으로 정렬
    citations.sort(reverse=True)
    for i in range(len(citations)):
        # for 문을 돌며 해당 인덱스 숫자가 논문 인용 횟수보다 크거나 같을 경우 해당 값을 리턴
        if i >= citations[i]:
            return i
    # 위의 조건에 맞지 않는 경우([100, 20, 20, 99]) 해당 길이만큼 리턴
    return len(citations)

# 테스트 케이스
if __name__ == '__main__':
    print(solution([3, 0, 6, 1, 5])) # 3
    print(solution([100, 20, 20, 99])) # 4
    print(solution([4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6])) # 6
    print(solution([0,1,2,3,3,3,3,3,3,4,10,20,30,40])) # 4
    print(solution([3, 0, 6, 1, 5])) # 3
    print(solution([20, 19, 18, 1])) # 3
    print(solution([5,5,5,5])) # 4
