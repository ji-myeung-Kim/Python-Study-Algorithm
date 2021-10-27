# 너무 어려워서 이해하는 데 한계가 느껴집니다. . . 그냥. . 그런가보다 하려고여. . 💩

import sys
input = sys.stdin.readline

def top(disc, start, temp, target):
    if disc == 1:                           # 2️⃣ 맨 아래 원판을 목표 기둥으로 옮기기
        print(start, " ", target)        
    else:
        top(disc - 1, start, target, temp)  # 1️⃣ 맨 아래 원판을 제외한 모든 원판을 보조 기둥으로 옮기기
        print(start, " ", target)
        top(disc - 1, temp, start, target)  # 3️⃣ 나머지 원판들을 목표 기둥으로 옮기기

a = int(input())

print(2 ** a - 1) # 이동하는 수는 규칙적임. 그냥 그런거야~
top(a, 1, 2, 3)
