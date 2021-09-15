a, b, c = map(int, input().split())
print((a + b) % c)

# 연산순서에 유의하며 괄호 갯수를 잘 쳐주자!
print(((a % c) + (b % c)) % c)

print((a * b) % c)

# 연산순서에 유의하며 괄호 갯수를 잘 쳐주자!
print(((a % c) * (b % c)) % c)