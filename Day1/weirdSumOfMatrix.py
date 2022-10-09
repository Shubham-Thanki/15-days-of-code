r = int(input())
c = int(input())
matrix = []
res = []
nums = list(map(int, input().split()))
k = 0
for i in range(r):
    matrix.append(nums[k:k+c])
    k += c
# print(matrix)
for downcnt in range(r-2):
    sum = 0
    for rightcnt in range(c-2):

        # Top 3 elements
        sum = sum+matrix[downcnt][rightcnt] + \
            matrix[downcnt][rightcnt+1]+matrix[downcnt][rightcnt+2]

        # Middle element
        sum = sum+matrix[downcnt+1][rightcnt+1]

        # Bottom 3 elements
        sum = sum+matrix[downcnt+2][rightcnt] + \
            matrix[downcnt+2][rightcnt+1]+matrix[downcnt+2][rightcnt+2]
        res.append(sum)
        sum = 0
print(max(res))

# 4
# 4
# 6 2 1 3 4 2 1 5 9 2 8 7 4 1 2 9
