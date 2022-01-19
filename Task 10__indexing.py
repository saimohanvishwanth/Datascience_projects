a= [1,2,3,4,55,6,78,8]
for x in a:
    if x==78:
        k=a.index(55)
        a[k] = ' '
        print(k)
