num1 = int(input())
num2 = input()
i=2

while(i > -1):
    print(num1 * int(num2[i]));
    i = i - 1

print(num1* ((int(num2[2])) + (int(num2[1])*10) + (int(num2[0])*100)))