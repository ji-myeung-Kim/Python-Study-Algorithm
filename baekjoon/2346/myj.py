'''
문제 - 스택과 큐
백준 2346 풍선 터뜨리기
https://www.acmicpc.net/problem/2346
'''


n = int(input())
idx = 0
result = []

data = list(map(int, input().split()))  
index = [x for x in range(1, n + 1)]

temp = data.pop(idx)
result.append(index.pop(idx))

while data:
    if temp < 0:
        idx = (idx + temp) % len(data)
    else:
        idx = (idx + (temp - 1)) % len(data)
    temp = data.pop(idx)
    result.append(index.pop(idx))

for r in result:
    print(r, end=' ')


'''
풀이
data = list(map(int, input().split()))  
    # input().split()로 값을 여러개 입력받고
    # 그 값들을 map함수 이용해서 int 타입으로 한번에 변형 후 배열로 만들기
    # [3, 2, 1, -3, -1]

index = [x for x in range(1, n + 1)]
    # 인덱스로 사용할 값(1, 2, 3, 4, 5) 하나씩 받아서 배열로 만들기

temp = data.pop(idx)
    # data에서 값을 pop으로 앞에서부터 하나씩 뽑아서 temp에 넣기
    # temp = 3, data = [2, 1, -3, -1]

result.append(index.pop(idx))
    # 위에서 뽑은 값의 인덱스 값을 결과에 하나씩 쌓기
    # result =[1], index = [2, 3, 4, 5]
    
while data:
    if temp < 0:
        idx = (idx + temp) % len(data)
            # temp가 0보다 작으면 == 왼쪽으로 몇번째
            # idx와 temp를 더한 값을 data의 길이로 나눈 후 나머지 값을 idx에 넣기
            
    else:
        idx = (idx + (temp - 1)) % len(data)
            # temp가 0보다 작지 않으면 == 오른쪽으로 몇번째
            # idx와 temp-1을 더한 값을 data의 길이로 나눈 후 나머지 값을 idx에 넣기


알고 가자
map : 리스트의 요소를 지정된 함수로 처리해주는 함수. 
      원본 리스트를 변경하지 않고 새 리스트를 생성
      리스트뿐만 아니라 모든 반복 가능한 객체를 넣기 가능
'''
