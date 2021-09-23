
def solution(brown, yellow):
    all = brown + yellow

    for h in range(1, all+1):
        if all % h == 0:
            w = all/h
            if w >= h:
                # print(w,h)
                if (w-2)*(h-2) == yellow :
                    return [int(w),h]

print(solution(10, 2))