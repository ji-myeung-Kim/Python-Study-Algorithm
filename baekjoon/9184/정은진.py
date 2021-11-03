import sys
input = sys.stdin.readline

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if dp[a][b][c]:         # 해당 배열이 존재할 경우
        return dp[a][b][c]  # 기존 값 반환 (같은 연산 반복할 필요 X)

    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return dp[a][b][c]

dp = [[[0 for _ in range(21)] for _ in range (21)] for _ in range(21)]  # 3차원 배열 생성 (원소는 모두 0)

while True:
    a, b, c = map(int, input().split(" "))
    if a == -1 and b == -1 and c == -1: # 문제에서 제시한 조건
        break
    print("w({}, {}, {}) = {}".format(a, b, c, w(a, b, c)))
