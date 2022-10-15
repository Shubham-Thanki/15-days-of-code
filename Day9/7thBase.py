n = int(input())
nflag = False
if (n < 0):
    nflag = True
    n = abs(n)
res = ""
while(n > 0):
    k = n % 7
    res = res+str(k)
    n = n//7
res = res[::-1]
# print(res)
if (nflag):
    res = "-"+res
    print(res)
else:
    print(res)
