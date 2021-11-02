import sys

input = sys.stdin.readline

N = int(input())

# dic = {}
dp = [0 for _ in range(N+1)] #0 번째 dummy data
# [[],[],[],[],[],[],[]]
day = []


for i in range(N):
    day.append(list(map(int, input().split())))

# [[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]]

# value[0] + key 가 다음 가능한 날
# 특정 날에서 시작했을 때 
for i in range(N):
    # 다음날 = 
    dp[i + 1] = max(dp[i + 1], dp[i])

    # 현재 위치에사 다음 가능한 위치가 N보다 작거나 같을 떄
    # dp에 기록이 없다면 저장, 더 높은 합이 있다면 update
    if i + day[i][0] <= N:      
        dp[i + day[i][0]] = max(dp[i + day[i][0]], dp[i] + day[i][1])
    
    print(dp)

# [0, 0, 0, 10, 0, 0, 0, 0]
# [0, 0, 0, 10, 0, 0, 20, 0]
# [0, 0, 0, 10, 0, 0, 20, 0]
# [0, 0, 0, 10, 30, 0, 20, 0]
# [0, 0, 0, 10, 30, 30, 45, 0]
# [0, 0, 0, 10, 30, 30, 45, 0]
# [0, 0, 0, 10, 30, 30, 45, 45]
# [0, 0, 0, 10, 30, 30, 45, 45]
print(dp[-1])