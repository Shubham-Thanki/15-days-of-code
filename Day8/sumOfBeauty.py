# n = int(input())
# nums = list(map(int, input().split()))
nums = [2, 4, 6, 4]
# nums = [1, 2, 3]
# nums = [3, 2, 1]
res = []
for i in range(1, len(nums)-1):
    preflag = True
    for j in range(0, i):
        if nums[j] >= nums[i]:
            preflag = False
    for k in range(i+1, len(nums)):
        if nums[k] <= nums[i]:
            preflag = False
    if (preflag):
        res.append(2)
        preflag = False
    else:
        preflag = True

    if (nums[i - 1] < nums[i] < nums[i + 1]) and preflag:
        preflag = True
        res.append(1)

# print(res)
print(sum(res))
