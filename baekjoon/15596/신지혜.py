# def solve(a: list) -> int

def solve(a):
    sum = 0
    # print(len(range(a)+1))
    for i in range(len(a)):
        sum += int(a[i])
    return sum