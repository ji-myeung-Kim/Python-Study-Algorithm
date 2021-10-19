# 백준_while문_A+B -4
# https://www.acmicpc.net/problem/10951

while True:     # 테스트케이스가 없기 떄문에 무한루프
    try:        # 에러 발생할 여지가 있는 코드
        a, b = map(int, input().split())
    except :    # 에러 발생시 실행시킬 코드
        break
    print(a + b) # 에러가 발생하지 않으면 실행시킬 코드
