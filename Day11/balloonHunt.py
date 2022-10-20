# n=input()
n = "loonbalxballpoon"
s = ['b', 'a', 'l', 'o', 'n']
# mydic = {}
arr = [0]*5
cnt = 0
for i in n:
    if(i == "b"):
        arr[0] += 1
    elif(i == "a"):
        arr[1] += 1
    elif(i == "l"):
        arr[2] += 1
    elif(i == "o"):
        arr[3] += 1
    elif(i == "n"):
        arr[4] += 1
    else:
        pass
while True:
    if (arr[0] == 0) or (arr[1] == 0) or (arr[4] == 0):
        break
    if (arr[2] < 2) or (arr[2] < 0):
        break
    arr[0] -= 1
    arr[1] -= 1
    arr[4] -= 1
    arr[2] -= 2
    arr[3] -= 2
    cnt += 1
print(cnt)
