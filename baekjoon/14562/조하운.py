import sys
from collections import deque

input = sys.stdin.readline

# A는 현재 점수만큼 점수를 얻을 수 있는 엄청난 연속 발차기이다. 하지만 상대 역시 3점을 득점하는 위험이 있다.
# B는 1점을 얻는 연속 발차기이다.
def bfs(S, T, cnt):
    queue = deque()
    queue.append((S, T, cnt))
    
    while queue:
        A, B, C = queue.popleft()
        if A <= B:
            queue.append(((A*2), B+3, C+1))
            queue.append(((A+1), B, C+1))
            if A == B:
                return C
                
C = int(input())

for i in range(C):
    S, T = map(int, input().split())
    cnt = 0

    print(bfs(S,T, cnt))


