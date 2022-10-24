# n = int(input())
# k = int(input())
# nums = list(map(int, input().split()))
n = 6
k = 2
nums = [1, 2, 3, 1, 2, 3]
dic = {}
cnt = k
flag = False
for i in range(n):
    if (nums[i] not in dic):
        dic[nums[i]] = i
    else:
        j = i
        diff = abs(dic[nums[i]]-j)
        if (diff <= k):
            flag = True
        dic[nums[i]] = j
if (flag):
    print("true")
else:
    print("false")
