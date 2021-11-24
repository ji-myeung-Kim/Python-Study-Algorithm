# H-Index란? https://www.ibric.org/myboard/read.php?Board=news&id=270333
# 코드 참고 - https://yunaaaas.tistory.com/56
def solution(citations):
    citations.sort(reverse=True)                # 내림차순 정렬
    for idx, citation in enumerate(citations):  # 인덱스와 요소 추출하여 반복
        if(citation<=idx):                      # 인용수보다 논문의 수가 많아지면
            return idx                          # 논문 수 리턴

    return len(citations)                       # 왜인지 모름