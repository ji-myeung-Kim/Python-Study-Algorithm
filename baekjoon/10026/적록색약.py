from collections import deque

# 동서남북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
color_list = [list(map(str, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
q = deque()

count_normal, count_nanshi=  0, 0

def bfs_search(x, y):
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if color_list[nx][ny] == color_list[x][y] and visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = 1

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs_search(i, j)
            count_normal += 1
print(count_normal, end=' ')
# 적록색약일 때
for i in range(n):
    for j in range(n):
        if color_list[i][j] == "R":
            color_list[i][j] = "G"

visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs_search(i, j)
            count_nanshi += 1
print(count_nanshi)
            


