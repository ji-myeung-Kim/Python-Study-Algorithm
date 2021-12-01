## 1차시도 - 제출하기도 전에 잘못됐다는걸 깨달음 ##
'''
import sys
input = sys.stdin.readline

n = int(input())
time = []
pay = []
for i in range(n):
    t, p = map(int, input().strip().split())
    time.append(t)
    pay.append(p)

dp = []

for i in range(0, n):  
    j = i
    value = 0
    while True:       
        if j+time[j] <= n:                
            value += pay[j]
            j += time[j]
            if j > n-1:
                break
        else:
            break 

    dp.append(value)
     
print(max(dp)) 
'''

# 반례
# time = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
# pay = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50]
# 50 + 10 + 30 선택해야 하는데 위 코드대로라면 50 + 10 + 20 선택해버림



## 2차시도 - 구글링.. ##

# 각 날짜의 상담마다 소요시간이 다르다. 며칠 후에 시작할 수 있을지 알 수 없다 
# => 퇴사일에 가까운 순으로 뒤에서부터 계산한다
# n일에 상담을 한 후 그 소요기간동안의 다른 상담들을 포기하고 n+T[n]일에 다시 상담을 하는 것이 나은지, 
# 아니면 n일에 상담을 하지 않는 것이 나은지 (이 경우 직전 반복에서 구해놓은 n+1일~퇴사일까지의 상담 스케줄을 선택하게 된다)
# 둘을 비교해서 최댓값을 저장해나간다
import sys
input = sys.stdin.readline

n = int(input())
time = []
pay = []
for _ in range(n):
    t, p = map(int, input().strip().split())
    time.append(t)
    pay.append(p)

dp = [0]*(n+1)   
for i in range(n-1, -1, -1):  # 퇴사 D-1일 ~ 0일 순으로 거꾸로 탐색
    
    # i일에 하는 상담이 퇴사일을 넘기면 상담을 하지 않음
    if i+time[i] > n:  
        dp[i] = dp[i+1]
        
    # i일에 상담을 하고 i+time[i]일 후에 또다른 상담을 하는것 or i일에 상담을 안하고 그냥 i+1일부터의 스케줄을 선택하는 것 중 큰 금액을 선택 
    else:
        dp[i] = max( pay[i]+dp[i+time[i]], dp[i+1] )  
    
print(dp[0])  # 0일부터 퇴사 D-1일까지 모두 탐색한 결과인 dp[0] 반환 