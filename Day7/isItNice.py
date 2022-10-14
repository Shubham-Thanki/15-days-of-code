# n = int(input())
# nums = list(map(int, input().split()))
nums = [1, 3, 8, 48, 10]
n = 5
# nums = [3, 1, 5, 11, 13]
temp = []
maxi = 1
i = 0
j = 1
temp.append(nums[i])
while (i < len(nums)-1) and (j < len(nums)):
    flag = True
    # Comparing the elements here can be seen.
    print(nums[j], temp)
    for z in temp:
        if (nums[j] & z != 0):
            flag = False
    if (flag):
        temp.append(nums[j])
        j += 1
        if len(temp) > maxi:
            maxi = len(temp)
    else:
        temp.clear()
        i += 1
        temp.append(nums[i])
        j = i+1

print(maxi)
