'''
문제 - BFS, DFS
백준 2178 미로탐색
https://www.acmicpc.net/problem/2178
'''


from collections import deque

n,m = map(int,input().split())
maze = [list(map(int,input())) for _ in range(n)]
dx, dy = [-1,1,0,0], [0,0,-1,1]

def check(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def bfs(a,b):
    if maze[a][b] == 1:
        queue = deque([[a,b]])
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if check(nx,ny):
                    if maze[nx][ny] == 1:
                        maze[nx][ny] += maze[x][y]
                        queue.append([nx,ny])

bfs(0,0)
print(maze[n-1][m-1])


'''
풀이
from collections import deque

n,m = map(int,input().split())
maze = [list(map(int,input())) for _ in range(n)]
dx, dy = [-1,1,0,0], [0,0,-1,1]
    # 상하좌우

def check(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False
        # 바깥 범위에 있는지 확인

def bfs(a,b):
    if maze[a][b] == 1: 
        # 1이면 미방문이라고 판단
        
        queue = deque([[a,b]])
        while queue:
            x,y = queue.popleft()
            for i in range(4): 
                # 상하좌우
                
                nx, ny = x + dx[i], y + dy[i]
                if check(nx,ny): 
                    # 바깥 범위에 있으면 배제
                    
                    if maze[nx][ny] == 1:
                        maze[nx][ny] += maze[x][y] 
                            # 방문하지 않은 곳이라면 1칸 이동할 때 이전 값 더해주기
                        
                        queue.append([nx,ny])

bfs(0,0)
print(maze[n-1][m-1])
'''