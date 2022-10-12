s = input()
mydic = {}
for i in range(len(s)):
    if (s[i] not in mydic):
        mydic[s[i]] = 1
    else:
        mydic[s[i]] += 1

for i in range(len(s)):
    if (mydic[s[i]] == 1):
        print(i)
        break
