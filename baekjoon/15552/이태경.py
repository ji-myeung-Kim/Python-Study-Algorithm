import sys  # sys 모듈 불러오기(이거 때문에 헤맴)
t = int(sys.stdin.readline())   # input = sys.stdin.readline
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
