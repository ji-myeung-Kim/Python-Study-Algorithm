n = int(input())
def hanoi(n, start, middle, end):
    print("n:", n, "start:",start, "middle:", middle, "end:",end)
    if n == 1:
        print("n:", n, "start:",start, "end:",end)
        print(start,"에서", end,"로 옮길래1" ,n)
    else:
        hanoi(n - 1, start, end, middle)
        print(start,"에서", end,"로 옮길거야2======",n - 1, start, end, middle )
        hanoi(n - 1, middle, start, end)
        # print(middle, "에서" ,end ,"로 옮길겡3")
sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
print(sum)
hanoi(n, 1, 2, 3)
