word = input()

count = 0
for i in range(len(word)-1):
    if word[i] != word[i+1]:
        count += 1
# 한번만 바뀌는 경우에 0이 나오므로 1을 더해준 후 정수만 뽑아낼 수 있도록 //로 처리
# ex 0000001에서 한번 바뀔경우 //2를 해버리면 0이 나오므로 +1을 하여 2를 만들어준 후
# 2로 나눌때 값이 나오도록 구성
print(count//2)

