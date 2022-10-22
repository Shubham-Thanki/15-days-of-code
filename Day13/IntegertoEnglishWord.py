unitdict = {"0": "", "1": "One", "2": "Two", "3": "Three", "4": "Four",
            "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine"}
tenzdict = {"0": "", "2": "Twenty", "3": "Thirty", "4": "Forty",
            "5": "Fifty", "6": "Sixty", "7": "Seventy", "8": "Eighty", "9": "Ninety"}
excepdict = {"0": "Ten", "1": "Eleven", "2": "Twelve", "3": "Thirteen", "4": "Fourteen",
             "5": "Fifteen", "6": "Sixteen", "7": "Seventeen", "8": "Eighteen", "9": "Nineteen"}


def getIntToEng(nums, x):
    ans = ""
    num_str = ""
    for i in nums:
        num_str = num_str+str(i)

    num_int = int(num_str)
    # print(num_int)
    # ans=unitdict[num_str[2]]#If the number is zero, ans will be asigned
    if(num_int == 0):
        return ans
    elif (num_int > 0) and (num_int < 10):
        # [1,9]
        ans = ans+unitdict[num_str[2]]+" "
    elif(num_int < 20):
        # [10,19]
        ans = ans+excepdict[num_str[2]]+" "
    elif(num_int < 100):
        # [20,99]
        ans = ans+tenzdict[num_str[1]]+" "+unitdict[num_str[2]]+" "
    else:
        # [100,999]
        ans = ans+unitdict[num_str[0]]+" Hundred "

        # To handle x10,x11,x12,x13,x14,x15,x16,x17.....
        if (num_str[1] == "1"):
            ans = ans+excepdict[num_str[2]]+" "
        else:
            ans = ans+tenzdict[num_str[1]]+" "+unitdict[num_str[2]]+" "

    ans = ans+x

    return ans


if __name__ == '__main__':
    # n = (input())
    n = "1000010"
    nums = []
    for i in n:
        nums.append(int(i))
    rmain = 12-len(nums)
    while (rmain > 0):
        nums.insert(0, 0)
        rmain -= 1
    z = 0
    arr_ptr = 0
    res = ""
    arr = ["Billion", "Million", "Thousand", ""]
    for i in range(4):
        k = getIntToEng(nums[z:z+3], arr[arr_ptr])
        res = res+k+" "
        z += 3
        arr_ptr += 1
    if (res == "    "):
        print("Zero")
    else:
        print(" ".join(res.split()))
