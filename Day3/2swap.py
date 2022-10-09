s = input()
goal = input()
goaln = []
flag = False

# if len(s)!=len(goal):
#     flag=False

k = 0
for i in s:
    if i != goal[k]:
        goaln.append(i)
    k += 1

# Given the equal input for example aab and aab, now since the inputs are equal we neeed at least one element whose
# count is greater than 2, because then we can swap it and we'll still be on goal, due to one mandatory swap.
if len(goaln) != 2:
    if len(goaln) == 0:
        for i in s:
            if s.count(i) >= 2:
                flag = True
else:
    flag = True

if flag:
    print('true')
else:
    print('false')
