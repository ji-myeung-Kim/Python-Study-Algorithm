import math

def solution(brown, yellow):
    total = brown + yellow  # 카펫의 총 넓이
    divisors = []
    answer = []

    # 카펫 넓이(total)의 약수 구하기 - total의 제곱근 이하 까지만
    for i in range(1, int(math.sqrt(total))+1):
        if total % i == 0:
            divisors.append(i)   

    for height in divisors:  # 문제 조건에서 height < width 이기 때문에 divisors에 담겨있는 수는 height가 된다
        width = total // height
        if (width-2)*(height-2) == yellow:
            answer = [width, height]         
            return answer
            