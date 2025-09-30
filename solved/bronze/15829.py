N = int(input())
S = input()

result = 0
for i in range(N):
    result += (ord(S[i]) - 96) * (31 ** i)

print(result % 1234567891)