# n = int(input())
# nums = list(map(int, input().split()))
nums = [2, 4, 6, 4]
# nums = [1, 2, 3]
res = []
for i in range(1, len(nums)-1):
    preflag = True
    for j in range(0, i):
        for k in range(i, len(nums)):
            if (nums[j] < nums[i] < nums[k]):
                preflag = False
                res.append(2)

    if (nums[i - 1] < nums[i] < nums[i + 1]) and preflag:
        preflag = False
        res.append(1)

    if (preflag):
        res.append(0)
print(res)
