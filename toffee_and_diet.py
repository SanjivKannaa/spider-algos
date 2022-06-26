def function(l, n):
    global values
    if n>1:
        for i in l:
            n -= 1
            values.append(i ^ function(l, n))
    else:
        for i in l:
            

values = []
print(function([1, 2, 3, 4, 5], 2))