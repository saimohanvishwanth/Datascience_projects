from datetime import datetime

name=input('enter your name:')
#Lists of items
lists= ''' 
Rice               Rs  20/kg
Sugar              Rs 30/kg
Oil                Rs 80/kg
Panner             Rs 75/kg
Onion              Rs 40/kg
Potato             Rs 30/kg
Tomato             Rs 25/kg
Colgatetooth paste Rs 50/kg
Maggi              Rs 50/kg
Icecream           Rs 60/kg
Complain           Rs 100/kg
Cadbury Chocolate  Rs 60/Unit'''
#declaration
price= 0
pricelist = []
totalprice =0
finalprice=0
ilist=[]
qlist=[]
plist=[]
# rates for items
items= {'Rice': 20, 'Sugar':30, 'Oil':80,'Panner':75,'Onion':40,'Potato':30,'Tomato':25,'Colgatetooth paste':50, 'Maggi':50,
        'Icecream': 60,' Complain' : 100, 'Cadbury Chocolate': 60}
option= int(input("for list of items press 1"))
if option ==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input('if you want  to buy press 1 or 2 for exit:'))
    if inp1==2:
        break
    if inp1==1:
        item=input('enter your items')
        quantity = int(input('enter your quantity'))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append(item, quantity, items, price)
            totalprice+= price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print('sorry there are not available')
    else:
        print('you have entered wrong number')
    inp = input('do you want to bill for these items? yes or no')
    if inp == 'yes':
        pass
        if finalamount !=0:
            print(25*'=','moni supermarket', 25*'=')
            print(28*'', 'warangal')
            for i in range(len(pricelist)):
                print(i,ilist[i],qlist[i],plist[i])
            print('totalamount:', 'Rs', totalprice)
            print('gst amount', 'Rs',gst)
            print(finalamount, 'Rs', finalamount)
        




 



 