N = int(input())    # 전체 사람의 수 N
p = []              # 각 사람의 몸무게와 키 튜플 저장 리스트

for i in range(N):  # 각 사람의 몸무게와 키를 튜플로 리스트에 저장
    x,y = map(int,input().split(' '))
    p.append((x,y))

for i in range(N):
    k=1                     # 기본 등수 = 1등
    for j in range(N):      # for문으로 모든 조합 비교
        # i번째보다 키와 몸무게가 모두 큰 j가 있을 때 등수 +1 (뒤로밀림)
        if p[i][0] < p[j][0] and p[i][1] < p[j][1]:
            k += 1
    print(k, end=" ")       # 등수 출력