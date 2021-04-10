def operation(v1, v2, sign):
    if v2 == 0 and sign == "/":
        return None
    if sign == "*":
        return v1 * v2
    if sign == "+":
        return v1 + v2
    if sign == "-":
        return v1 - v2
    if sign == "/":
        return v1 // v2


a, b, c, d = map(int, input().split())

signs = ["*", "+", "-", "/"]

sol = False

for i in range(4):
    s1 = signs[i]

    for j in range(0, 4):
        s2 = signs[j]

        if operation(a, b, s1) is not None and operation(c, d, s2) is not None and operation(a, b, s1) == operation(c,
                                                                                                                    d,
                                                                                                                    s2):
            sol = True
            print(str(a) + " " + s1 + " " + str(b) + " = " + str(c) + " " + s2 + " " + str(d))

if not sol:
    print("problems ahead")
