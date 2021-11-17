citations = [3, 0, 6, 1, 5]

def solution(citations):

    n = len(citations)

    for h in range(n+1):
        cnt = 0
        for cit in citations:
            if cit >= h:
                cnt += 1
        
        if cnt == h:
            return cnt


print(solution(citations))