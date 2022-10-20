a = [2, 3, 5]
n = int(input())
uglynums = [0]*n
uglynums[0] = 1
idx2 = 0
idx3 = 0
idx5 = 0
for i in range(1, n):
    uglynums[i] = min(uglynums[idx2]*2,
                      min(uglynums[idx3]*3, uglynums[idx5]*5))
    if (uglynums[i] == uglynums[idx2]*2):
        idx2 += 1
    if (uglynums[i] == uglynums[idx3]*3):
        idx3 += 1
    if (uglynums[i] == uglynums[idx5]*5):
        idx5 += 1
print(uglynums[-1])
