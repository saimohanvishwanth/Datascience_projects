count =0
n = int(input('enter the number'))
for i in range(1, n+1):
    if n%i==0:
        count+=1
    if count == 2:
        print('primt numbers')
    else:
        print('not prime')