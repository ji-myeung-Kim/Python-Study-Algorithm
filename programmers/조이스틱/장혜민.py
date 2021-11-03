## 1차시도 - 성공 ##

# print(ord("A"))  # 65
# print(ord("Z"))  # 90
name = "JEROEN"

def solution(name):
    check = [1 if name[i] == "A" else 0 for i in range(len(name))]    
    answer = 0
    i = 0
    while True:          
        # 알파벳을 만들기위해 위가 빠를지 아래가 빠를지 정한다
        if check[i] == 0:
            answer += min(ord(name[i])-65, 1+90-ord(name[i]))
            check[i] = 1

        # 더이상 만들어야 할 글자가 없으면 좌우로 이동하지 않고 종료
        if 0 not in check:
            break

        # 다음 글자가 A일때 오른쪽으로 이동하는게 빠를지 왼쪽으로 뒤돌아가는게 빠를지 정한다    
        left = right = 0  # 왼쪽 또는 오른쪽으로 이동할 횟수
        l = r = i  # 인덱스를 나타낼 변수
        while True:
            r = (r+1) % len(check)   # 인덱스 1칸씩 오른쪽으로 이동
            right += 1          
            if check[r] == 0:
                break                     
        while True:
            l = (l-1) % len(check)  # 인덱스 1칸씩 왼쪽으로 이동
            left += 1
            if check[l] == 0:
                break           
        if left < right:
            answer += left
            i = l
        else:
            answer += right
            i = r

    return answer