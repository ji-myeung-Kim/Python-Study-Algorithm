# 조이스틱 / 탐욕법
# https://programmers.co.kr/learn/courses/30/lessons/42860

# ---------문제 해석---------------------------------------------------------------------- 
# 조이스틱 조작(상하좌우)횟수의 최솟값을 구해야 한다
# 좌우는 [가로조작], 상하는 알파벳 [세로조작]

# 이름에 A가 들어갈 경우 바꿀 필요가 없음  ->  [가로조작] 최솟값 계산 할 때 주의한다 
# [세로조작]시 알파벳이 오름차순 또는 내림차순으로 변경 -> 어떤 방식으로 알파벳을 전환할 것인가 
# 알파벳 m, o 처럼 가운데 쯤에 위치한 경우, 조이스틱을 위로 조작할지 아래로 조작할지 최솟값을 계산한다

# 첫 커서의 위치는 자유?  ->  조건 없음 
# 첫 커서의 위치조건이 없다면, [가로조작]을 최소화하기 위해, 어떤 문자에서 시작할 것인지 고려해야 한다
# ex) ACDAAAB가 주어졌을 떄, C에서 시작하는 것보다 D에서 시작하는 것이 최소 이동 

# ---------접근 방법----------------------------------------------------------------------
# name의 글자마자 A~Z 26의 길이를 가진 문자열을 각각 생성하여 인덱스값을 활용해 본다
# [세로조작]의 최솟값은 문자열 길이의 중간값을 기준으로 위로 조작할 지, 아래로 조작할 지 결정한다
# [가로조작]의 최솟값은 현재 위치의 [세로조작]이 끝난 상태에서, A가 아닌 글자의 위치가 왼쪽이 가까운 지 오른쪽이 가까운 지 계산한다
# 첫 커서의 위치 정하기 - 주어진 name을 순환하면서 A가 아닌 것들을 탐색하고, 탐색이 끝날 때까지의 시간(길이)을 각 인덱스마다 측정해 본다 

# ---------1차 오답---------------------------------------------------------------------- 
# 첫 커서 위치를 첫 번째 문자로 고정하지 않음  => 제약조건 없는데..?
# ABAAAAAABA의 경우 - 순방향으로 진행하다 다시 역방향으로 돌아오는게 더 빠름 
# => 한 쪽 방향으로 고정하지 않고, 탐욕법을 적용하여 매 순간 최솟값 측정 필요 

# ---------접근 방법2----------------------------------------------------------------------
# 1. 첫 커서 위치에서 순방향, 역방향을 측정한 뒤, 최솟값 지점으로 이동
# 2. 최솟값 지점에서 다시 순방향, 역방향을 측정하여 최종 최솟값 산출

# ----------------------------------------------------------------------------------------

name1 = "JEROEN"
name2 = "JAN"
name3 = "ABAAAAAABA"  

def solution(name):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    
    vertical = 0
    horizon = 0
    non_A = len(name) - name.count("A") 

    if non_A != 0:
        count = 0
        start = 0
        while count != non_A:
            if start == 0:
                for i in range(len(name)):
                    if name[i] != "A":
                        count += 1
                        name[i] = "A"
                        if i != 0:
                            horizon, start = i
                            break
            else:
                forward = 0
                f_check
                backward = 0
                b_check
                for i in range(start+1, len(name)):
                    if name[i] != "A":
                        f_check = name[i]
                        forward = i - start
                        break
                
                name_reverse = name[ :start+1] + name[ :start][::-1] + name[start+1: ][::-1]
                for i in range(start+1,len(name)):
                    if name_reverse[i] != "A":
                        b_check = name_reverse[i]
                        backward = i - start

                if forward <= backward:
                    f_check = "A"
                    horizon += forward
                else:
                    b_check = "A"
                    horizon += backward

        for n in name:
            if alphabet.index(n) > len(alphabet)/2:
                vertical += len(alphabet) - alphabet.index(n)
            else:
                vertical += alphabet.index(n)

    return vertical + horizon


# print(solution(name1))
# print(solution(name2))
print(solution(name3))

# ---------1차 오답---------------------------------------------------------------------- 
# [가로조작]이 순방향 or 역방향 중 한 방향으로만 진행하고 있음 
# => 진행하다 되돌아오는 케이스 추가 필요

# ---------------------------------------------------------------------------------------

'''
name1 = "JEROEN"
name2 = "JAN"
name3 = "ACDAAAB"  

def solution(name):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"      # A부터 N까지의 거리는 순방향, 역방향 모두 13(기준점) => B~M은 순방향, O~Z는 역방향이 최소거리
    pivot = len(alphabet)/2     # 13 = N까지의 거리 
    vertical = 0
    horizon = 0
    non_A = len(name) - name.count("A")    # 주어진 name에서 A가 아닌 문자열 갯수 측정

 # ========= [가로조작] =========
    if non_A != 0:       
        horizon = 20    # [가로조작]의 최댓값 설정 
        for i in range(len(name)):      # name을 순환하면서 첫 커서를 놓는다(커서위치=i) ----> 커서가 첫 글자로 고정되지 않고, name의 모든 글자를 시작위치로 설정해보면서 최솟값을 산출한다 
            name_double = name*2      
            count = 0
            for j in range(i, len(name_double)):     
                                        # 커서위치 i 를 기준으로 [name전체를] 순방향, 역방향 모두 순환할 수 있게 name_double을 대상으로 삼음 
                                        # name이 "ABAACA"인 경우 첫 커서 위치가 C라면, 마지막 A를 지나 다시 첫 번째 A로 돌아오는 방법으로 name_double을 생성 
                                        # ex) 로직은 ABAA[CA ABAA]CA 에서 대괄호 부분만 계산하고 종료된다
                                        # 역방향의 경우, B에서 역방향으로 C까지 도달하는 거리는, C에서 순방향으로 B에 도달하는 거리와 동일하다. ----> name을 뒤집어 계산할 필요 없음 
                                        # ex) AB]AA[CA = ABAA[CA AB]AACA
                                                      
                if name_double[j] != "A":
                    count += 1       
                    if count == non_A:        # A가 아닌 문자열(non_A)을 측정한 갯수가, 주어진 name의 것과 같으면 반복문 탈출 
                        if horizon > j-i:     # j는 시작커서i 에서 모든 non_A가 측정된 때의 거리 
                            horizon = j-i             
                        break                 # => name의 모든 글자를 순환하면서, 가장 짧은 거리를 horizon에 담게 된다 =======> ※ 진행하다 돌아오는 케이스 상정하지 않았을 경우임!
                                                    
 # ========= [세로조작] =========
    for n in name:       
        if alphabet.index(n) > pivot:
            vertical += len(alphabet) - alphabet.index(n)
        else:
            vertical += alphabet.index(n)

    return vertical + horizon


print(solution(name1))
print(solution(name2))
print(solution(name3))
'''