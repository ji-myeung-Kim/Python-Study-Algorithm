# 태권왕 
# https://www.acmicpc.net/problem/14562

# ---------문제 해석---------------------------------------------------------------------- 
# 태균이의 점수S와 상대의 점수T가 주어지고, 태균이는 항상 지고 있는 상황이다(1 ≤ S < T ≤ 100).
# S와 T가 같아 지는 시점의 발차기 횟수를 구하되, 최솟값으로 계산해야 한다.
# 발차기 A는 점수S 를 두 배로, 점수 T는 +3을 적용한다.
# 발차기 B는 점수S 에만 +1을 적용한다

# ---------접근 방법---------------------------------------------------------------------- 
# 모든 경우를 검증하는 BFS방법으로 시도 

# 매 회차에 발차기 A와 발차기 B를 시행하고, 각각의 경우에 S == T 인지 검증한다.
# 다음 회차에는 이전 회차에서 발차기 A를 시행한 케이스와 발차기 B를 시행한 케이스에 각각 다시 발차기 A,B를 시행한다.
# S == T인 경우의 시행회차를 최솟값으로 리턴하고 종료.

# 예상되는 문제: 매 회차마다 계산할 케이스가 2배씩 늘어난다 
# ---------1차 오답---------------------------------------------------------------------- 
# 문제점: 예상대로 케이스가 2배씩 늘어나는 부작용 -> 시간초과 발생... 
# 마지막 케이스 [34 59]는 계산해야 할 케이스가 2**25 = 33554432개...

# => 케이스를 생성하면서 S > T가 되는 경우는 케이스를 더 이상 생성하지 않도록 수정 시도 
# ----------------------------------------------------------------------------------------

def kick(case_list):
    for cl in case_list:
        count = 0
        queue = [cl]
        
        while queue:
            for i in range(len(queue)):
                now = queue.pop(0)
                if now[0] == now[1]:
                    queue = False
                    break
                else:
                    A = [now[0]+1, now[1]]
                    B = [now[0]*2, now[1]+3]
                    if A[0] <= A[1]:
                        queue.append(A)
                    if B[0] <= B[1]:
                        queue.append(B)
            if queue:
                count += 1
        print(count)


import sys

input_count = 0
first_line = 0
cases = []

while input_count <= first_line:
    input = list(map(int, sys.stdin.readline().split()))
    if first_line == 0:
        first_line = input[0]
    else:
        cases.append(input)
    input_count += 1

kick(cases)


# ---------1차 오답---------------------------------------------------------------------- 
# 문제점: 예상대로 케이스가 2배씩 늘어나는 부작용 -> 시간초과 발생... (마지막 케이스 - 34 59)

# ----------------------------------------------------------------------------------------

# def kick(case_list):
#     for cl in case_list:
#         count = 0
#         queue = [cl]
        
#         while queue:
#             for i in range(len(queue)):
#                 now = queue.pop(0)
#                 if now[0] == now[1]:
#                     queue = False
#                     break
#                 else:
#                     queue.append([now[0]+1, now[1]])
#                     queue.append([now[0]*2, now[1]+3])
#             if queue:
#                 count += 1

#         print(count)


# import sys

# input_count = 0
# first_line = 0
# cases = []

# while input_count <= first_line:
#     input = list(map(int, sys.stdin.readline().split()))
#     if first_line == 0:
#         first_line = input[0]
#     else:
#         cases.append(input)
#     input_count += 1

# kick(cases)

# ----------------------------------------------------------------------------------------