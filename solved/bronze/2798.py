N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= M and sum > max_sum:
                max_sum = sum

print(max_sum)