from collections import deque
import sys
f = sys.stdin.readline

city_count, street_count, path, start_point = map(int, f().split())
graph = [ [] for _ in range(city_count+1)]
visited = [False] * (city_count+1)
distance = [0] * (city_count+1)

for _ in range(street_count):
    a, b = map(int, f().split())
    graph[a].append(b)

def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[now] + 1
                q.append(i)
                if distance[i] == path:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')

bfs(start_point)