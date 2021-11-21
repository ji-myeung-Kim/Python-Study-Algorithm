import sys

input = sys.stdin.readline

N = int(input())

# 모든 요소가 0인 배열로 초기화
table = [[0 for _ in range(N)] for _ in range(N)]

# input 읽어서 배열에 넣기
for i in range(N):
    ilist = list(map(int, input().split()))
    for j in range(len(ilist)):
        if ilist[j] == 0:
            table[i][j] = False
        else:
            table[i][j] = True

answers = [] # 횟수들을 담을 배열. 여기서 min값 찾기

print('초기 테이블-----------')
for _ in table:
    print(_)
print('-'*20)

def answer(N, table):
    for i in range(1 << N):
        cnt = 0
        slist = list(format(i,'0'+str(N)+'b'))

        # 스위치를 누를 부분을 True, 아닌 부분을 False로 변경하는 배열
        for i in range(len(slist)):
            if slist[i] == '1':
                slist[i] = True
            else:
                slist[i] = False

        # print(slist)

        print('********* 누르게 될 첫 줄 스위치 *********')
        print('slist = ', slist)
        # 첫째줄 스위치 누르기
        for i in range(N):
            if slist[i]:    # 스위치를 누르면
                if i == 0:  # 맨 왼쪽 전구일 경우
                    table[0][i + 1] = not table[0][i + 1]  # 오른쪽 전구 바꾸기
                elif i == (N - 1):  # 맨 오른쪽 전구일 경우
                    table[0][i - 1] = not table[0][i - 1]  # 왼쪽 전구 바꾸기
                    print('실행 됐나요 : ', table[0][i-1], not table[0][i-1])
                else:  # 둘 다 아닌 경우
                    print('설마 실행됐나요')
                    table[0][i + 1] = not table[0][i + 1]  # 오른쪽 전구 바꾸기
                    table[0][i - 1] = not table[0][i - 1]  # 왼쪽 전구 바꾸기
                table[0][i] = not table[0][i]  # 자기 자신 바꾸기
                table[1][i] = not table[1][i]  # 아래 전구 바꾸기
                print(table)
                cnt += 1

        print('<첫 줄 스위치 다 누른 후 테이블 상태>')
        for real in table:
            print(real)
        print('*' * 20)

        print('********************************')

        # 첫 째 줄 검사
        # for i in range(len(table[0])):
        #     if table[0][i]:  # 자신의 불이 켜져있을 경우
        #         if i == 0:  # 맨 왼쪽 전구일 경우
        #             table[0][i + 1] = not table[0][i + 1]  # 오른쪽 전구 바꾸기
        #         elif i == (N - 1):  # 맨 오른쪽 전구일 경우
        #             table[0][i - 1] = not table[0][i - 1]  # 왼쪽 전구 바꾸기
        #         else:  # 둘 다 아닌 경우
        #             table[0][i + 1] = not table[0][i + 1]  # 오른쪽 전구 바꾸기
        #             table[0][i - 1] = not table[0][i - 1]  # 왼쪽 전구 바꾸기
        #         table[0][i] = not table[0][i]  # 자기 자신 바꾸기
        #         table[1][i] = not table[1][i]  # 아래 전구 바꾸기
        #         cnt += 1

        # 둘 째 줄부터 검사 - 바로 위 전구가 켜져있을 경우 스위치를 누른다.
        for light in range(1, N):
            for j in range(N):
                if table[light - 1][j]:  # 위 전구의 불이 켜져있을 경우
                    if j == 0:  # 맨 왼쪽 전구일 경우
                        table[light][j + 1] = not table[light][j + 1]  # 오른쪽 전구 바꾸기
                    elif j == (N - 1):  # 맨 오른쪽 전구일 경우
                        table[light][j - 1] = not table[light][j - 1]  # 왼쪽 전구 바꾸기
                    else:  # 둘 다 아닌 경우
                        table[light][j + 1] = not table[light][j + 1]  # 오른쪽 전구 바꾸기
                        table[light - 1][j] = not table[light - 1][0]  # 왼쪽 전구 바꾸기
                    table[light][j] = not table[light][j]  # 자기 자신 바꾸기
                    table[light - 1][j] = not table[light - 1][j]  # 위 전구 바꾸기

                    if light != (N-1):
                        table[light + 1][j] = not table[light + 1][j]  # 아래 전구 바꾸기

                    for _ in table:
                        print(_)
                    print('*' * 20)

        if True not in table[N-1]:
            # for i in table:
            #     print(i)
            # print('count=', cnt)
            # print('*' * 20)
            answers.append(cnt)

    if answers:
        print(min(answers))
    else:
        print(-1)


answer(N, table)




# a = 10
# print(type(a), a)
# a = 0b10 # 10을 2진수로 나타내겠 (접두어 0b)

# alist = []
# N=3
# for i in range(1<<N):
#     alist = list((format(i,'0'+str(N)+'b')))  # 일정한 자릿수로 2진수를 표현하기
#     print(alist)

# 2진수: 0b
# 8진수: 0o
# 16진수: 0x

# >>> bin(42)
# '0b101010'
# >>> oct(42)
# '0o52'
# >>> hex(42)
# '0x2a'

# >>> int('0b101010', 2)
# 42
# >>> int('0o52', 8)
# 42
# >>> int('0x2a', 16)

# format(5, '04b')

# alist = [1,2,3,4,5]
# table = [[0],[1]]
# table[0] = [i for i in alist]
# print(table)