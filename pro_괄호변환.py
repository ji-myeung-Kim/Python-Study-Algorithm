def check(u):
    check = 0
    for char in u:
        if char == '(':
            check += 1
        else:
            check -= 1
        if check < 0:
            return False
    return True 

def solution(p):
    u = ''
    v = ''
    for i in range(1, len(p)+1):
        u = p[:i]
        v = p[i:]
        if u.count('(') == u.count(')'):
            break   

    if check(u) == True:
        if len(v) == 0:
            return u
        else:
            return u + solution(v)
    else:
        u = u[1:-1]
        u2 = ''
        dic = {'(':')', ')':'('}
        for char in u:
            u2 += dic[char]
        return '(' + solution(v) + ')' + u2



print(solution(')('))
