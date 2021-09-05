"""
프로그래머스 LEVEL2 카펫
https://programmers.co.kr/learn/courses/30/lessons/42842

카펫의 넓이 = brown + yellow = width x height
외부 사각형 갯수(brown) = 2w + 2h + 4
내부 사각형 갯수(yellow) = (x-2) * (y-2)
"""

def solution(brown, yellow):
    total = brown + yellow
    # 카펫의 가로길이가 세로길이보다 크거나 같기 때문에 큰수에서 작은수로 반복
    for weight in range(total, 2, -1):
        if total % weight == 0: # 카펫넓이에서 가로길이 탐색
            height = total // weight # 카펫넓이 / 가로길이를 통해 세로길이 탐색
            # 구해진 카펫의 길이에서 테두리길이(2)만큼 빼주고 면적을 구한뒤 yellow의 면적과 같다면 해당 값 return
            if yellow == (weight-2) * (height-2):
                return [weight, height]

# 테스트 케이스
print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
