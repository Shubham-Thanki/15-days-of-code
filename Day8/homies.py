n = int(input())
words = list(map(str, input().split()))
# n = 4
# words = ["Hello", "Alaska", "Dad", "Peace"]
rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
res = []
final = []
for i in words:
    idx = []
    for j in i:
        for k in range(3):
            if (j.lower() in rows[k]):
                idx.append(k)
    res.append(idx)

for i in range(len(res)):
    myset = set(res[i])
    if (len(myset) == 1):
        final.append(words[i])

print(*final)
