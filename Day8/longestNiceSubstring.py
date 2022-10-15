
# n = "YazaAay"
# n = "aAcdC"
# n = "abABB"
n = input()
# n = "aAcdC"
# n = "YazaAay"
res = ""


def isNice(x):
    for i in x:
        if (ord(i) < 91 and i.lower() not in x):
            return False
        elif (ord(i) > 96 and i.upper() not in x):
            return False
    return True


for i in range(len(n)):
    for j in range(i+1, len(n)+1):
        strng = isNice(n[i:j])
        if (strng):
            res = res+n[i:j]+";"


res = res.split(";")
maxlen = []
for i in res:
    maxlen.append(len(i))
print(res[(maxlen.index(max(maxlen)))])
