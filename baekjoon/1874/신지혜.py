'''
https://www.acmicpc.net/problem/1874
백준 1874 - 스택 수열
'''
import sys

# 수열 갯수 입력 및 list, 변수 초기화
n = int(sys.stdin.readline())
stack = []
answer = []
top = 1
flag = 0

for _ in range(n):
    # 수열을 이루는 숫자 입력
    num = int(sys.stdin.readline())
    
    # 입력받은 숫자보다 작을 땐 스택에 숫자들을 쌓는다
    while top <= num:
        stack.append(top)
        answer.append('+')
        top += 1
        
    # 스택의 숫자가 입력받은 숫자와 동일하면 answer에 - 추가 / 스택 pop
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    # 그렇지 않은 경우는 스택을 이용해 해당 수열을 만들 수 없는 경우로 NO 출력
    else:
        print('NO')
        flag = 1
        break
    
# NO가 나오지 않은 스택의 결과만 출력
if flag == 0:
    for i in range(len(answer)):
        print(answer[i])       