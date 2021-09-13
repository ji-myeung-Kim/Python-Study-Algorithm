def solution(brown, yellow):
    answer = []
    sum = brown + yellow                                # 총 카펫 수 sum

    for i in range(2, sum):
        if (sum % i == 0):                              # sum이 두 개의 수로 곱해지는 경우 찾기 ex) sum=12면 2*6 3*4
            if (sum // i >= i):                         # 몫이 나누는 수보다 클 경우
                width = sum // i                        # 그 값을 width로 결정하고
                height = i                              # 나누는 수를 height로 결정
            else:                                       # 반대 경우
                width = i
                height = sum // i

            if ((width - 2) * (height - 2) == yellow):  # width와 height가 결정되면 테두리 안의 격자 개수를 구할 수 있다.
                                                        # 테두리 내의 격자 개수와 yellow 카펫의 개수가 동일하면, 해답 찾기 완료.
                answer.append(width)
                answer.append(height)
                break;                                  # break 해주지 않으면 가로 세로 길이가 위치만 바뀐 채로 append된다.

    return answer