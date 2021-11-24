#### 1차시도 ####
# def solution(tickets):
#     tickets.sort()
    
#     stack = ["ICN"]
#     stack = []

#     while stack:
#         now = stack.pop(0)
#         stack.append(now)
#         for ticket in tickets:
#             if ticket[0] == now:
#                 stack.append(ticket[1])
#                 tickets.remove(ticket)

#     return stack 

#### 반례 ####
# tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
# 정답: ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]
# 위와 같이 풀면 remove 할때 인덱스값이 바뀌어서 for문으로 탐색 못하는 ticket 생김 




#### 2차시도 ... 1번 케이스 실패 ####
# def solution(tickets):
#     tickets.sort(reverse = True)    
#     stack = ["ICN"]    
#     routes = dict()
#     for t in tickets:
#         routes[(t[0],t[1])] = False

#     answer = []

#     while stack:        
#         now = stack.pop()
#         answer.append(now)
#         if len(answer) > 1:
#             routes[(answer[-2], answer[-1])] = True

#         # 남은 티켓 중 now에서 출발하는 티켓이 있는지 탐색
#         flag = False
#         for t in tickets:
#             if routes[(t[0], t[1])] == False and t[0] == now:
#                 stack.append(t[1])                
#                 flag = True

#         # now에서 출발하는 티켓이 더이상 없다면 정답인지 검사
#         if flag == False:      
#             # 정답이 아니라면 직전 경로를 취소하고 stack에 저장돼있는 다른 경로로 다시 탐색해야함
#             if len(answer) != len(tickets)+1:
#                 routes[(answer[-2], answer[-1])] = False
#                 answer.pop()         
#             else: 
#                 return answer
    
#### 반례 ####
# tickets = [["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]
# 정답: ["ICN", "AOO", "BOO", "COO", "DOO", "EOO", "DOO", "COO", "BOO", "AOO"]
## 두번 이상 잘못된 길로 빠졌을경우 now = stack.pop() 하면 잘못된 값 얻음


#### 3차시도.. 구글링 ###
def solution(tickets):
    tickets.sort(reverse = True)    
    routes = dict()      
    # 딕셔너리에 {출발지: [도착지1, 도착지2..], ...} 형태로 저장
    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)  
        else:
            routes[t1] = [t2]  

    stack = ['ICN']  # 현 시점에서 갈 수 있는 지점들을 담아놓는 스택
    answer = []  

    # 스택을 이용한 깊이우선탐색
    while stack:
        now = stack[-1]  
        if now not in routes or len(routes[now])==0:  # now에서 더 이상 갈 도착지가 없는 경우 = 현 routes 상태에서 now가 가장 마지막 지점이라는 의미
            answer.append(stack.pop())  # 마지막 지점부터 answer에 담기게 된다
        else:  # now에서 갈 도착지가 있는 경우
            stack.append(routes[now].pop())  # 도착지를 stack에 담는다        
        
    answer.reverse()
    return answer

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))