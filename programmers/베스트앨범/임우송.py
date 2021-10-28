# 2. 베스트앨범 / 해시

# ---------문제 해석---------------------------------------------------------------------- 
# 장르마다 최대 두 개까지의 노래를 수록한다.(재생횟수가 많은 두 곡)
# 정렬 순서
# 1.속한 노래들의 재생횟수를 모두 더하여, 장르 순서로 먼저 정렬한다.   
#       ※ 재생횟수 합이 같으면? => 제한사항 없음? => 1번 정렬 패스? ======> 제한사항 마지막 - 모든 장르는 재생된 횟수가 다르다 
#       ※ 재생횟수의 합은 2곡의 합인지? or 해당 장르 전체의 합인지?  => 먼저 전체 합으로 진행 
# 2.장르로 먼저 정렬한 뒤, 그 안에서 노래 각각의 재생횟수로 정렬한다.
# 3.재생횟수가 같으면 고유번호=인덱스 순서로 정렬한다. 

# ---------접근 방법---------------------------------------------------------------------- 
# 노래의 인덱스(고유번호)를 key로, 장르이름을 value로 해시를 생성해서 장르(value)별 재생횟수를 가져오도록 구성해본다.
# ----------------------------------------------------------------------------------------

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = []
    hash = {}   
    sumGenres = {}   
 
    for i in range(len(genres)):
        hash.setdefault(i, [genres[i], plays[i]])   # {고유번호 : [장르,재생횟수]} 해시 생성  -> 각각의 노래마다 [장르, 재생횟수]를 연결
        
        sumGenres.setdefault(genres[i], 0)   # {장르 : 장르별 재생횟수의 합} 해시 생성  -> 재생횟수 많은 장르별로 가장 먼저 정렬하기 위한 dictionary
        sumGenres[genres[i]] += plays[i]    # 장르(key)가 같으면 재생횟수(value)를 중복해서 더해준다 

    # 재생횟수를 기준으로 내림차순 정렬 
    hash = sorted(hash.items(), reverse=True, key = lambda item : item[1][1])   
    sumGenres = sorted(sumGenres.items(), reverse=True, key = lambda item : item[1])

    index = 0
    while index < len(sumGenres):   # 정렬된 장르를 기준으로, 모든 장르 검색이 끝날때까지 반복 
        count = 0 
        for h in hash:
            if count < 2:   # 한 장르의 노래가 2개이면 반복문을 빠져나와 다음 index(다음 장르)의 곡을 찾는다
                if h[1][0] == sumGenres[index][0]:  # 노래의 집합인 hash를 돌면서 장르가 같으면 
                    answer.append(h[0])     
                    count += 1  # 한 장르의 노래를 추가할 떄마다 누적
        index += 1

    return answer

solution(genres, plays)




