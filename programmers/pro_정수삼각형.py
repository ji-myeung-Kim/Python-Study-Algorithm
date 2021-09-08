# 테스트케이스만 통과.. 런타임 에러
# def solution(triangle):
#     answer = 0
#     for i in range(0, len(triangle[-1])-1):
#         result = []
#         n = len(triangle)-1
#         k = i+1
#         def find_max(result, k, n):
#             if n == 0:
#                 result.append(triangle[n][0])
#                 return
#             if k == 0:
#                 result.append(triangle[n][0])
#             else:
#                 max_value = max(triangle[n][k-1], triangle[n][k])
#                 result.append(max_value)
#                 k = triangle[n].index(max_value)
#             find_max(result, k, n-1)
#             return result

#         find_max(result, k, n)    
#         if sum(result) > answer:
#             answer = sum(result)
#     return answer

def solution(triangle):
    answer = ""
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	
print(solution(triangle))