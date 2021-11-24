def solution(clothes):
    di = {}
    for cloth in clothes:
        if cloth[1] not in di.keys():
            di[cloth[1]] = [cloth[0]]  #동일한 키값을 가질경우 여러개의 항목을 받을 수 있도록 리스트로 선언
        else:
            di[cloth[1]].append(cloth[0]) # 동일한 키가 없을경우 추가해줌
    answer =1
    for k in di.keys():
        answer *= len(di[k]) + 1    

    return(answer -1)

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))