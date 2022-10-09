n = int(input())
nums = list(map(int, input().split()))
idx = []

# Flag is used to not run the code when the no. of zeroes present is either 0 or 1.
flag = True


# Getting the index of 0's
for i in range(n):
    if nums[i] == 0:
        idx.append(i)

# print(idx)
if len(idx) < 2:
    print(n-1)
    flag = False


if flag:
    # Each element in this array is the count of the number of non-zero elements from the previous occuring 0
    # and the 0 present at the current index.
    diff = []
    diff.append(idx[0])
    for i in range(1, len(idx)):
        a = idx[i]-idx[i-1]-1
        diff.append(a)

    # This is written because of the presence of nonzero elements after last present 0 in the array.
    diff.append(n-idx[-1]-1)
    # print(diff)

# This array contains the number of non-zero elements if that particular 0 is removed.
    final = []
    for i in range(len(diff)-1):
        s = diff[i]+diff[i+1]
        final.append(s)
    # print(final)
    print(max(final))
