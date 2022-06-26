input()
l = [int(i) for i in input().split()]
values = dict()
for i in l:
    values[i] = set()
    for j in range(1, min(l)+1):
        if i%j == 0:
            values[i].add(j)

lst = list(values.values())
print(len(lst[0].intersection(*lst)))