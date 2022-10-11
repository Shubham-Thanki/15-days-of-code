nums = list(map(int, input().split()))
# nums = [1, 2, 4]
# nums = [4, 4, 5]
sec = 0
# k = 8
while True:
    if nums.count(0) == 3:
        break
    nums.sort()
    if nums[1] != 0:
        nums[1] = nums[1]-1
    if nums[2] != 0:
        nums[2] = nums[2]-1
    sec += 1
print(sec)
