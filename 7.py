def mystery_func(t):
    result=1
    for i in t:
        result *=i
    return result

t=(1,2,(2,3))
print(mystery_func(t))