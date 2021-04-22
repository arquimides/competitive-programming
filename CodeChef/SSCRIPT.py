# https://www.codechef.com/APRIL21C/problems/SSCRIPT
# Example Input
# 3
# 5 2
# *a*b*
# 5 2
# *a**b
# 5 1
# abcde
# Example Output
# NO
# YES
# NO

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    S = input()
    count = 0
    for i in range(len(S)):
        if S[i] == "*":
            count = count+1
        else:
            count = 0
        if count == K:
            break
    if count == K:
        print("YES")
    else:
        print("NO")
