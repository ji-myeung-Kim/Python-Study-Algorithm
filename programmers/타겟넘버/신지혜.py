def dfs(numbers, target, depth, sum):
    if depth == len(numbers):
        if target == sum:
            return 1
        else:
            return 0
    else:
        return dfs(numbers, target, depth+1, sum+numbers[depth])+dfs(numbers, target, depth+1, sum-numbers[depth])

def solution(numbers, target):
    return dfs(numbers, target, 0, 0)


print(solution([1, 1, 1, 1, 1], 3))
