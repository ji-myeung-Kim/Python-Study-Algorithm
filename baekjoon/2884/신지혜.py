H, M = map(int,input().split(" "))

if 45<=M<=59:
    print(H,(M-45))
else:
    if 1<=H<=23:
        print((H-1),(M+15))
    else:
        print(23,(M+15))