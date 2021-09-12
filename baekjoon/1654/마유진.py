'''
문제 - 이분탐색
백준 1654 랜선 자르기
https://www.acmicpc.net/problem/1654
'''


k, n = map(int, input().split())
lengths = [int(input()) for _ in range(k)]

min = 1;
max = max(lengths)
result = 0

while(min <= max):
    mid = (min + max) // 2
    cut = 0
    for length in lengths:
        cut += length // mid
        
    if(cut >= n):
        result = mid
        min = mid length + 1
    elif(cut < n):
        max = mid - 1
print(result)


'''
풀이
k, n = map(int, input().split())
    # 이미 가지고 있는 랜선의 개수 k, 그리고 필요한 랜선의 개수 n
    # input에 들어온 값을 정수로 받아서 k와 n에 하나씩 넣는다.
    
lengths = [int(input()) for _ in range(k)]
    # 랜선의 길이는 k의 범위 동안 input으로 들어온 값을 정수로 변환한 값

min = 1
max = max(lengths)
result = 0
    # 랜선의 최솟값 min은 1, 최댓값 max는 랜선 길이의 max 값, 결과는 0으로 초기화

while(min <= max):
    mid = (min + max) // 2
    cut = 0
        # 랜선의 최소가 최대 이하일 때,
        # min과 max를 더한 값을 2로 나누고 소수점 이하의 수를 버린 값을 mid로 설정
        # 자른 횟수는 0으로 초기화
    
    for length in lengths:
        cut += length // mid
            # 랜선의 길이를 계속 자를 동안,
            # 자른 횟수는 랜선을 mid로 자르고 소수점 이하의 수를 버린 값을 더하기
            
    if(cut >= n):
        result = mid
        min = mid + 1
            # 만약 자른 횟수가 n 이상이면, (랜선 개수가 n개 이상)
            # mid가 결과 (더 자를 필요 없음)
            # min은 mid 다음값
        
    elif(cut < n):
        max = mid - 1
            # 자른 횟수가 n 미만이면, (랜선 개수가 부족)
            # max는 mid 앞의 값 & 다시 자르기 (mid 이상의 값은 조건에 맞지 않음)
            
print(result)


알고 가자
k, n = map(int, input().split())
input() : 입력 받은 내용을 문자열로 인식
input().split() : input으로 입력받은 문자열을 띄어쓰기(기본) 기준으로 분리
map(int, input().split()) : 분리된 값을 정수로 인식해서 map에 담음
참고 : https://ccamppak.tistory.com/38

for _ in range(k)
_는 실제로 코드에서 사용되지 않는 변수를 의미함
의미 없는 값으로 반복하는 횟수만 진행할 때 사용함
'''