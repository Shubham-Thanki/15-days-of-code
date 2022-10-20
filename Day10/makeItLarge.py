nums = [3, 30, 36, 348, 9, 98, 43]
# nums = [3, 30, 34, 5, 9]
# nums = [5, 4, 3, 2, 1]

for i in range(len(nums)-1, -1, -1):
    for j in range(0, i):
        # print(nums[j], nums[j+1])
        a = str(nums[j])+str(nums[j+1])
        b = str(nums[j+1])+str(nums[j])
        if (int(b) > int(a)):
            nums[j], nums[j+1] = nums[j+1], nums[j]

ans = ""
for z in nums:
    ans = ans+str(z)
print(ans)
