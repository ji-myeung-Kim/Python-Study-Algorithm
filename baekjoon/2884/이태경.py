# h는 시간 m은 분
h, m = map(int, input().split())
# h가 0보다 클 경우
if(h > 0):
    # m이 45분 보다 작을 경우
    if(m < 45):
        h -= 1
        m += 15
    else:
        m -= 45
# h가 0과 같을 경우
elif(h == 0):
    # m이 45분 보다 작을 경우
    if(m < 45):
        h = 23
        m += 15
    else:
        m -= 45
print(h, m)
