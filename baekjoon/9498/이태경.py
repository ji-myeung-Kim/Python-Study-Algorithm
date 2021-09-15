# 굳이 어렵게 표현하려다 어려번 틀렸다
# 차라리 쉽게 표현하니 금방 통과!
score = int(input())
if(100 >= score >= 90):
    print("A")
elif(90 > score >= 80):
    print("B")
elif(80 > score >= 70):
    print("C")
elif(70 > score >= 60):
    print("D")
else:
    print("F")
