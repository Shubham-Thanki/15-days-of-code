n = int(input())
nums = list(map(int, input().split()))
hmap = []
flag = "false"
for i in nums:
    if i not in hmap:
        hmap.append(i)
    else:
        flag = "true"
        break
print(flag)
