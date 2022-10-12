# n = input()
# n = "3[a2[bc]]"
n = "3[a]2[bc]"
# n = "2[3[4[abc]]]"
opsqrcnt = 0  # Open square count
tos = -1  # Top of the Stack
strp = 0  # string pointer
ourstk = []  # stack in operation
temp = []
final = []
while strp != len(n):
    # print(strp)
    ourstk.append(n[strp])
    strp += 1
    tos += 1

    if ourstk[tos] == "[":
        opsqrcnt += 1

    if ourstk[tos] == "]":
        ourstk.pop()  # ']' will be popped
        tos -= 1
        while opsqrcnt != 0:
            # print(ourstk)
            if ourstk[tos] == "[":
                opsqrcnt -= 1
                ourstk.pop()
                tos -= 1

                s = int(ourstk.pop())
                tos -= 1
                temp = temp*s
            # print(temp)
            else:
                s = ourstk.pop()
                tos -= 1
                temp.append(s)
            # print(ourstk)
            # print()

            # print(temp)

        temp = temp[::-1]
        for z in temp:
            final.append(z)
        temp.clear()


for fk in final:
    print(fk, end='')
