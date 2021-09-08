# a, b를 입력 받아 split으로 분할
# 파이썬은 입력 값을 문자열로 인식하기 때문에 int로 명시

a, b = input().split()
a = int(a)
b = int(b)
print(a + b)

# print(int(A) + int(B))
# 위 코드로 한방에 처리하자