'''
문제 - BFS, DFS
프로그래머스 여행 경로
https://programmers.co.kr/learn/courses/30/lessons/43164
'''


def solution(tickets):
    routes = dict()

    for (start, end) in tickets:
        routes[start] = routes.get(start, []) + [end]  

    for r in routes.keys():
        routes[r].sort(reverse=True)

    stack = ["ICN"]
    path = []
    
    while stack:
        top = stack[-1]

        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    
    answer = path[::-1]
    return answer


'''
풀이
def solution(tickets):
    routes = dict()
        # 주어진 티켓들을 dictionary 형식으로 저장

    for (start, end) in tickets:
        routes[start] = routes.get(start, []) + [end]
            # 출발 - 도착 순으로 정렬

    for r in routes.keys():
        routes[r].sort(reverse=True)
            # key값마다 시작점 - 끝점 역순으로 정렬

    stack = ["ICN"]
    path = []
        # 첫번째 출발지 ICN을 기준으로 스택 쌓기
    
    while stack:
        top = stack[-1]
            # 스택의 top부터 하나씩 확인
            # answer에 담겨질 때는 start에 값이 꽉차고 routes에 값이 없을 때이므로
            # answer에는 반대로 값이 들어가 있음

        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
                # 현재 routes에서 now가 가장 마지막으로, 더 이상 갈 도착지 없으면
                # answer에 마지막 지점부터 pop해서 넣음
                
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
                # now에서 더 갈 곳이 있으면
                # 도착지를 stack에 담기
    
    answer = path[::-1]
    return answer
        # 만든 path를 역순으로(출발지-도착지 순으로) 출력
'''