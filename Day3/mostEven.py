n = int(input())
nums = list(map(int, input().split()))
# nums=nums[1:]
evdic = {}
res = []
final = -1

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        if nums[i] not in evdic:
            evdic[nums[i]] = 1
        else:
            evdic[nums[i]] += 1
maxi = max(evdic.values())
# print(evdic)
for i in evdic:
    if evdic[i] == maxi:
        res.append(i)

print(min(res))
