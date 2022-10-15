# n = int(input())
# nums = list(map(int, input().split()))
nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
res = []
ndic = {}

# Creating a hash map
for i in range(len(nums)):
    if nums[i] not in ndic:
        ndic[nums[i]] = 1
    else:
        ndic[nums[i]] += 1

# Getting unique count values, and arranging them in ascending.
myset = set(ndic.values())
freq = sorted(myset)


# For each value in freq, the loop will fetch all the matching elements in nums, store them in temp,
# then arrange them in descending, and then append them in the res.
for z in range(len(freq)):
    temp = []
    for i in range(len(nums)):
        if (ndic[nums[i]] == freq[z]):
            temp.append(nums[i])
    temp.sort(reverse=True)
    for h in temp:
        res.append(h)
print(*res)
