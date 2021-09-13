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