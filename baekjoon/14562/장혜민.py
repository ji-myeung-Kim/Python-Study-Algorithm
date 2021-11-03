## 1차시도 ##
# 이렇게 하면 될줄 알았는데 왜 return값이 None이 나올까요?????
'''
import sys
input = sys.stdin.readline

def recur(s, t, cnt):    
    if s == t:
        return cnt
    elif s < t:
        recur(s*2, t+3, cnt+1)
        recur(s+1, t, cnt+1)
    
    

c = int(input())
for i in range(c):
    s, t = map(int, input().strip().split(" ")) 
    print(recur(s, t, 0))
'''

## 2차시도 - 성공 ##
import sys
input = sys.stdin.readline

def recur(s, t, cnt, result):    
    if s == t:
        result.append(cnt)
    elif s < t:
        recur(s*2, t+3, cnt+1, result)
        recur(s+1, t, cnt+1, result)
    return result
    

c = int(input())
for i in range(c):
    s, t = map(int, input().strip().split(" ")) 
    result = []
    print(min(recur(s, t, 0, result)))