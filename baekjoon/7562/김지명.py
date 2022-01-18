from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
"""
sx = 0
sy = 0
ax = 7
ay = 0
"""
def bfs(sx, sy, ax, ay):
    q = deque()
    q.append([sx, sy])
    # deque q = ([[0, 0]])
    s[sx][sy] = 1
    while q:
        # a = 0, b = 0
        a, b = q.popleft()
        if a == ax and b == ay:
            print("answer ", s[ax][ay] -1)
            """
            [
                
                [1, 4, 3, 4, 3, 4, 5, 6], 
                [4, 5, 2, 3, 4, 5, 4, 5], 
                [3, 2, 5, 4, 3, 4, 5, 6], 
                [4, 3, 4, 3, 4, 5, 4, 5], 
                [3, 4, 3, 4, 5, 4, 5, 6], 
                [4, 5, 4, 5, 4, 5, 6, 5], 
                [5, 4, 5, 4, 5, 6, 5, 6], 
                [6, 5, 6, 5, 6, 5, 6, 0]
                                            ]
            """
            print(s)
            return
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and s[x][y] == 0:
                q.append([x, y])
                s[x][y] = s[a][b] + 1
t = int(input())
for i in range(t):
    n = int(input())
    # sx, sy = 0, 0
    sx, sy = map(int, input().split())
    # ax, ay = 7, 0
    ax, ay = map(int, input().split())
    """
    [
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0,]
    ]
    """
    s = [[0] * n for i in range(n)]
    bfs(sx, sy, ax, ay)
