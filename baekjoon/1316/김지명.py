n = int(input())
count = n

for i in range(0, n):
    word = input()
    for j in range(0, len(word)-1):
        # 한 글자가 연속 될 경우 pass
        if word[j] == word[j+1]:
            pass
        # 한 글자가 그 다음 글자부터 끝에 있는 글자안에 포함될 경우 연속되지 않은 글자로 지정
        # 후에 -1을 누적 
        elif word[j] in word[j+1:]:
            count -= 1
            break
print(count)