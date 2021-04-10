N = int(input())

for _ in range(N):
    n, a, c = map(int, input().split())

    if n < a - c:
        print("advertise")
    elif n == a - c:
        print("does not matter")
    else:
        print("do not advertise")
