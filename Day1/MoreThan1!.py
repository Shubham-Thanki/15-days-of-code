n = int(input())
nums = list(map(int, input().split()))
count = n//2
numdict = {}
for i in range(n):
    if nums[i] not in numdict:
        numdict[nums[i]] = 1
    else:
        numdict[nums[i]] += 1

for i in range(n):
    if numdict[nums[i]] > count:
        print(nums[i])
        break
