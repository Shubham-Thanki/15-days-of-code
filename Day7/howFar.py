s = input()
c = input()
# s = "loveleetcode"
# c = "e"
idx = []
final = []
for i in range(len(s)):
    if (s[i] == c):
        idx.append(i)
# print(idx)
for i in range(len(s)):
    temp = []
    for j in range(len(idx)):
        temp.append(abs(i-idx[j]))
    final.append(min(temp))

print(*final)
