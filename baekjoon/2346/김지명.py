n = int(input())
idx = 0
result = []

data = list(map(int, input().split())) # 공백기준 입력받은 값은 map함수로 int화/ [ 3, 2, 1, -3, -1]
index = [x for x in range(1, n + 1)]   #(1, 2, 3, 4, 5)인덱스로 사용할 값을 받아옴

temp = data.pop(idx)  #temp = 3, data = [2, 1, -3, -1]
result.append(index.pop(idx)) #index = [ 2, 3, 4, 5], result =[1]

while data:
    if temp < 0:
        idx = (idx + temp) % len(data)
    else:
        idx = (idx + (temp - 1)) % len(data)
    temp = data.pop(idx)
    result.append(index.pop(idx))

for r in result:

    print(r, end=' ')

