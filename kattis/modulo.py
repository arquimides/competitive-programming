map = {}
for i in range(10):
    map[int(input())%42] = 1
print(len(map))