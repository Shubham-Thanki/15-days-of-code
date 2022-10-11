n = 5
pref = [5, 2, 0, 3, 1]
res = []
res.append(pref[0])


def getXOR(idx):
    xor = res[0]
    for i in range(1, idx):
        xor = xor ^ res[i]
    return pref[idx] ^ xor


for i in range(1, n):
    k = getXOR(i)
    res.append(k)
print(res)
