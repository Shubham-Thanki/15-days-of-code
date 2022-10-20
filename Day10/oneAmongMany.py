# n=int(input())
arr = [9, 9, 8, 7, 6, 5, 4, 3]
n = 2
i = 0
# prod = 9
sum = 10
for i in range(1, n):
    j = 0
    prod = 1
    while(j <= i):
        prod = prod*arr[j]
        j += 1
    sum = sum+prod
if (n == 0):
    print(1)
else:
    print(sum)
