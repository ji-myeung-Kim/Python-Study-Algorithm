"""
프로그래머스 LEVEL3 - 여행경로
https://programmers.co.kr/learn/courses/30/lessons/43164
"""

# 1차시도
# def solution(tickets):
#     answer = []
#     route = {}
#     for ticket in tickets:
#         if ticket[0] not in route:
#             route[ticket[0]] = [ticket[1]]
#         else:
#             route[ticket[0]].append(ticket[1])
#     country_list = ['ICN']

#     while country_list:
#         country = country_list[-1]

#         if not route[country]:
#             answer.append(country_list.pop())
#         else:
#             country_list.append(route[country].pop())
    
#     return answer

# if __name__ == '__main__':
#     tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
#     tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
#     print(solution(tickets)) # answer : ["ICN", "JFK", "HND", "IAD"]
#     print(solution(tickets2)) # answer : ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
"""
    첫번째 테스트 케이스에서 KeyError 발생(20라인 : if not route[country])
    마지막에 방문하는 IAD가 key로 등록되어 있지 않음
"""

# 2차시도
# def solution(tickets):
#     answer = []
#     route = {}
#     for ticket in tickets:
#         if ticket[0] not in route:
#             route[ticket[0]] = [ticket[1]]
#         else:
#             route[ticket[0]].append(ticket[1])
    
#     country_list = ['ICN']
    
#     while country_list:
#         country = country_list[-1]
#         try:
#             if not route[country]:
#                 answer.append(country_list.pop())
#             else:
#                 country_list.append(route[country].pop())
#         except KeyError:
#             route[country] = []
    
#     answer.reverse()
    
#     return answer

# if __name__ == '__main__':
#     tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
#     tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
#     print(solution(tickets)) # answer : ["ICN", "JFK", "HND", "IAD"]
#     print(solution(tickets2)) # answer : ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
"""
    두번째 테스트 케이스에서 가운데에 위치한 도시 순서가 다름
    하나의 출발지에서 두개 이상의 도착지가 존재할 경우 알파벳 순서가 앞서는 경로를 선택해야하는데 정렬이 되어 있지 않음
"""

# 3차시도
def solution(tickets):
    answer = []
    route = {}
    
    # 출발지와 목적지를 dict형태로 만들기 위해 반복
    for ticket in tickets:
        # 티켓의 출발지(key)가 존재하지 않으면 key와 value를 생성
        # 이때 key는 출발지, value는 도착지가 되며, 다수의 도착지를 고려하여 list로 생성
        if ticket[0] not in route:
            route[ticket[0]] = [ticket[1]]
        # 출발지(key)가 존재할 경우 해당 키에 도착지를 추가
        else:
            route[ticket[0]].append(ticket[1])
    # 알파벳 순서가 앞서는 경로를 선택해야 하며,
    # 스택의 pop을 사용하기 때문에 앞선 순서의 도착지를 먼저 꺼낼 수 있게 내림차순으로 정렬
    for k in route.keys():
        route[k].sort(reverse=True)
    
    # 항상 ICN 공항에서 출발하기 때문에 출발지 지정
    country_list = ['ICN']
    
    # 스택의 값이 존재하지 않을때까지 반복
    while country_list:
        # 현재 위치(마지막에 추가된 출발지) 지정
        country = country_list[-1]
        # 1차 시도에서 발생한 에러를 위한 예외 처리
        try:
            # 현재 위치(country)에서 갈수 있는 도착지가 있는 경우
            if route[country]:
                # 해당 도착지를 꺼내 현재위치에 추가한다.
                country_list.append(route[country].pop())
            # 현재 위치(country)에서 갈수 있는 도착지가 없는 경우
            else:
                # 현재 출발지를 pop해서 answer에 넣어준다.
                answer.append(country_list.pop())
        # KeyError가 발생할 경우(마지막에 방문하는 나라가 key등록이 되어있지 않을때(도착지만 존재))
        except KeyError:
            # 해당하는 나라로 키 생성
            route[country] = []
    
    # 뒤에서 부터 저장됐기 때문에 역순으로 리턴
    return answer[::-1]

if __name__ == '__main__':
    tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    print(solution(tickets)) # answer : ["ICN", "JFK", "HND", "IAD"]
    print(solution(tickets2)) # answer : ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
"""
    뒤늦게 찾아보니 from collections import defaultdict를 사용할경우
    존재하지 않는 key로 접근할때 KeyError가 아닌 default 값을 채워 key를 생성해줌
    
    try-except의 경우 속도가 느린것으로 알고 있어 try-except보다는
    defaultdict 사용이 효율성면에서 더욱 좋을것으로 생각됨
    자세한 내용은 readme 참고
"""