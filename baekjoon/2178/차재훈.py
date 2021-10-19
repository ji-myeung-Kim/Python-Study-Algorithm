"""
https://www.acmicpc.net/problem/2178
백준 2178 - 미로탐색
BFS
"""

from collections import deque
import sys

def solution(x, y):
    queue = deque([(x,y)])
    
    while queue:
        x, y = queue.popleft() # 현재 위치한 x, y 좌표
        
        # 현재 위치에서 네방향으로의 위치 확인
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
        
            # 미로 찾기 공간을 벗어난 경우 무시
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                continue
            # 벽인 경우 무시
            if maze[next_x][next_y] == 0:
                continue
            # 해당 위치를 처음 방문한 경우 거리 기록
            if maze[next_x][next_y] == 1:
                maze[next_x][next_y] = maze[x][y] + 1
                queue.append((next_x, next_y))
    return maze[N - 1][M -1]

if __name__ == "__main__":
    N, M = map(int, input().split())
    # 문제에 맞는 제한 조건 설정(2 ≤ N, M ≤  100)
    if 2 <= N <= 100 and 2 <= M <= 100:
        maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
        # 상, 하, 좌, 우 방향 정의
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        print(solution(0, 0))
