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