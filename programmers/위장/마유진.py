'''
문제 - 해시
프로그래머스 위장
https://programmers.co.kr/learn/courses/30/lessons/42578
'''


def solution(clothes):
    answer = {}
    
    for i in clothes:
        if i[1] in answer:
            answer[i[1]] += 1
        else:
            answer[i[1]] = 1

    cnt = 1
    for i in answer.values():
        cnt *= (i+1)
    return cnt - 1


'''
풀이
def solution(clothes):
    answer = {}
        # 딕셔너리 형태 만들기
    
    for i in clothes:
        if i[1] in answer:
            answer[i[1]] += 1
                # 옷을 종류별로 카운트하기
                # 이미 있는 종류면, 해당 종류에 개수 1 추가
        else:
            answer[i[1]] = 1
                # 없는 종류면, 1로 저장

    cnt = 1
        # 카운트를 1로 세팅
    
    for i in answer.values():
        cnt *= (i+1)
            # 아이템들의 개수를 한개씩 뽑ㅏ서
            # 아이템 개수에 1 더함 (착용하지 않는 경우 포함)
            
    return cnt - 1
        # 하나도 안 입는 경우는 빼기
'''