'''
프로그래머스 - 조이스틱
https://programmers.co.kr/learn/courses/30/lessons/42860

참고
https://bellog.tistory.com/152
abcdefghijklmnopqrstuvwxyz

JEROEN - 56
JAN - 23
JANA
'''

def solution(name):
    answer = 0
    min_move = len(name) - 1 # for문 안에서만 사용 시 제대로 된 값이 적용되지 않아 여기서 선언
    next = 0

    for i, char in enumerate(name):
        # 조이스틱 상하 방향 횟수 -> Z인 경우는 기본적으로 1번 아래로 내리고 시작하기 때문에 +1을 해준다.
        answer += min(ord(char)-ord('A'), ord('Z')-ord(char)+1)

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        min_move = min(min_move, i + i + len(name) - next)

    # 처음 시도했던 방법 - A 갯수를 카운트해서 길이에서 빼주는 방법 / 75점
    # aNum = name.count('A')
    # answer += min(min_move,len(name)-aNum)
    
    answer += min_move
    return answer

print(solution('JEROEN')) # 56
print(solution('JAN')) # 23
print(solution('AAAAA')) # 0
print(solution('BBBAABB')) # 11
print(solution('BABAB')) # 6
print(solution('JANA')) # 24