N = int(input())
result = 0

for i in range(1, N+1):
    # 1) str(n) : 숫자를 문자열로 만들어준다
    # 2) map(int, str(n)) : 문자열로 되어있는 각 자릿수를 정수로 바꿔준다( ex, "123" > 정수 1, 2, 3 각각으로 바꿔준다)
    arr = list(map(int, str(i)))
    result = i + sum(arr)

    if N == result:
        print(i)
        break

    if N == i:
        print(0)


