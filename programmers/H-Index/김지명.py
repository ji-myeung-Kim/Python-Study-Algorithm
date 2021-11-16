def solution(citations):
    citations.sort(reverse=True)
    print(citations)
    for idx , citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations)