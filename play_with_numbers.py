for __ in range(int(input())):
    n = int(input())
    i = int(n//2)
    print("*"*n)
    while i > 0:
        print(str("*"*i).ljust(n//2) + " " + str("*"*i).rjust(n//2))
        i -= 1
    i = 2
    while i <= n//2:
        print(str("*"*i).ljust(n//2) + " " + str("*"*i).rjust(n//2))
        i += 1
    print("*"*n)