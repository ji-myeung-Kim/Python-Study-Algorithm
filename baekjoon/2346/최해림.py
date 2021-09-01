첫번째 수는 popleft()를 통해 터트린다.

rotate함수를 통해서 양수면 오른쪽, 음수면 왼쪽으로 회전시킨다.

풍선이 남아있고 num이 양수면 -(num-1)만큼 회전시킨다. 

(처음에 -1은 풍선을 터트리는 사람을 기준으로 왼쪽에 놓게만들기 위해서, num-1은 양수면 왼쪽으로 회전하는데

popleft를 통해 위치를 -1만큼 옮기기 때문) 

풍선이 남아있고 num이 음수면 (-1*num)만큼 회전한다

(-1은 풍선을 터트리는 사람을 기준으로 왼쪽에 놓게만들기 위해서, num은 오른쪽으로 회전시켜야 해서 굳이 -1할 필요 없음)


from collections import deque
N = int(input())
q = deque([(num, idx) for idx, num in enumerate(map(int, input().split()))])
answer = []

while q:
    num, idx = q.popleft()
    answer.append(idx + 1)

    if q and num > 0:
        q.rotate(-1*(num-1))
    elif q and num < 0:
        q.rotate(-1*num)

print(' '.join(map(str, answer)))
