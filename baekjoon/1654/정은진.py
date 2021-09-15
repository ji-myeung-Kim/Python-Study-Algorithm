# 절대 답이 나오지 않던 망한 풀이 (

# def lan_len(start, end, lans, N, answers):
#     if start+1 >= end :
#         return answers
#
#     mid = (start + end) // 2
#     lans_sum = 0
#
#     for i in lans:
#         lans_sum += (i // mid)
#
#     if lans_sum == N:
#         lan_len(start, mid, lans, N, answers.append(mid))
#     else:
#         if lans_sum > N:
#             lan_len(mid, end, lans, N, answers)
#         else:
#             lan_len(start, mid , lans, N, answers)
#
# lans = [802, 743, 457, 539]
#
# answers = []
# print(lan_len(1, 802, lans, 11, answers))

import sys
K, N = map(int, input().split())
lans = [int(sys.stdin.readline()) for _ in range(K)]    #sys.stdin.readline()는 String을 반환하기 때문에, 형변환 필수
start, end = 1, max(lans)                               #end는 lans배열의 원소 중, max값으로 지정한다

while (start <= end) :                                  #이진탐색 블럭
    mid = (start+end) // 2
    lans_sum = 0

    for i in lans :
        lans_sum += (i//mid)

    if lans_sum >= N :                                  #자른 랜선의 개수가 목표치보다 많다면, 더 길게 자른다
        start = mid + 1
    else :                                              #자른 랜선의 개수가 목표치보다 적다면, 더 짧게 자른다
        end = mid - 1                                   #해당 문장을 끝으로 반복문이 끝났다면 현 mid(즉 201)길이로 랜선을 자를 때, N보다 수가 적다는 뜻
                                                        #아마 어떤 값이 입력되든, 해당 문장을 끝으로 반복문이 끝나게 되는 듯하다.

print(mid)                                              #따라서 직전길이인 mid-1(200)의 길이로 잘라야, 잘랐을 때 N개가 나오는 랜선 길이 중 가장 긴 길이이다.