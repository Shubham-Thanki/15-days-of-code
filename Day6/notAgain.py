n = int(input())
nums = list(map(int, input().split()))
numdic = {}
cnt = 0
myset = set()
for i in range(n):
    if (nums[i] not in numdic):
        numdic[nums[i]] = 1
    else:
        numdic[nums[i]] += 1
for i in numdic:
    cnt += 1
    myset.add(numdic[i])

if (len(myset) == cnt):
    print('true')
else:
    print('false')
