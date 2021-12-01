# 유기농 배추 / 실버2 / 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
# https://www.acmicpc.net/problem/1012

# ---------문제해석-----------------------------------------------------------------------
'''
테스트케이스 둘째 줄에 밭의 가로길이, 세로길이, 배추의 갯수가 주어진다 
배추의 위치는 좌표값 (x,y)로 주어진다.
지렁이 하나는 상하좌우의 배추를 커버한다.
    => 해석오류: 인접해있으면 모두 커버한다. 상하좌우는 인접의 기준일 뿐
지렁이의 최솟값을 구한다. 
'''

# ---------접근방법---------------------------------------------------------------------- 
'''
밭을 2차원 배열로 만든다.
스택을 사용해서 [인접한 배추]들을 담고, [인접한 배추]들이 없을 떄(스택이 빌 때) 벌레를 +1 한다.
밭이 여러 개일 수 있으므로, 각 밭의 벌레들을 리스트에 담아뒀다가 마지막에 한 번에 출력한다.
'''

# ----------------------------------------------------------------------------------------

import sys

def Solution(cabbage_list):
    worm = 0
    stack = []
    for i in range(len(cabbage_list)):  # 배추 리스트를 돌면서
        if cabbage_list[i] != 'visited':    
            stack.append(cabbage_list[i])   # 방문하지 않은 배추를 스택에 담고 시작
            cabbage_list[i] = 'visited'

            while stack:
                now = stack.pop()
                direction = 0   # [인접한 배추] count(상하좌우)
                for i in range(len(cabbage_list)):  # [현재 배추]를 기준으로 [인접한 배추]를 찾는다
                    if cabbage_list[i] != 'visited':    
                        if cabbage_list[i] == [now[0]+1, now[1]] or \
                            cabbage_list[i] == [now[0], now[1]+1] or \
                            cabbage_list[i] == [now[0]-1, now[1]] or \
                            cabbage_list[i] == [now[0], now[1]-1]:  
                                stack.append(cabbage_list[i])   # [인접한 배추]를 찾으면 스택에 담고 방문 표시
                                cabbage_list[i] = 'visited' 
                                direction += 1  
                                if direction == 4:  # 상하좌우 4개를 이미 모두 찾았다면, [인접한 배추]를 탐색하는 반복문 강제 종료 
                                    break
            worm += 1
    return worm

routine = 0   # 배추밭(field)의 갯수만큼 반복 
field = sys.maxsize
cabbage_list = []
cabbages = 0
worm_list = []

while routine < field:
    input = list(map(int, sys.stdin.readline().split()))
    if len(input) == 1:
        field = input[0]
        continue
    elif len(input) > 2:
        cabbages = input[2]   # 케이스의 [배추갯수] 데이터를 저장
        continue
    
    cabbage_list.append(input)    # 각 [배추좌표]들을 저장
    if len(cabbage_list) == cabbages:   # [배추좌표]들의 갯수와 [배추갯수]가 같으면 함수실행
        worm_list.append(Solution(cabbage_list))    
        cabbage_list.clear()    # 벌레갯수를 구하고나면 배추좌표 리스트를 비우고, 다음 배추밭 탐색을 준비
        routine += 1

for w in worm_list:
    print(w)            

'''
메모 
- 케이스에 주어진 밭의 가로길이, 세로길이 데이터를 사용하지 않고 있음


예제 입력 1 
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

예제 출력 1 
5
1

예제 입력 2 
1
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0

예제 출력 2 
2
'''


# ---------1차 오답---------------------------------------------------------------------- 



# ----------------------------------------------------------------------------------------




