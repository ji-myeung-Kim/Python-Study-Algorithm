#### 최단경로찾기: BFS 이용 (같은 레벨의 모든 원소 탐색 후 다음 레벨로 이동) ####

n, m = map(int, input().strip().split(' '))
maze = []
for i in range(n):
    maze.append(list(input().strip())) 

def solution(maze, n, m):
    queue = [(0,0)]  # 현시점에서 이동할 수 있는 좌표 담아두는 큐
    maze[0][0] = '2'  # (0,0) 지점 방문했음으로 표시
    answer = 1
    while queue:
        for i in range(len(queue)):  # 현재 시점에서 이동할 수 있는 좌표 개수만큼 반복
            now = queue.pop(0) # pop(0)으로 먼저 들어가있는 원소를 i번 꺼내야 같은 레벨상의 좌표를 다 탐색할 수 있음 
            
            # 종료조건
            if now == (n-1, m-1):
                return answer

            x = now[1]  # now의 가로 좌표
            y = now[0]  # now의 세로 좌표     
            # 왼쪽으로 이동할 수 있다면
            if x > 0 and maze[y][x-1] == '1':
                queue.append((y, x-1))  # 이동할 수 있는 좌표라면 큐에 담음
                maze[y][x-1] = '2'  # 이미 방문한 위치임을 표시
            # 오른쪽으로 이동할 수 있다면
            if x < m-1 and maze[y][x+1] == '1':
                queue.append((y, x+1))
                maze[y][x+1] = '2'
            # 위쪽으로 이동할 수 있다면
            if y > 0 and maze[y-1][x] == '1':
                queue.append((y-1, x))
                maze[y-1][x] = '2'
            # 아래쪽으로 이동할 수 있다면
            if y < n-1 and maze[y+1][x] == '1':
                queue.append((y+1, x))
                maze[y+1][x] = '2'
        
        # 동일 거리선상의 좌표들에 대해 탐색 완료 -> 다음 거리로 이동
        answer += 1
    return answer

print(solution(maze, n, m))