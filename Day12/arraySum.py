n = int(input())
nums = list(map(int, input().split()))
k = int(input())
flag = False
for i in range(0, n-1):
    tot = 0
    for j in range(i+2, n+1):
        tot = sum(nums[i:j])
        if (tot % k == 0):
            flag = True
            break
if (flag):
    print("true")
else:
    print("false")
