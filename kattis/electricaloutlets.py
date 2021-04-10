N = int(input())

for _ in range(N):
    line = input().split()
    p = int(line[0])
    values = [int(numeric_string) for numeric_string in line[1:]]
    print(sum(values) - p + 1)
