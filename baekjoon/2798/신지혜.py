N, M = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

b = []

def blackJack(a, cards, final):
    for i in range(cards):
        for j in range(i+1, cards):
            for k in range(j+1, cards):
                sum = a[i] + a[j] + a[k]
                if a[i] + a[j] + a[k] <= final:
                    b.append(sum)
    
    return max(b)

print(blackJack(a, N, M))
