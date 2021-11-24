 
"""
프로그래머스 LEVEL2 조이스틱
https://programmers.co.kr/learn/courses/30/lessons/42860
탐욕법
"""
def solution(name):
    # A를 빼고 Z에서 I를 빼고 최소값(위로 올릴지 아래로 올릴지)
    name_cnt = [min(ord(i)-ord('A'), 1+ord('Z')-ord(i)) for i in name]
    idx = 0
    answer = 0

    while True:
        answer += name_cnt[idx]
        name_cnt[idx] = 0

        if sum(name_cnt) == 0:
            break

        left, right = 1, 1
        while name_cnt[idx - left] == 0:
            left += 1

        while name_cnt[idx + right] == 0:
            right += 1

        answer += left if left < right else right
        idx += -left if left < right else right
            
    return answer

if __name__ == '__main__':
    print(solution("JEROEN"))
    print(solution("JAN"))
    print(solution("AZAAAZ"))
