'''
https://www.acmicpc.net/problem/10773
백준 10773 - 제로
'''
import sys

# 명령의 수 입력 및 stack 초기화
N = int(sys.stdin.readline())
stack = []

for i in range(N):
    num = int(sys.stdin.readline().strip())
    
    if num > 0:
        stack.append(num)
    elif num == 0:
        stack.pop()
        
print(sum(stack))