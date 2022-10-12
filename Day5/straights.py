# n = int(input())
# nums = list(map(int, input().split()))
nums = [2, 1, 5, 0, 4, 6]
# nums = [5, 4, 3, 4, 7]
# nums = [5, 4, 3, 2, 1]
flag = False
a, b = float('inf'), float('inf')
c = 0
for i in range(len(nums)):
    if nums[i] < a:
        a = nums[i]
    elif nums[i] != a and nums[i] < b:
        b = nums[i]
    if nums[i] > a and nums[i] > b:
        flag = True
        break
if flag:
    print('true')
else:
    print('false')
