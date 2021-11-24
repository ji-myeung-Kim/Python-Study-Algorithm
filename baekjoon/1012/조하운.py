import sys

input = sys.stdin.readline

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < M):
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dfs(nx, ny)

T = int(input())
# T = 1
for _ in range(T):
    M, N, K = map(int, input().split())
    # M, N, K = 10, 8, 17

    cnt = 0

    graph = [[0] * M for _ in range(N)]
    # print(graph)
    # graph = [
    #     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
    #     [0, 0, 1, 1, 0, 0, 0, 1, 1, 1], 
    #     [0, 0, 0, 0, 1, 0, 0, 1, 1, 1], 
    #     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # ]

    for _ in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                dfs(i, j)
                cnt += 1

    print(cnt)


