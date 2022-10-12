n = input()
# n = "abccbaacz"
cdic = {}


def checkcnt():
    for i in cdic:
        if cdic[i] > 1:
            return i
    return 0


for i in n:
    if i not in cdic:
        cdic[i] = 1
    else:
        cdic[i] += 1
    # print(cdic)
    k = checkcnt()
    if k != 0:
        print(k)
        break
