n = int(input())
balloons = list(zip([i for i in range(1, n+1)], input().strip().split(' ')))
idx = 0
answer = ''
while balloons:
    if len(balloons) == 1:
        target = balloons.pop(0)
        answer += str(target[0])
        break
   
    target = balloons.pop(idx)
    answer += str(target[0]) + ' '
    value = int(target[1])
    if value > 0:
        idx = (idx + value - 1) % len(balloons) 
    elif value < 0:
        idx = (idx + value) % len(balloons)

print(answer) 

# [0,1,2,3,4]
# target = 2 
# [0,1,3,4]
# 2에서 오른쪽으로 5칸 => 3,4,0,1,3 = 인덱스 2 = 인덱스 2-1+5 = 6 
# 2에서 왼쪽으로 5칸 => 1,0,4,3,1 = 인덱스 1 = (2 -5)  
# [0,1,2,3]
# 4에서 오른쪽으로 3칸 => 0,1,2 = 인덱스 2 = 4+3-4-1
# 4에서 왼쪽으로 3칸 => 3,2,1 = 인덱스 1 = 4-3