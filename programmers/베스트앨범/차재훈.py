"""
프로그래머스 LEVEL3 베스트앨범
https://programmers.co.kr/learn/courses/30/lessons/42579
해시
"""
# 1차시도
# from collections import defaultdict

# def solution(genres, plays):
#     answer = []
#     hash = defaultdict(list)
#     total_dict = defaultdict(int)
#     for genre, i in zip(genres, range(len(plays))):
#         total_dict[genre] += plays[i]
#         hash[genre].append((i,plays[i]))

#     sorted_total_list = sorted(total_dict.items(), key=lambda x:x[1], reverse=True)

#     for key in sorted_total_list:
#         hash[key[0]].sort(key=lambda x:x[1], reverse=True)

#         for i in range(2):
#             answer.append(hash[key[0]][i][0])
            
#     return answer
"""
테스트케이스 1, 2, 4, 8, 9, 11, 12번에서 런타임 에러 발생
장르에 속한곡이 하나일때 list index out of range 에러 확인
"""

# 2차시도
from collections import defaultdict

def solution(genres, plays):
    answer = []
    hash = defaultdict(list)
    total_dict = defaultdict(int)
    # 장르와 노래의 인덱스 값을 반복한다.
    for genre, i in zip(genres, range(len(plays))):
        # 장르를 키로 두고 해당하는 장르 재생횟수를 더해준다.
        total_dict[genre] += plays[i]
        # 노래를 장르별로 모아 주기 위해 hash라는 딕셔너리에 장르를 키로 인덱스와 재생횟수를 튜플로 저장한다.
        hash[genre].append((i,plays[i])) 
    
    # 장르별 총 재생횟수가 저장된 딕셔너리를 내림차순으로 정렬해준다.
    sorted_total_list = sorted(total_dict.items(), key=lambda x:x[1], reverse=True)
    print(f'{sorted(total_dict, key=lambda x:total_dict[x], reverse=True)} -------------------------------value')
    print(f'{sorted_total_list} -------------------------------sorted')
    # 내림차순으로 정렬된 장르별 총 재생횟수 딕셔너리를 반복한다.
    for key in sorted_total_list:
        # 장르별 노래들의 재생횟수가 저장된 딕셔너리의 장르별 재생횟수(value)를 내림차순으로 정렬한다.
        hash[key[0]].sort(key=lambda x:x[1], reverse=True)

        # 장르별 최대 두곡까지만 선택 가능하므로 정렬된 딕셔너리의 각 장르별 밸류의 길이만큼 반복한다.
        for i in range(len(hash[key[0]])):
            # i가 2이상 일 경우 두곡이 선택되었으므로 반복을 멈추고 다음 장르로 넘어간다.
            if i >= 2:
                break
            # i가 2미만 일 경우 answer에 노래(plays)의 인덱스값을 넣어준다.
            else:
                answer.append(hash[key[0]][i][0])
            
    return answer
"""
주석을 달다보니 total_dict을 정렬할때 items()를 이용한 정렬보다
sorted(total_dict, key=lambda x:total_dict[x], reverse=True)으로 정렬을 했다면
key[0]과 같은 복잡한 형태가 아닌 key로 검색이 가능해서 조금더 직관적?인 코드가 되지 않을까 싶다.
"""
if __name__ == '__main__':
    genres = ["classic", "pop", "classic", "classic", "pop"]
    genres2 = ["classic", "pop", "classic", "classic","jazz","pop", "Rock", "jazz"]
    plays = [500, 600, 150, 800, 2500]
    plays2 = [500, 600, 150, 800, 1100, 2500, 100, 1000]
    print(solution(genres, plays)) # [4, 1, 3, 0]
    print(solution(genres2, plays2)) # [5, 1, 4, 7, 3, 0, 6]
