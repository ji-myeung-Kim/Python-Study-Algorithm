'''
문제 - 해시
프로그래머스 베스트앨범
https://programmers.co.kr/learn/courses/30/lessons/42579
'''


def solution(genres, plays):
    answer = []
    song = len(genres)
    total_dic = {}
    
    for i in range(song):
        if genres[i] not in total_dic.keys():
            total_dic[genres[i]] = {'total': plays[i], i: plays[i]}
        else:
            total_dic[genres[i]]['total'] += plays[i]
            total_dic[genres[i]][i] = plays[i]
    
    sorted_genres_list = sorted(
        total_dic.items(), key=lambda x: x[1]['total'], reverse=True)
    
    for j in range(len(sorted_genres_list)):
        genre_dic = sorted_genres_list[j][1]
        sorted_songs_list = sorted(
            genre_dic.items(), key=lambda x: x[1], reverse=True)
        k = 1
        while k <= 2:
            answer.append(sorted_songs_list[k][0])
            if (len(sorted_songs_list) < 3):
                break
            k += 1
    
    return answer


'''
풀이
def solution(genres, plays):
    answer = []
    song = len(genres)
        # 곡 개수
    total_dic = {}
        # 몇 번 재생했는지 확인할 딕셔너리 생성
        
    for i in range(song):
        # 곡 개수만큼 반복문 실행하면서
        
        if genres[i] not in total_dic.keys():
            # 만약 key에 없는 장르라면
            
            total_dic[genres[i]] = {'total': plays[i], i: plays[i]}
                # 새로운 장르 key의 하위 딕셔너리에 장르별 총 재생 수 total key에 plays[i] 넣기
                # 곡 번호 i key에 plays[i] 넣기
                
        else:
            total_dic[genres[i]]['total'] += plays[i]
            # key에 있는 장르라면 total에 합 누적
            
            total_dic[genres[i]][i] = plays[i]
            # 곡 번호에 plays[i] 입력
    
    sorted_genres_list = sorted(
        total_dic.items(), key=lambda x: x[1]['total'], reverse=True)
            # 만들어진 total_dic의 items로 정렬하기
            # 각 genre의 하위 딕셔너리의 total key를 기준으로 내림차순 정렬
    
    for j in range(len(sorted_genres_list)):
        # total을 기준으로 정렬한 리스트의 한 요소씩 접근
        
        genre_dic = sorted_genres_list[j][1]
            # 각 장르의 딕셔너리를 가져오기
        
        sorted_songs_list = sorted(
            genre_dic.items(), key=lambda x: x[1], reverse=True)
                # 가져온 각 장르의 딕셔너리에서 각 value를 기준으로 내림차순 정렬하기
        
        k = 1
        while k <= 2:
            answer.append(sorted_songs_list[k][0])
                # 두 개씩 answer 리스트에 넣기
            
            if (len(sorted_songs_list) < 3):
                break
                    # 리스트의 길이가 3미만인 경우 중단
                    # total까지 포함되어 있는 리스트이므로 2일 때 total과 곡 1개의 play 수가 있으므로
            k += 1
    return answer
'''