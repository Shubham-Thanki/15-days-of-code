morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
         "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
# n = int(input())
# words = list(map(int, input().split()))
n = 4
words = ["gin", "zen", "gig", "msg"]
ans = []
for i in words:
    temp = ""
    for j in i:
        temp = temp+morse[ord(j)-97]
    ans.append(temp)
print(ans)
print(len(set(ans)))
