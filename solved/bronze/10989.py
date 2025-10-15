import sys

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())

counts = [0] * 10001  
for _ in range(N):
    counts[int(readline())] += 1

for value in range(1, 10001):
    c = counts[value]
    if c:
        line = str(value) + "\n"
        for _ in range(c):
            write(line)