t = int(input())        # 테스트 케이스 개수 t개 입력 받음
for i in range(t):      # 변수 선언이 굳이 필요 없다면 언더바 사용
    a, b = map(int, input().split())    # input으로 받는 것은 for문을 통해서도 가능
    print(a + b)                        # map으로 split으로 나눈 부분에 각각 int 씌워주기