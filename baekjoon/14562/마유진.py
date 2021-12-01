'''
문제 - 동적계획법
백준 14562 태권왕
https://www.acmicpc.net/problem/14562
'''


from collections import deque

def bfs(S, T):
    q = deque()
    q.append((S, T, 0))
    check = [-1]*(200)
    while q:
        node, t, c = q.popleft()
        if node <= t and check[node] == -1:
            q.append((node*2, t+3, c+1))
            q.append((node+1, t, c+1))
            if node == t:
                return c

C = int(input())
for _ in range(C):
    S, T = map(int, input().split())
    print(bfs(S, T))


'''
풀이
https://jinho-study.tistory.com/1076
B가 200점 이상이 되는 최단경로는 없을 것 같아서 check 리스트 크기를 200으로 정함
'''