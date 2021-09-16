'''
## 실패 - 런타임에러(ValueError) ##

import sys

k, n = map(int, input().strip().split())
arr = []
for i in range(k):
    arr.append(int(sys.stdin.readline()))

# 만들수 있는 최소길이: 1 / 최대길이: 주어진 랜선들 중 가장짧은것
left = 1
right = min(arr)
while left <= right:
    mid = (left + right) // 2
    
    # mid 길이로 랜선 나눠서 몇개 나오는지 count 변수에 담기
    count = 0
    for lan in arr:
        count += lan // mid
    
    # 나눠진 조각이 원하는 조각 수가 맞는지 확인
    if count < n:
        right = mid - 1
    if count > n:  
        left = mid + 1
    if count == n:  
        break
    
print(mid)
'''

## 수정한 코드 ##

import sys

k, n = map(int, input().strip().split())
arr = []
for i in range(k):
    arr.append(int(sys.stdin.readline()))

# 만들 수 있는 랜선 가장 짧은길이 : 1 / 가장 긴 길이 : 주어진 랜선중 가장 !!긴 것!! (n==1인 경우)
left = 1
right = max(arr)
while left <= right:
    mid = (left + right) // 2
    # mid 길이로 랜선 나눠서 몇개 나오는지 count 변수에 담기
    count = 0
    for lan in arr:
        count += lan // mid   

    # 만들어진 랜선 개수가 원하는 개수보다 크거나 같을때 (count == n일때가 분기점)
    if count >= n:
        left = mid + 1
    else:
        right = mid - 1

print(right) # right를 출력하는 이유가 명확히 이해안갑니다. 도와주세요.

# 깨달음. 무조건 while 마지막 루프 돌때 else블럭에서 right = mid-1 하고 끝나게 되기 때문이다!!
# 왜냐면 랜선 길이가.. 예를들어 198일때도 11조각 나오긴 하기 때문에 count >= n 에 걸려서 left = mid + 1됨 (=> 가능한 최대 길이를 향해 감)
# 그러다가 mid값이 딱 11조각에서 10조각 나올 값이 되는순간 else블럭에 걸리는데 그때 그 값이 정답 +1인 값이므로
# else블럭에 의해 -1해주고 더이상 while문 돌지않고 출력하면됨
# ^ㅇ^.. 이해가..되시나요...?
