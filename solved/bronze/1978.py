def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

N = int(input())
numbers = list(map(int, input().split()))

prime_count = 0
for num in numbers:
    if is_prime(num):
        prime_count += 1

print(prime_count)