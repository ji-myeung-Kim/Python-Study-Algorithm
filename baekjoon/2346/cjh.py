"""
https://www.acmicpc.net/problem/2346
백준 2346 - 풍선터뜨리기
스택/큐
"""

from collections import deque

def solution(n, queue):
    # 풍선이 터진 순서를 담아둘 리스트 변수 선언
    answer = []

    while queue:

        # queue의 첫번째 요소를 pop
        val = queue.popleft()
        # pop 한 첫번째 요소의 인덱스값 에 +1 하여 answer에 삽입
        answer.append(val[0]+1)
            
        if queue and val[1] > 0:
            # queue에 값이 존재하고 val[1](풍선의 값)이 양수일때 해당 값 만큼 queue를 회전
            queue.rotate(-(val[1]-1))
        else:
            # val[1](풍선의 값)이 음수 일때 해당 값 만큼 회전
            queue.rotate(-val[1])

    # 리스트의 요소를 띄어쓰기 형태로 리턴
    return ' '.join(map(str, answer))

if __name__ == "__main__":
    # 입력값
    n = int(input())
    
    # 문제에 맞는 제한 조건 설정(1 ≤ N ≤ 1,000)
    if 1 <= n <= 1000:
        # 풍선에 적혀 있는 값을 입력받고 띄어쓰기 기준으로 split하고 요소를 map을 통해 int로 형변환 한뒤 enumerate로 index값과 value를 튜플형태로 deque형태로 변수에 저장한다.
        queue = deque([(index, value) for index, value in enumerate(map(int, input().split()))])

        print(solution(n, queue))