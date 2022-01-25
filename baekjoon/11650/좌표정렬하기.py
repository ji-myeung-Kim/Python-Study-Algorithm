import sys
input = sys.stdin.readline

n = int(input())

array = []
for i in range(n):
    [a, b] = map(int, input().split())
    array.append([a, b])

"""
[
    [1, -1], 
    [1, 1], 
    [2, 2], 
    [3, 3], 
    [3, 4]
             ] 
    로 정렬 시키기
"""
sorted_array = sorted(array)

for  i in range(n):
    # 첫번째 인덱스0인 첫번째 값출력(1, )(1, )(2, )(3, )(4, )
    # 두번째 인덱스1인 값 출력(, -1)(, 1)(, 2)(, 3)(, 4)
    # >>>     1 -1
            # 1 1
            # 2 2
            # 3 3
            # 3 4
    print(sorted_array[i][0], sorted_array[i][1])