from math import gcd
def get(x, l):
    return_list = []
    for i in range(len(l)):
        if l[i] == x:
            return_list.append(i)
    return return_list


n = int(input())
color = [0, 1]
for i in range(2, n):   # i => 1... n
    for j in range(max(color)): # checking which clr is free
        for clrnumber in get(j, list(color)):   # checking if its compatible
            if gcd(clrnumber, i) != 1:
                color.append(clrnumber)
                break
print(sum(list(set(color))))