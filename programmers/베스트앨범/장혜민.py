## 1차시도 
def solution(genres, plays):
    hash = dict()   
    # 장르별 플레이 총합 딕셔너리 
    for i in range(len(genres)) :
        if genres[i] not in hash:
            hash[genres[i]] = plays[i]
        else:
            hash[genres[i]] += plays[i]

    hash_sorted = sorted(hash.items(), key=lambda x: -x[1])  # 플레이횟수 기준 내림차순으로 딕셔너리 정렬    
    dic = {k[0] : [] for k in hash_sorted}  # key값(장르)만 리스트로 만듬 => 플레이총합 많은순으로 정렬된 장르 리스트
    
    for i in range(len(plays)):
        dic[genres[i]].append((plays[i], i))  # key가 장르, value가 (플레이횟수, 인덱스)들의 리스트인 딕셔너리 
    
    answer = []
    for play in dic.values():
        play.sort(key=lambda x: (-x[0], x[1]))  # 각 장르별 (플레이횟수, 인덱스)들의 리스트를 플레이횟수 기준 내림차순, 인덱스 기준 오름차순으로 정렬
        answer.append(play[0][1])
        if len(play) > 1:  # 장르 내 곡 개수가 1개면 1개만 추가하고, 2개 이상이면 1개 더 추가
            answer.append(play[1][1])
    
    return answer

# genres=["classic","classic","classic","classic","pop"]
# plays=[500,150,800,800,2500]
# 정답: [4,2,3]
# 처음에 틀렸던 이유: 같은 장르 내 플레이 횟수가 동일한 곡이 있을 경우 고유번호가 낮은 순으로 들어가야 함



## 다른 사람의 풀이
from collections import defaultdict

def solution2(genres, plays):
    play_count_by_genre = defaultdict(int)
    songs_in_genre = defaultdict(list)

    for idx, genre, play in zip([i for i in range(len(genres))], genres, plays):
        play_count_by_genre[genre] += play  # 장르별 플레이 총합 딕셔너리 생성  
        songs_in_genre[genre].append((-play, idx)) # key가 장르, value가 (플레이횟수, 인덱스)들의 리스트인 딕셔너리 생성. 이때 play는 내림차순, idx는 오름차순 정렬해야 하므로 부호 반대로 해줌
        
    genre_in_order = sorted(play_count_by_genre.keys(), key=lambda x:play_count_by_genre[x], reverse=True) # 플레이횟수 기준 내림차순으로 딕셔너리 정렬.. 아 이렇게하면 key값만 리스트로 만들어지는구나..
    
    answer = []
    for genre in genre_in_order:
        answer.extend([ idx for (play_minus, idx) in sorted(songs_in_genre[genre])[:2]])  # 아까 플레이횟수 부호 반대로 집어넣었기 때문에 내림차순 정렬됨
        # 넣을 원소가 [곡1, 곡2] = list(iterable 객체) 형태이기 때문에 풀어서 넣으려고 extend 함수를 사용한다
       
        ### 파이썬 list 함수 extend(iterable) vs append(x) ###
        # append는 x 그 자체를 리스트에 넣는다
        # extend는 iterable 객체의 가장 바깥쪽 iterable을 넣는다
        # 예) x = ['a','b']인 경우 'a', 'b'가 들어가고, x = [['a','b']]인 경우 ['a','b']가 들어감
    return answer



genres=["classic","classic","classic","classic","pop"]
plays=[500,150,800,800,2500]
print(solution2(genres, plays))