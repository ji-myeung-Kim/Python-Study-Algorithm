import sys
sys.setrecursionlimit(10000)

def ans(lists, x, y):
    global answer

    if (x, y-1) in lists:
        lists.remove((x, y-1))
        ans(lists, x, y-1)
    elif (x, y+1) in lists:
        lists.remove((x, y+1))
        ans(lists, x, y+1)
    elif (x-1, y) in lists:
        lists.remove((x-1, y))
        ans(lists, x-1, y)
    elif (x+1, y) in lists:
        lists.remove((x+1, y))
        ans(lists, x+1, y)


input = sys.stdin.readline

testcase = int(input())
answers = []

for i in range(testcase):
    answer = 0
    graphlist = list(map(int, input().split()))
    testl = []

    for j in range(graphlist[2]):
        a, b = map(int, input().split())
        testl.append((a, b))

    while len(testl) != 0:
        temp = testl.pop()
        ans(testl, temp[0], temp[1])
        answer += 1

    answers.append(answer)

for i in answers:
    print(i)