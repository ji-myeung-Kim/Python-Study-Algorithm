# 첫번째풀이
# n = int(input())
# result = []

# def binary(n):
#     if n == 1:
#         result.append('1')
#     else:
#         binary(n//2)
#         result.append(str(n % 2))
    
#     return ''.join(result)

# 두번째풀이 : global 사용
n = int(input())
answer = ''

def binary(n):
    global answer
    if n == 1:
        answer += '1'
    else:
        binary(n//2)
        answer += str(n % 2)    
    return answer 

print(binary(n))


# 당연히 이렇게해도됨
# print(bin(int(input()))[2:])