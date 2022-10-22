# n=(input())
n = "2345"
arr = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
temp = []
ans = []
if (len(n) == 1):
    print(arr[int(n)-2])
else:
    a = arr[int(n[0])-2]  # 2->0->"abc"
    b = arr[int(n[1])-2]  # 3->1->"def"
    temp = []
    for i in a:
        for j in b:
            temp.append(""+i+j)

remains = len(n)-2
idx = 2
ans = temp
while (remains != 0):
    ans = []
    for i in temp:
        for j in arr[int(n[idx])-2]:
            ans.append(""+i+j)
    remains -= 1
    idx += 1
    temp = ans
print(*(ans))
