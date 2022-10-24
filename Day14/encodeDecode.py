# n=int(input())
# words=list(map(str,input().split()))
# words = ["fruit", "freetime", "time", "me", "apple"]
# words = ["time", "me", "bell"]
# words = ["me", "time"]
words = ["p", "grah", "qwosp"]
ans = ""
temp = []
temp.append(words[0])
temptr = 0

for i in range(1, len(words)):
    flag = True
    curr = words[i]
    seen = temp[temptr]
    if (curr in seen):
        if (curr[-1] == seen[-1]):
            flag = False
    if (seen in curr):
        if (seen[-1] == curr[-1]):
            flag = False
            temp.pop()
            temp.append(words[i])
            temptr += 1
    if (flag):
        temp.append(words[i])
        temptr += 1

ans = "#".join(temp)
ans = ans+"#"
print(ans)
