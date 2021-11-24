'''
문제 - 동적계획법
프로그래머스 조이스틱
https://programmers.co.kr/learn/courses/30/lessons/42860
'''


def solution(name):
    moves = [min(ord(s) - ord('A'), ord('Z') - ord(s) + 1) for s in name]

    pos = 0
    answer = 0
    while True:
        answer += moves[pos]
        moves[pos] = 0

        if sum(moves) == 0:
            break

        left, right = 1, 1

        while moves[pos - left] == 0:
            left += 1

        while moves[pos + right] == 0:
            right += 1

        if left >= right:
            pos += right
            answer += right
        else:
            pos -= left
            answer += left

    return answer


'''
풀이
def solution(name):  
    moves = [min(ord(s) - ord('A'), ord('Z') - ord(s) + 1) for s in name]
        # 65~90(A~Z)
        # 상하 조정으로 알파벳 바꾸기 

    pos = 0
    answer = 0
    while True:
        answer += moves[pos]
            # 모든 target 문자에 대해 A로부터의 거리와 Z로부터의 거리 중 작은 값 저장
            
        moves[pos] = 0

        if sum(moves) == 0:
            break
                # target문자 A일 경우 변환 필요없으므로 값 0 넣어줌

        left, right = 1, 1
            # 좌우 이동방향을 정하기

        while moves[pos - left] == 0:
            left += 1

        while moves[pos + right] == 0:
            right += 1
                # left, right 각각 1씩 늘려가며 target 문자 A가 아닌 문자에 먼저 도달하는 경우 찾기

        if left >= right:
            pos += right
            answer += right
        else:
            pos -= left
            answer += left
                # left, right 중 더 짧은 거리의 위치로 이동하여 반복

    return answer
'''