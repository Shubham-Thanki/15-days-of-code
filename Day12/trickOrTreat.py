# n=int(input())
# nums=list(map(int,input().split()))
n = 6
nums = [6, 5, 7, 9, 2, 2]
nums.sort(reverse=True)
print(nums)
cost = 0
skip = 2
for i in range(len(nums)):
    if (skip == 0):
        skip = 2
        continue
    cost = cost+nums[i]
    skip -= 1
print(cost)
