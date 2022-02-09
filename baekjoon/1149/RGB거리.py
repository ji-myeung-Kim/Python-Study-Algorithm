n = int(input())

dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, len(dp)):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]
print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))
#  
#    [
#       [26, 40, 83], 
#       [49, 60, 57], 
#       [13, 89, 99]
#                     ]        
#     [
        # [26, 40, 83], 
        # [89, 86, 83], 
        # [13, 89, 99]
#                       ]        
#     [
        # [26, 40, 83], 
        # [89, 86, 83], 
        # [96, 172, 139]
#                        ]
