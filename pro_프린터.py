# # 1차 풀이

# priorities = [2,1,3,2]
# location = 2

# def solution(priorities, location):
#     cnt = 0
#     arr = []
#     for index, item in enumerate(priorities) :
#         arr.append((item, index))
#     print(arr)   
#     while priorities:          
#         target = arr.pop(0)
#         t = priorities.pop(0)        
#         if len(arr) != 0:
#             if target[0] >= max(priorities) :  # 더 큰 값이 하나도 없으면
#                 cnt += 1  # 인쇄    
#                 if target[1] == location:
#                     return cnt  
#             else:
#                 arr.append(target)  
#                 priorities.append(t)
#         else:
#             cnt += 1
#             if target[1] == location:
#                 return cnt


# 2차풀이
def solution(priorities, location):
    cnt = 0
    return cnt



print(solution(priorities, location))
