'''
for ____ in range(int(input())):
    s = input()
    count =[0, 0]
    for i in s:
        if i == "<":
            count[0] += 1
        else:
            count[1] += 1
    print(min(count))
'''

for ____ in range(int(input())):
    s = input()
    opened = 0
    closed = 0
    for i in s:
        if i == "<":
            opened += 1
        elif i == ">":
            closed += 1
        if closed > opened:
            opened, closed = min(opened, closed), min(opened, closed)
    print(opened + closed)