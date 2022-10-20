# s=input()
# s = "cbacdcbc"
# s = "bcabc"
s = "acbacbdcbcd"


def getLastOccurrence(x):
    k = None
    for i in range(len(s)):
        if (s[i] == x):
            k = i
    return k


myset = set(s)
mylist = list(myset)
lstoccdic = {}
for i in mylist:
    idx = getLastOccurrence(i)
    lstoccdic[i] = idx
# print(lstoccdic)
ans = []
tos = -1
ans.append(s[0])
tos += 1

for i in range(1, len(s)):
    flag = True
    if (s[i] not in ans):
        while(True):
            if(s[i] < ans[tos]) and (lstoccdic[ans[tos]] > i):
                ans.pop()
                tos -= 1
                if (tos == -1):
                    break
            else:
                break
        ans.append(s[i])
        tos += 1
    else:
        pass

for i in ans:
    print(i, end='')
