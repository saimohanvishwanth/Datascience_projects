#!/usr/bin/env python
# coding: utf-8

# # Strings

# In[23]:


#strings as array
e= ("you are not same")
print(e[3])

#string length
print(len(e))

#String Sclicing
print(e[1:18])
print(e[:5])
print(e[5:])
print([-1.-9])
print(e.upper())
print(e.strip())
print(e.replace('not',''))
print(e.split(','))


# ##String methods

# In[44]:


r= 'hi,This is Kumar here,is it D?'
print(r.capitalize())
print(r.casefold())
r.count("is")
r.encode()
r.endswith('?')
r.startswith('hi')
r.expandtabs(2)


# In[46]:


t='Yes Kumar,i came just now and what is you age{''} and at what time{''} will be available?'
t.format(23,3.40)


# In[47]:


h=('ram', 'krishna', 'parashuram')
x= '#'.join(h)
print(x)


# In[50]:


n={'blood_group':'o-ve','gender':'Male'}
t="TEST"
p=t.join(n)
print(p)


# In[56]:


r=t.ljust(20)
print(n,'then you are eligible')


# In[60]:


d='Hello'
s=d.ljust(20, 'o')
print(s)


# In[68]:


s= 'hello dam'
ri=s.maketrans('d','s')
print(s.translate(ri))


# In[76]:


f="i could eat all mangoes with in one day"
z=f.partition("lemons")
x=f.partition("mangoes")
print(z)
print(x)
c=f.replace("Mangoes","Watermelon")
print(c)
f.rfind('could')


# In[87]:


#rjust,rindex,rpartition,rsplit,rstrip,strpi Method()
h='banana'
t=h.rjust(30)
print(t,'is the staple food')
f=h.rjust(40, 'o')
print(f,'is the staple food in my region')
g='here the momos please have it'
c=f.rpartition('momos')
print(c)
v=f.rpartition('staple')
print(v)
b="moto,realme,xiomai"
l=b.rsplit(",",1)
print(l)
m="      maples    "
k=m.rstrip()
print('Canada is the place where ',m,'available very cheaply')
g.split()


# # spliting and joining of the string

# In[90]:


s="abhi"
a="sahil"
d= s +a
print(d)
x= s+" "+a
print(x)


# # LISTS

# In[27]:


s=['Tom','Jerry','Scobby','pokemon']
print(len(s))
print(s)
if 'Tom' in s:
    print('Yes','he is a person ')
s[2]='rahul'
print(s)
#insert
s.insert(4,'rohit')
print(s)
#append
s.append('madhu')
print(s)
#remove
s.remove('rohit')
s
#copy
a=s.copy()
a
#count
w=s.count(2)
w
#extend
a=[22,33,12,89]
s.extend(a)
s
#index
s.index(22)



# #stack:it is a type of datastructure where inserting and deletion of items take place at the end.Push adds an item to the top of the stack and pop removes an items at bottom of the stack

# In[31]:


stack=[22,3,45,74,43]
stack.append(34)
stack
stack.pop(3)


# Queue is the linear data structure where one element is inserted at one end and deleted from another end.
# Dequeue means to doublended Queue.first-in first-out

# In[40]:


from collections import deque
queue=deque([23,12,78,234,67,23])
queue.append(98)
print(queue)
queue.popleft()
queue


# looping inside the list

# In[43]:


r=[1,23,45,89,55]
s=[f**2 for f in r]
print(s)


# In[48]:


#with out loop comprehension
r=[1,2,3,4,5,6,7,8,9]
s=[]
for numbers in r:
    s.append(numbers**2)
print(s)


# In[58]:


s= 32
p= "\'please\' enter your age {}"
p.format(s)


# # Tuples

# In[63]:


g=(2,3,45)
max(g)
min(g)
len(g)
sum(g)


# # Sets

# In[68]:


#we can add or remove from the lists
#we can't do sclicing, indexing in Sets but converting in to list we can do that
s={1,2,4,6,7,8,4,5,6}
s.add('34')
#hre


# In[69]:


k={'monday','tuesday','wednesday','thursday','friday','saturday','sunday'}
print(k)
for i in k:
    print(i)


# In[73]:


k=set(['monday','tuesday','wednesday','thursday','friday','saturday','sunday'])
print(k)
for i in k:
    print(i)
    


# In[75]:


print(k)
print(k.add('may'))


# #removing sets
# 

# In[79]:


print(k)
print(k.discard('saturday'))


# Using union operator

# In[89]:


g={'ooni','peri','yamuna','demigod','canivorse'}
f={'demigod','rahul','hero','yamuna'}
g.union(f)
g.intersection(f)
g.difference(f)
g.issuperset(f)
g-f


# frozenset

# In[100]:


#we have to use dictionary, if weare using frozenset()
s={'Moni':'23','dog':'34','fried':'56','cow':'78','rohit':'43','druva':'23'}
print(type(s))
frozenset=frozenset(s);
print(type(s))
for i in frozenset:
    print(i)


# # Functions

# In[107]:


def print_hi():
    print('HI')

    
    print_hi()
    


# In[111]:


def interior(a,b):
    c= a+b
    print('this is the saple of the program')

    interior(4,5)
    


# In[113]:


def username():
    user=input("user: " )
    
    
username()


# In[114]:


f='pagala'
g='dewana'
h='desh'
def hyder():
    print(f,g,h)
    
hyder()


# In[116]:


def thing():
    g='hello, welcome everybody'
    print('goodevening' ,g)
          
thing()


# In[122]:


theygod = ['everybody']
def permission():
    theygod.append('local guys')
    
permission()
theygod


# In[130]:


def print_box(message):
    print('*'*len(message))
    print(message)


# In[132]:


def print_box(message, character='*'):
    print(character * len(message))
    print(message)
    print(character * len(message))


# In[133]:


print_box('hello world', "  ")


# In[135]:


print_box(message ='hello world')


# In[136]:


print_box('hello world', " ? ")


# In[137]:


print_box(message='keyworld', character=" ")
print_box(character=" " , message='keyworld')


# In[140]:


def gtevice(device):
    return device * 4
gtevice(3)

    


# In[144]:


def gtavicecity(cheatcodes):
    return cheatcodes * 5
gtavicecity(34) +gtavicecity(23)
print('2*5 is',gtavicecity(2))


# In[146]:


def intoralent(a,b):
    c=a+b
    return(c)
intoralent(4,6)


# In[149]:


def mignito(a,f,g):
    h=(a*f)/g
    return(h)
mignito(3,4.5,67)


# # Generator function

# In[157]:


def g():
    yield 13*23
    yield 21*23
    yield 35*56
for values in g():
    print(values)


# In[162]:


def generator_function():
    yield 1
    
    yield 2
    
    yield 3
    
s= generator_function()

print(s.__next__())
print(s.__next__())
print(s.__next__())


# # Lambda function

# In[165]:


#lambda pi ,p2 :expression
adder= lambda x,y:x+y
print(adder(1,2))


# In[170]:


s=lambda p,r,t : p*r*t
print('the simple interest is', s(1,2,4))


# In[173]:


s=lambda d,t:d/t
print('\nthe  resultant speed is',s(10,5))


# In[178]:


f=lambda m,n,e,r,t,s: s*m*n*e*r*t
print('the resultant is ', f(1,2,3,4,5,67))


# In[180]:


g='here the pokemon comes'
print(lambda g: print(g))


# # Map function

# In[6]:


def square(n):
    return n*n
d=[1,3,5,6,7,8,9]
f=map(square,d)
print(f)
print(list(f))


# In[8]:


def networth(p,t,r):
    return p*t*r/100
d=[10000,20000,34000,12100,3242,1231]
f=[23,23,1,21,12,11]
r=[2.1,3.1,5.6,2.3,7.2]
principal=map(networth, d,f,r)
print(principal)
print(list(principal))


# In[13]:


def rightowrong(distance,time):
    return distance/time
c=[23,34,45,68,90,112,345,234]
h=[4,5,6,12,24,6,8,22]
for x in map(rightowrong,c,h):
    print(x)


# # Python reduce

# In[30]:


#it is similary to map function but it on ly returns one iteration
import functools
def networth(p,t,r):
    return p*t*r/100
j=functools.reduce(networth, range(1,50,100))
print('the principal amount is ',j)


# # Python filter()

# In[42]:


def throif(var):
    f=['a','e','i','o','u']
    if (var in f):
        return True
    else:
        return False
sequence=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']
g=filter(throif, sequence)
print('filtered letters are')
for s in g:
    print(s)


# In[49]:


def brandnames(var):
    brand=['pepe jeans','polo','viswa','raymond','ramraj','kalyanlakshmi','lee','leecooper','louis phillipe']
    if (var in brand):
        return True
    else:
        return False

total_brands = ['tom&jerry','fastrack','pepe jeans','manyavar','lee','louis philipe','ben','wrangler','redcape','rocky','viswa','kalyanlakshmi','hemarold']
available_brands=filter(brandnames,total_brands)
print('these are the brands that are available')
for d in available_brands:
    print(d)


# In[ ]:




