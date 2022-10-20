n = 4
nums = [2, 3, -2, 4]
# n = int(input())
# nums = list(map(int, input().split()))
res = []
if (n == 1):
    print(nums[0])
else:
    for i in range(n-1):
        for j in range(i, n):
            prod = 1
            print(nums[i:j])
            # for n=4
            # i->[0,2]
            # j->[i,3]
            # k->[i,j]
            for k in range(i, j+1):
                prod = prod*nums[k]
            res.append(prod)
    # print(res)

    print(max(res))
