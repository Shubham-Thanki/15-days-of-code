# n=int(input())
z = int(input())
# nums=list(map(int,input().split()))
nums = [1, 1, 1, 2, 2, 3]
mydic = {}
ans = []
for i in nums:
    if (i not in mydic):
        mydic[i] = 1
    else:
        mydic[i] += 1
sortedByVal = {k: v for k, v in sorted(
    mydic.items(), key=lambda v: v[1], reverse=True)}
# print(sortedByVal)
for k, v in sortedByVal.items():
    ans.append(k)
    z -= 1
    if (z == 0):
        break
print(ans)
