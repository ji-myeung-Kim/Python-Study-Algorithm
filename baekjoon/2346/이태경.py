"""
혼자 힘으로 문제를 해결하지 못했습니다.
스스로에게 '비효율코드' 한표를 던집니다.

알고리즘보단 파이썬 기본 문법이 부족해서
"리스트, 튜플, 맵, 디큐, 이뉴멀레이트" 등등
문법 위주로 일단 공부했습니다~

if __name__ == "__main__":
유일하게 위 코드를 사용해서 '제한조건? 예외처리?'
를 활용하신 재훈님을 효율적인 코드로 선정했습니다.

수요일에 리뷰를 들어볼 수 있었으면 합니다!
(아래는 재훈님의 완성 코드)
"""

from collections import deque

def solution(n, queue):
    answer = []

    while queue:

        val = queue.popleft()
        answer.append(val[0] + 1)

        if queue and val[1] > 0:
            queue.rotate(-(val[1] - 1))
        else:
            queue.rotate(-val[1])

    return ' '.join(map(str, answer))

if __name__ == "__main__":
    n = int(input())

    if 1 <= n <= 1000:
        queue = deque([(index, value) for index, value in enumerate(map(int, input().split()))])

        print(solution(n, queue))
