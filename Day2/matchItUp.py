rnote = input()
maga = input()
rdic = {}  # a:2
mdic = {}  # a:2,b:1
flag = "true"

# Creating rdic
for i in range(len(rnote)):
    if rnote[i] not in rdic:
        rdic[rnote[i]] = 1
    else:
        rdic[rnote[i]] += 1


# Creating mdic
for i in range(len(maga)):
    if maga[i] not in mdic:
        mdic[maga[i]] = 1
    else:
        mdic[maga[i]] += 1


flag = "true"
for i in rdic:
    if i in mdic:
        if rdic[i] <= mdic[i]:
            pass
        else:
            flag = "false"
            break
    else:
        flag = "false"
        break
print(flag)
