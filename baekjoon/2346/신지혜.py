'''
백준 2346 - 풍선 터뜨리기 (스택/큐)
https://www.acmicpc.net/problem/2346

예시 입력
5
3 2 1 -3 -1

예시 출력
1 4 5 3 2
'''

from collections import deque

# 풍선 갯수 입력
n = int(input())
# 풍선에 적혀 있는 값 받음 -> 공백 기준 값 쪼개기 -> map을 통해 int 변환 -> enumarate 사용해 (idx,val) 튜플 변환 뒤 deque 저장
# deque 사용 이유 -> 실행 속도 : list를 사용하면 pop 뒤, 정렬을 해야해서 시간복잡도가 O(n)인 반면, deque는 삭제연산이 O(1))
deque_n = deque(enumerate(map(int, input().split()), start=1))
answer = []

while deque_n:

    # 가장 앞 요소를 pop하여 idx는 answer list에 추가
    val = deque_n.popleft()
    answer.append(val[0])
            
    # (idx, val)에서 val의 음/양수값에 따라 rotate 구분
    if deque_n and val[1] > 0:
        deque_n.rotate(-(val[1]-1))

    else :
        deque_n.rotate(-val[1])

# 완성된 answer list를 map을 통해 str으로 변환 후, 공백으로 join해 출력한다.
print(' '.join(map(str,answer)))
