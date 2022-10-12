n = input()
ans = []
stkptr = -1

# n = "3[a2[bc]]"
# 3,[,a,2,[,b,c=ans
for i in range(len(n)):
    if (n[i] != "]"):
        ans.append(n[i])
        stkptr += 1
    else:
        sbstr = ''
        while (ans[len(ans)-1] != "["):
            sbstr = sbstr+ans.pop()
        ans.pop()
        numstr = ''
        while (ans and ans[len(ans)-1].isdigit()):
            numstr = numstr+ans.pop()
        numstr = numstr[::-1]
        sbstr = int(numstr)*sbstr
        # sbstr = sbstr[::-1]
        ans.append(sbstr)

# ans = ans[::-1]
for i in ans:
    print(i[::-1], end='')
