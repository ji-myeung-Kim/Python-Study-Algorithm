a, b = input().split()
a = int(a)
b = int(b)
print(a + b)
print(a - b)
print(a * b)
# 파이썬의 경우 정수 둘을 나누었을 때 정확히 나누어 떨어지지 않으면
# 자동으로 'float'으로 처리하기 때문에 또 'int형'으로 명시해준다
print(int(a / b))
print(a % b)
