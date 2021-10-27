'''
백준 11729 하노이 탑 이동 순서
https://www.acmicpc.net/problem/11729

이해를 위한 참고 : https://shoark7.github.io/programming/algorithm/tower-of-hanoi
hanoi(N)은 그림을 그려보면 2번의 hanoi(N-1) 과정을 수반한다.
'''

# N : 첫번째 장대에 쌓인 원판의 개수
# start : 시작 장대
# to : 목표 장대
# via : 경유 장대
N = int(input())

def hanoi(N, start, to, via):
    
    # 원판이 1개라면 바로 시작 -> 목표 장대 출력
    if N == 1:
        print(start, to)

    else:
        # 원판 N-1개를 시작 -> 경유 장대로 이동
        hanoi(N-1, start, via, to)
        # 가장 큰 원반을 목표 장대로 이동
        print(start, to)
        # 원판 N-1개를 경유 -> 목표 장대로 이동
        hanoi(N-1, via, to, start)

# 하노이 탑 경우의 수 계산 식
print(2**N-1)
hanoi(N,1,3,2)