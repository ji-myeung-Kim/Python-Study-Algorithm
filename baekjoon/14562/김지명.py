    from collections import deque

def bfs(S, T):
    q = deque()
    q.append((S, T, 0))
    check = [-1] * 200
    while q:
        node, t, c = q.popleft()
        #내가때린게 맞은거보다 더 작을동안
        if node <= t and check[node] == -1 :
            # 내가 맞은거 *2, 타격+3 발차기횟수 + 1
            q.append((node*2, t+3, c+1))
            # 내가 맞은거 +1, 발차기횟수 + 1
            q.append((node+1, t, c+1))
            if node == t:
                return c

C = int(input())
for _ in range(C):
    S,T = map(int, input().split())
    print(bfs(S,T))
