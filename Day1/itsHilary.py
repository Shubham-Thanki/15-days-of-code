n = int(input())
a = list(map(int, input().split()))
count = 0
slope = []
carry = 0
for i in range(1, n):
    if a[i] > a[i-1]:
        slope.append(1)
    elif a[i] < a[i-1]:
        slope.append(-1)
    else:
        pass
for i in range(len(slope)-1):
    if slope[i]+slope[i+1] == 0:
        count += 1

print(count)
