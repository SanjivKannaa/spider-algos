for ____ in range(int(input())):
    n = int(input())
    l = [i+1 for i in range(n)]
    while len(n)>1:
        for i in range(0, 1+(len(n)//2), 2):
            n.pop(i)
    print(l[0])
