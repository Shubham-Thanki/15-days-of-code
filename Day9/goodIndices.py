# n = int(input())
# k = int(input())
# nums = list(map(int, input().split()))
n = 12
k = 2
nums = [1, 3, 3, 8, 8, 8, 9, 9, 9, 8, 8, 10]
# rflag=True
res = []
for i in range(k, n-k):
    flag = False
    lnums = nums[i-k:i]
    rnums = nums[i+1:i+k+1]
    if(sorted(lnums, reverse=True) == lnums) and (sorted(rnums) == rnums):
        flag = True

    if flag:
        res.append(i)
print(*res)
