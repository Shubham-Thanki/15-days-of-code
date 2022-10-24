# n=int(input())
# k=int(input())
# nums=list(map(int,input().split()))
n = 7
k = 3
nums = [1, 2, 3, 4, 5, 6, 7]
idx = []
ans = [0]*n
for i in range(n):
    x = i+k
    if (x > n-1):
        x = abs(n-x)
    idx.append(x)
ptr = 0
for i in nums:
    ans[idx[ptr]] = i
    ptr += 1
print(ans)
