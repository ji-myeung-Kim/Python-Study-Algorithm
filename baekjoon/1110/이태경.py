# 백준_while문_더하기 사이클
# https://www.acmicpc.net/problem/1110

n = int(input())        # 새로운 수(68)
num = n
cnt = 0                 # 사이클의 수

while True:             # == while 1:
    a = num // 10       # 68의 몫 == 6
    b = num % 10        # 68의 나머지 == 8
    c = (a + b) % 10    # 6 + 8 = 1"4"
    num = (b * 10) + c  # 80 + 4 = 84

    cnt += 1            # 사이클 수 + 1
    if(num == n):       # num과 n이 같다면(68) 브레이크
        break

print(cnt)
