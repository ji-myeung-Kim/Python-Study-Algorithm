n = int(input())

num = [1] * 10
for i in range(n-1):
    for j in range(1, 10):
        print("num[j] = ", num[j], "num[j-1] = ",num[j-1])
        num[j] += num[j-1]
        print(num)
        print("=================")

print(sum(num)%10007)
