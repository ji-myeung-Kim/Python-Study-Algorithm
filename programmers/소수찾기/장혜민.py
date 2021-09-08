import math

# 최종 함수
def solution(numbers):
    result = permutation(numbers)
    return prime_number(result)


# 만들 수 있는 모든 숫자 구하는 함수
def permutation(numbers):
    used = [0]*len(numbers) # 숫자 만들때 해당 숫자를 뽑았는지 안뽑았는지 표시하는 용도의 리스트(중복 선택 막기위해)
    result = set() # numbers에 중복된 숫자 있는 경우(예: "117") - set으로 정답 중복 제거
    
    # nP1, nP2, ... nPn
    for r in range(1, len(numbers)+1):
        
        # numbers 중 r개의 숫자 뽑은 모든 결과 구하는 함수
        def generate(value, used):
            # 재귀함수 종료조건: 만든 숫자의 길이가 r이 되면 종료
            if len(value) == r:
                result.add(int(value)) # int 변환 - 맨 앞자리 0 제거
                return
            
            # 재귀함수 본문
            for i in range(len(numbers)):
                if used[i] == 0: 
                    value += numbers[i] # 숫자를 뽑아서 길이가 r이 될때까지 더해나간다
                    used[i] = 1 # 숫자 뽑을때 중복방지
                    generate(value, used)
                    
                    # 재귀함수 종료후, 직전 상태로 되돌아가서 for문 마저 실행
                    value = value[:-1]
                    used[i] = 0

        # generate 함수는 value="" 부터 시작 -> 길이 r 될때까지 재귀호출
        generate("", used)
    return result


# 소수 몇개인지 반환하는 함수
def prime_number(numbers):
    answer = 0
    for num in numbers:
        check = 0
        # 0, 1은 소수 아님
        if num < 2:
            check = 1
        # 2는 소수임
        elif num == 2:
            pass
        # num이 3 이상인 경우
        else:     
            # num을 2 ~ num의 제곱근까지 나눠봤을때 나머지가 0인 경우가 없다면 소수임
            for i in range(2, int(math.sqrt(num))+1):            
                if num % i == 0:                
                    check = 1
                    break        
        if check == 0:            
            answer += 1   
    return answer



print(solution("011"))  





################
# from itertools import permutations
# import math

# def solution(numbers): 
#     result = set()
#     for r in range(1, len(numbers)+1):
#         for p in permutations(numbers, r):
#             result.add(int(''.join(p)))
                            
#     answer = 0
#     for num in result:
#         check = 0
#         if num < 2:
#             check = 1
#         elif num == 2:
#             pass
#         else:     
#             for i in range(2, int(math.sqrt(num))+1):            
#                 if num % i == 0:                
#                     check = 1
#                     break        
#         if check == 0:            
#             answer += 1

#     return answer
