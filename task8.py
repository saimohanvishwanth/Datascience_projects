a= int(input('enter the value'))
b= int(input('enter another value'))
c= input('enter the operator')
if c == 'sum':
    d = a+b
    print(d)
elif c == 'sub' :
    e= a-b
    print(e )
elif c == 'multiply':
    f=a*b
    print(f)
elif c == 'divide':
    g = a/b
    print(g)
elif c == 'power':
    h =a^b
    print(h)
else:
    print("calculations are over or invalid, please try again")
         
