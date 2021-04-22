# cook your dish here
T = int(input())
for _ in range(T):
    N,K = map(int, input().split())
    S = input()
    count = 0
    for i in range(S):
        if(S[i] == "*"):
            count = count+1
        else:
            count = 0
        if(count == K):
            break
    if(count ==  K):
        print("YES")
    else:
        print("NO")