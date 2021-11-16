from collections import deque

def bfs(S, T):
    q = deque()
    q.append((S, T, 0))
    while q:
        hit, hurt, cnt = q.popleft()
        #내가때린게 맞은거보다 더 작을동안
        if hit <= hurt  :
            # 내가 맞은거 *2, 타격+3 발차기횟수 + 1
            q.append((hit*2, hurt+3, cnt+1))
            # 내가 맞은거 +1, 발차기횟수 + 1
            print(q, " doubleattack" )
            q.append((hit+1, hurt, cnt+1))
            print(q, "singleattack")

            if hit == hurt:
                return cnt

C = int(input())
for _ in range(C):
    S,T = map(int, input().split())
    print(bfs(S,T))

# 10 20
# 20 23
# 21
# 22
# 23
# 15 62
# 30 65
# 60 68

