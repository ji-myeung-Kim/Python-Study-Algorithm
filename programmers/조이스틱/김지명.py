# name = "JAZ"
# change = [min(ord(i) - ord("A"), ord("Z") - ord(i)) for i in name]
# print(change)

def solution(name):
    change = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
    print(change)
    idx, answer = 0, 0

    while True:
        answer += change[idx]
        print("answer1:", answer)
        change[idx] = 0
        print(change)
        if sum(change) == 0:
            break

        left, right = 1, 1
        while change[idx - left] == 0:
            left += 1
            # print("change: ",change, "left :", left)
        while change[idx + right] == 0:
            right += 1
            # print("change:", change, "right :", right)
        answer += left if left < right else right
        
        idx += -left if left < right else right
        print("idx:",idx, "answer2:", answer,"left :", left,"right :", right)
    return answer
print(solution("CBX"))