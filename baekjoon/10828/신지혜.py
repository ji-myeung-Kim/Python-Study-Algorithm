'''
https://www.acmicpc.net/problem/10828
백준 10828 - 스택
'''
import sys

# 명령의 수 입력 및 stack 초기화
N = int(sys.stdin.readline())
stack = []

# command 종류에 따라서 출력 결과 상이
for i in range(N):
    command = sys.stdin.readline().strip().split(' ')
    
    if command[0] == 'push':
        stack.append(command[1])
        
    elif command[0] == 'pop':
        print(stack.pop() if len(stack) != 0 else -1)
            
    elif command[0] == 'size':
        print(len(stack))
        
    elif command[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
        
    elif command[0] == 'top':
        print(stack[-1] if len(stack) != 0 else -1)
        