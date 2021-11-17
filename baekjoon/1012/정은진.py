def ans(lists, x, y):
    global answer
    # temp = lists.pop()

    if (x, y-1) in lists:
        lists.remove((x, y-1))
        ans(lists, x, y-1)
        # answer += 1
    elif (x, y+1) in lists:
        lists.remove((x, y+1))
        ans(lists, x, y+1)
        # answer += 1
    elif (x-1, y) in lists:
        lists.remove((x-1, y))
        ans(lists, x-1, y)
        # answer += 1
    elif (x+1, y) in lists:
        lists.remove((x+1, y))
        ans(lists, x+1, y)
        # answer += 1
    # else:
    #     answer += 1
    #
    # if (temp[0], temp[1]-1) in lists:
    #     ans(lists)
    #     # answer.append((temp[0], temp[1]-1))
    #     # lists.remove((temp[0], temp[1]-1))
    # elif (temp[0], temp[1]+1) in lists:
    #     ans
    # else:
    #     answers.append(temp)

import sys
input = sys.stdin.readline

input()
input()

testl = list(tuple(map(int, input().split())))
print(testl)

# mydata = list(map(int, input().split()))
# print(mydata)

#
#
# testl = [(0, 0), (1, 0), (1, 1), (4, 2), (4, 3), (4, 5),
#          (2, 4), (3, 4), (7, 4), (8, 4), (9, 4), (7, 5),
#          (8, 5), (9, 5), (7, 6), (8, 6), (9, 6)]
# print(testl[2])
# answer = 0
#
# while len(testl)!=0:
#     temp = testl.pop()
#     ans(testl, temp[0], temp[1])
#     answer += 1
#
# print(answer)
