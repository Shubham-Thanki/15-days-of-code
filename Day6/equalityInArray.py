n = int(input())
nums = list(map(int, input().split()))
# n = 8
# nums = [1, 3, 5, 2, 4, 8, 2, 2]
# k = n//2


while len(nums) != 1:
    newnums = []*(len(nums)//2)
    for i in range(0, len(nums)//2):
        if i % 2 == 0:
            newnums.append(min(nums[2*i], nums[2*i+1]))
            # newnums[i] =
        else:
            newnums.append(max(nums[2*i], nums[2*i+1]))
            # newnums[i] =
        # print(newnums)
    nums = newnums
print(nums)
