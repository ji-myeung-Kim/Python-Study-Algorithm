import sys

input = sys.stdin.readline

N = int(input())

# 모든 요소가 0인 배열로 초기화
table = [[0 for _ in range(N)] for _ in range(N)]

# input 읽어서 배열에 넣기
for i in range(N):
    alist = list(map(int, input().split()))
    for j in range(len(alist)):
        if alist[j] == 0:
            table[i][j] = False
        else:
            table[i][j] = True


def answer(N, table):
    cnt = 0
    # 첫 째 줄 검사
    for i in range(len(table[0])):
        if table[0][i]:  # 자신의 불이 켜져있을 경우
            if i == 0:  # 맨 왼쪽 전구일 경우
                table[0][i + 1] = not table[0][i + 1]  # 오른쪽 전구 바꾸기
            elif i == (N - 1):  # 맨 오른쪽 전구일 경우
                table[0][i - 1] = not table[0][i - 1]  # 왼쪽 전구 바꾸기
            else:  # 둘 다 아닌 경우
                table[0][i + 1] = not table[0][i + 1]  # 오른쪽 전구 바꾸기
                table[0][i - 1] = not table[0][i - 1]  # 왼쪽 전구 바꾸기
            table[0][i] = not table[0][i]  # 자기 자신 바꾸기
            table[1][i] = not table[1][i]  # 아래 전구 바꾸기
            cnt += 1

    # 둘 째 줄부터 검사 - 바로 위 전구가 켜져있을 경우 스위치를 누른다.
    for i in range(len(table) - 1):
        for j in range(len(table[i])):
            if table[i - 1][j]:  # 위 전구의 불이 켜져있을 경우
                if j == 0:  # 맨 왼쪽 전구일 경우
                    table[i][j + 1] = not table[i][j + 1]  # 오른쪽 전구 바꾸기
                elif j == (N - 1):  # 맨 오른쪽 전구일 경우
                    table[i][j - 1] = not table[i][j - 1]  # 왼쪽 전구 바꾸기
                else:  # 둘 다 아닌 경우
                    table[i][j + 1] = not table[i][j + 1]  # 오른쪽 전구 바꾸기
                    table[i - 1][j] = not table[i - 1][0]  # 왼쪽 전구 바꾸기
                table[i][j] = not table[i][j]  # 자기 자신 바꾸기
                table[i - 1][j] = not table[i - 1][j]  # 위 전구 바꾸기
                table[i + 1][j] = not table[i + 1][j]  # 아래 전구 바꾸기
                cnt += 1

    for i in table[N-1]:
        if i:
            print(-1)
            return

    print(cnt)
    return


answer(N, table)






