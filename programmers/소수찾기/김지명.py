import itertools

def is_prime(num):
    #0과 1은 소수에 포함되지 않기때문에 False로 처리
    if num < 2:
        return False
    elif num==2:
        return True

    #넘겨 받은 수를 2부터 넘겨받은 숫자전까지의 숫자로 나누어줄때
    # 나머지가 없으면 소수가 아니므로 False, 나머지가 있으면 소수이므로 True

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    num1 = []
    num2 = []

    #받은수의 길이만큼 수들의 모든 조합들을 추출
    # ex) i 가 1일때['1', '7'], 2일때['17', '71'] 합쳐지면 [1, 71, 17, 7]
    for i in range(1, len(numbers)+1):
        num1 = list(map(''.join, itertools.permutations(numbers, i)))

        #int형으로 변환
        for j in num1:
            num2.append(int(j))

    #중복을 없애주기 위해 set형으로 변환     
    num2 = list(set(num2))

    #//[1, 71, 17, 7] 여기에서 소수이 있을때 answer에 1씩 더해준다.
    for i in num2:
        if is_prime(i):
            answer += 1

    return answer