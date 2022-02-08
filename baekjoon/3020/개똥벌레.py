
import sys

# 이분할 탐색
def Binary_Search_Upper(data_list, x):                  #주어진 list에서 x보다 큰 데이터의 개수를 반환; log n 안에 찾음
    left = 0
    right = len(data_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if data_list[mid] <= x:
            left = mid + 1
        else:
            right = mid - 1
    return len(data_list) - (right + 1)   

n, h = map(int, input().split())

down = []
up = []
for i in range(n):
    input_list = sys.stdin.readline().split()
    input_num = int(input_list[0])


    if i % 2 == 0:
        down.append(input_num)
    else:
        up.append(input_num)
down.sort()
up.sort()

min_count = n
range_count = 0


for i in range(1, h + 1):
    down_count = Binary_Search_Upper(down, i - 1)
    top_count =  Binary_Search_Upper(up, h-i)
    now_count = down_count + top_count

    if now_count < min_count:
        min_count = now_count
        range_count = 1
    
    elif now_count == min_count:
        range_count +=1
print(min_count, range_count)