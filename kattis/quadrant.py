# import sys
# 
# X = int(sys.stdin.readline())
# Y = int(sys.stdin.readline())
# 
# if(X > 0 and Y > 0):
#     print(1)
# elif(X < 0 and Y > 0):
#     print(2)
# elif(X < 0 and Y < 0):
#     print(3)
# else:
#     print(4)


import sys

sol = [1, 1, 2, 6, 4, 0, 0, 0, 0, 0, 0]

T = int(sys.stdin.readline())

for i in range(T):
    print(sol[int(sys.stdin.readline())])
