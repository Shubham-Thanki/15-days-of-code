n = int(input())
nums = list(map(int, input().split()))
j = 0
res = []
sumu = 0

for i in range(n-1):
    for j in range(i, n):
        sumu = sum(nums[i:j+1])
        res.append(sumu)

if n == 1:
    print(nums[0])
else:
    print(max(res))
