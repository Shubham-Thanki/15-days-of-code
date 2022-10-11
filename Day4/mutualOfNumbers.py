n1 = int(input())
n2 = int(input())
x = min(n1, n2)
f = []
for i in range(1, x+1):
    if n1 % i == 0 and n2 % i == 0:
        f.append(i)
# print(f)
print(len(f))
