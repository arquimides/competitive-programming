import sys

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())

resp = 0

for i in range(N):
    P = int(sys.stdin.readline())
    resp += X - P

print(resp + X)
