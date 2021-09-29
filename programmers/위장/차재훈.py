from collections import defaultdict

def solution(clothes):
    answer = 1
    hash = defaultdict(list)
    
    for i in clothes:
        hash[i[1]].append(i[0])

    for v in hash.values():
        # 모든 경우를 곱해준다.
        # 부위별로 있는 옷의 갯수에서 아무것도 안입는 경우가 있을 수 있으니 +1을 해준다.
        answer *= len(v) + 1

    # 모두 안입는 경우는 없다고 했으니 최종 곱한 값에서 -1을 해준다.
    return answer-1
    
if __name__ == '__main__':
    clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    clothes2 = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
    print(solution(clothes))
    print(solution(clothes2))