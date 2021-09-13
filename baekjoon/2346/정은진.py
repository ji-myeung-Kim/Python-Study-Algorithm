N = int(input())

list_N = list(map(int, input().split()))
list_index = []
result = []

for i in range(1, N + 1):
    list_index.append(i)

idx = 0
k = list_N.pop(idx)  # k 는 풍선 속 숫자
result.append(list_index.pop(idx))

while (len(list_N) > 0):

    if (k < 0):
        idx = (idx + k) % len(list_N)
    else:
        idx = (idx + (k - 1)) % len(list_N)

    k = list_N.pop(idx)
    result.append(list_index.pop(idx))

for j in range(N):
    print(result[j], end=" ")
