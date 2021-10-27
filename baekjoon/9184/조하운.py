# 신나는 함수 실행

# if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
#     1

# if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
#     w(20, 20, 20)

# if a < b and b < c, then w(a, b, c) returns:
#     w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

# otherwise it returns:
#     w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

import sys

input = sys.stdin.readline

boolean = True

# 메모이제이션 DP

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return (w(20, 20, 20))
    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
        # w(20, 20, 19) + w(20, 19, 19) - w(20, 19, 20)
    # 0이 아니고 이미 연산이 되었을 때 연산된 값 리턴
    else:
        dp[a][b][c] = (w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1))
        return dp[a][b][c]


# 1~20일때 의 결과값 memoization dp array
# [21개의 (0 * 21)]
dp = [[[0]*(21) for _ in range(21)] for _ in range(21)]
# 와 같은 [[0*21]*21] 배열 생성
# while boolean:

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")