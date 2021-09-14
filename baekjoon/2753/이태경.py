year = int(input())
# 파이썬에서는 && 대신에 and, || 대신에 or을 쓰네!?
if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    print(1)
else:
    print(0)
