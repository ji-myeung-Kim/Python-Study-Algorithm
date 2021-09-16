import sys
K, N = map(int, input().split()) #첫줄 공백을 기준으로 k와n에 대입
arr1 = [int(sys.stdin.readline()) for _ in range(K)]   #한줄 한줄 읽어와 arr1에 넣어준다
start, last = 1, max(arr1) #이분탐색 처음과 끝위치

while start <= last: 
    mid = (start + last) // 2 #중간 위치
    lines = 0 #랜선 수
    for i in arr1:
        lines += i // mid #분할 된 랜선 수
        
    if lines >= N: #랜선의 수가 입력된N 개수보다 많으면 수를 크게함으로써 수를 줄여준다
        start = mid + 1
    else:           ##랜선의 수가 입력된N 개수보다 적으면 수를 작게함으로써 수를 늘려준다
        last = mid - 1
print(last)