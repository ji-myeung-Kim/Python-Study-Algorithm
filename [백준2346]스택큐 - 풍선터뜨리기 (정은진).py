def solution(ballon, paper):
    b_list = [(i, v) for (i, v) in enumerate(paper)]
    answer = []

    picked_index = 0

    while len(b_list) > 0:
        papernum = b_list.pop(picked_index)  # pop, 즉 풍선 터뜨리기
        answer.append(papernum[0]+1)  # 터뜨린 풍선 answer에 넣기
        print("터진 풍선 인덱스 :", papernum[0]+1, "값:", papernum[1])
        if (len(b_list) > 0):
            if papernum[1] > 0:
                print("양수")
                picked_index = ((papernum[1]) % len(b_list)) - 1  # 다음 터뜨릴 풍선 찾기
                print("다음에 찾을 풍선 인덱스 :", picked_index)
            else:
                print("음수")
                picked_index = (papernum[0]+1+papernum[1]) % len(b_list)
                print("다음에 찾을 풍선 인덱스 :", picked_index)

        else:
            break

        print("-----------------------------")


    return answer

paper = [3, 2, 1, -3, -1]
print(solution(5, paper))