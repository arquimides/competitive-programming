dictionary = {}

for number in range(1,10001):
    digit_sum = sum(map(int, str(number)))
    
    if digit_sum in dictionary:
        dictionary[digit_sum].append(number)
     
    else:
        dictionary[digit_sum] = [number]

L = int(input())
D = int(input())
X = int(input())

elements = dictionary[X]

min = False
max = False

for i in range(len(elements)):
    
    if not min and elements[i] >= L:
        N = elements[i]
        min = True
    if not max and elements[len(elements) - i - 1]<= D:
        M = elements[len(elements)-i-1]
        max = True
        
print(N)
print(M)