def factorial(n):
    if (n == 1):
        return 1
    else:
        return n*factorial(n-1)


if (__name__ == "__main__"):
    r = int(input())  # m
    c = int(input())  # n
    k = factorial(r+c-2) // factorial(r-1) // factorial(c-1)
    print(k)
