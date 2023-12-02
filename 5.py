def tricky_function(a,b=[],c={}):
    b.append(len(b))
    c[len(b)]=len(c)
    return a,b,c

print (tricky_function('X'))
print(tricky_function('Y'))

#('X', [0], {1: 0})
#('Y', [0, 1], {1: 0, 2: 1})