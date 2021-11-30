import sys
input = sys.stdin.readline
N = int(input())
answer = 0

if N>=5:                                    # 5와 같거나 클 경우만 5kg 짜리 봉지 사용
    fkgnum = N//5                           # 최대 5kg봉지 개수
    
    while fkgnum>0:                         # 5kg봉지 개수 한개씩 줄이며 반복
        if (N - fkgnum*5)%3 == 0:           # 5kg봉지를 사용하고, 나머지 설탕을 3kg봉지에 넣을 수 있다면
            tkgnum = (N - fkgnum*5)//3
            answer = fkgnum + tkgnum        
            break;                          # 5kg봉지의 개수가 최대인 상황이므로 break
        fkgnum -= 1
        
if answer == 0:                             # 5kg봉지를 사용하지 않았으면 answer = 0임
    if N%3 == 0:                            # 3kg만으로 운반 가능하다면
        answer = N//3
    else:
        answer = -1                         # 위 모든 조건을 충족하지 못할 경우 -1
        
print(answer)




# 아래는 첫 번째 풀이인데 시간이 오래걸려서 위 풀이로 다시 풀었음~

# solutions = []  # 완전한 Nkg을 배달할 수 있는 모든 경우의 수
# answers = []    # 모든 경우의 수에서, 총 봉지의 수만 담겨있는 배열
# fkgnum = 0      # 5kg 봉지 개수

# # 5a+3b = 18 을 만족하는 모든 a,b를 찾는 반복문
# while True:
#     tkgnum = 0  # 3kg 봉지 개수
    
#     while True:                                 # 안쪽 while문에서 3kg봉지 개수를 1개씩 늘림
#         if (tkgnum*3+fkgnum*5) == N:
#             solutions.append([fkgnum, tkgnum])
#         elif (tkgnum*3+fkgnum*5) > N:           # N보다 커질 경우 반복문을 빠져나감
#             break;
        
#         tkgnum += 1                             
    
#     fkgnum += 1                                 # 안쪽 반복문을 빠져 나온 뒤 5kg봉지 개수 증가
    
#     if fkgnum*5>N:                              # 5kg봉지만으로도 N보다 커질 경우 반복문 완전히 종료
#         break;

# if solutions:
#     for i in solutions:
#         fkgnum = i[0]
#         tkgnum = i[1]
#         answers.append(fkgnum + tkgnum)
#     print(min(answers))
# else:                                           # 경우의 수가 1개도 없을 경우 -1출력
#     print(-1)   