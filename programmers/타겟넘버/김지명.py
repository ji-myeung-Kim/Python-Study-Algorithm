def solution(numbers, target):
    n = len(numbers)
    answer = 0
    
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer #위에 3번에 있는 answer를 사용할 수 있도록 하는 nonlocal 선언
                answer += 1
            return answer
        else:
            dfs(idx+1, result + numbers[idx])
            dfs(idx+1, result - numbers[idx])
    dfs(0,0)
    return answer