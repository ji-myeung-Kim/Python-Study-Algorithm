import sys

 # 문제 조건에서 a, b, c가 20보다 크면 모두 w(20, 20, 20)으로 통일시키기 때문에 3차원배열의 각 원소는 0~20까지만 필요함
memo = [ [ [0]*21 for _ in range(21) ] for _ in range(21) ]  # a, b, c의 값을 각각 저장할 3차원배열 생성

def w(a, b, c):    
    if a<=0 or b<=0 or c<=0 :
        return 1
    if a>20 or b>20 or c>20 :
        return w(20, 20, 20)

    # 메모이제이션 해둔 값이 있다면 바로 반환한다
    if memo[a][b][c]:
        return memo[a][b][c]    
    else:           
        if a < b < c:
            memo[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            return memo[a][b][c]
        else:
            memo[a][b][c] =  w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
            return memo[a][b][c]

while True:    
    a, b, c = list(map(int, sys.stdin.readline().split(" ")))

    if a == b == c == -1:
        break

    # print("w(%d, %d, %d) = %d"%(a, b, c, w(a,b,c)))
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')


# 참고: f-string
# f'문자열 {변수} 문자열'
# 문자열 맨앞에 f를 붙이고 {} 안에 직접 변수 이름이나 출력하고 싶은 값을 넣는다.