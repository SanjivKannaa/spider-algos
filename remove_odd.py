for ____ in range(int(input())):
    l = [i+1 for i in range(int(input()))]
    while len(l)>1:
        del l[0:len(l):2]
    print(l[0])


'''
while len(n)>1:
	for i in range(0,1+(len(n)//2), 2):
		n.pop(i)
'''