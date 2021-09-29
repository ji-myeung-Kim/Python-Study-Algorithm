#programmers 타겟 넘버

def solution(numbers, target):
    answer = 0
    
    def dfs(idx, sum) :
        if (idx == len(numbers)) :
            if (sum == target) :
                nonlocal answer             # 해당 함수가 아닌, 바로 바깥쪽 위치에 있는 answer를 사용하겠다는 의미
                answer += 1
            return 
        else : 
            dfs(idx+1, sum+numbers[idx])    # 계속해서 깊이 들어감 (+인 경우를 먼저 모두 탐색)
            dfs(idx+1, sum-numbers[idx])    # -인 자식 노드 탐색
    
    dfs(0,0)
    
    return answer

numbers = [1,1,1,1,1]
    
print(solution(numbers, 3))
