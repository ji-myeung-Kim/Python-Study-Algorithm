# name="JEROEN"
name="JAN"

def solution(name):
    start = [0]*len(name)
    answer = 0
    nexti = 0
    min_lr = len(name)
    # A~Z 65~90

    # 0~25 (+65)
    name = list(map(lambda x: ord(x)-65, name))

    # [9, 4, 17, 14, 4, 13]
    # [0, 0, 0, 0, 0, 0]
    # [9, 4, 25-17, 25-14, 4, 25-13]

    for i in range(len(name)):
        # 상하 move
        answer += min(name[i] - start[i], 25 - name[i] + 1)
        # print(name[i] - start[i])
        # print(25 - name[i] + 1)

        # 다음 기준
        nexti = i + 1

        # 좌우 move
        # 연속으로 A일 때의 좌우 길이
        while nexti < len(name) and name[nexti] == 0:
            nexti += 1
        # 오른쪽으로 갔다가 A를 마주하게되어 다시 돌아서 
        # (i * 2) + (len(name) - nexti)
        min_lr = min(min_lr, (i * 2) + (len(name) - nexti))
    print(nexti)

    print(answer + min_lr)


    return answer + min_lr

solution(name)