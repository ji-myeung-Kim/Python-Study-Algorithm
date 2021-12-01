import sys
import math

input = sys.stdin.readline

N = int(input())

# Greedy 풀이

# ans = 0

# while N >= 0:
#     if N % 5 == 0:
#         ans += (N // 5)
#         print(ans)
#         break
#     N -= 3
#     ans += 1

# else:
#     print(-1)


# DP 풀이

arr = [math.inf] * (N+1)
# 인덱스는 0부터 시작이기 때문에 N + 1까지 
# n개의 설탕은 최소 몇개의 봉지로 담을 수 있는지 기록
# 3과 5는 1개로 지정
# 3보다 적은 수는 담을 수 없기 때문에 inf 유지
arr[3] = arr[5] = 1


# 반복문은 5는 봉지 1개로 확정이며 다음 개수인 6부터 반복문 시작
for i in range(6, N+1):
    # 이전 단계중 3과 5가 담겨진 위치에서의 최소값에서 1을 더함
    arr[i] = min(arr[i-3], arr[i-5]) + 1

if arr[N] < math.inf:
    print(arr[N])
else:
    print(-1)

# print(arr[N] if arr[N] < 5001 else -1)
