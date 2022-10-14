s = input()
goal = input()
# s = "abcde"
# goal = "cdeab"
final = []

# final.append(s)
for i in range(-1, len(s)-1):
    k = i+1
    tempstr = ""
    for j in range(len(s)):
        tempstr = tempstr+s[k]
        k -= 1
    final.append(tempstr)

goal = goal[::-1]
if (goal in final):
    print("true")
else:
    print("false")
