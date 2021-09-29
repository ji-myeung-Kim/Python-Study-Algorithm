def solution(numbers, target):
    answer = 0
    result = 0  
    idx = 0

    def cal(result, idx):    
        # 재귀함수 종료조건 : numbers의 마지막 인덱스까지 다 탐색했으면 종료      
        if idx == len(numbers):
            if result == target:  # target 숫자와 일치하는 경우라면 answer += 1     
                nonlocal answer         
                answer += 1            
            return
              
        # 재귀함수를 통해 result 값을 누적해나간다
        cal(result + numbers[idx], idx+1)  # 직전까지의 누적값에 numbers의 다음 인덱스 값을 + 하는 경우
        cal(result - numbers[idx], idx+1)  # 직전까지의 누적값에 numbers의 다음 인덱스 값을 - 하는 경우
    
    cal(result, idx)
    return answer

        
numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))
