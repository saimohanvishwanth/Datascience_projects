#!/usr/bin/env python
# coding: utf-8

# class Harish: # defination
#      age=20 #attribute
#      def display(self):#method
#         print('inside the class',self.age)
# 
# #obj creation
#  saketh=Harish()
#  saketh.display() # objectname.method()
#  kiran=Harish() # objectname=classname()
# kiran.display()
# 

# In[4]:


class don:
    age =20
    def display(self):
        print('inside the class',self.age)
s=don()
s.display()
f=don()
f.display()
        


# In[8]:


class timeanddistance:
    distance=float(input(''))
    time = float(input(''))
    speed = distance/(time*60)
    def display(self):
        print('the resultant speed is ',self.speed)
s= timeanddistance()
s.display()


# In[21]:


class fight:
    a=float(input(''))
    b=float(input(''))
    c=float(input(''))
    d=float(input(''))
    figther= a**d-b**c
    def display(self):
        print('the resultant A.P is',self.figther)
        
v=fight()
v.display()


# # using ___init__ constructor
# 

# In[ ]:


class Remo:
    def __init__ (self,a,b,c,d,e,f):
        self.w=a
        self.v=b
        self.s=c
        self.n=d
        self.m=e
        self.z=f
    def Output(self):
        print('enter the first alphabet',self.w)
        print('enter the first alphabet',self.v)
        print('enter the first alphabet',self.s)
        print('enter the first alphabet',self.n)
        print('enter the first alphabet',self.m)
        print('enter the first alphabet',self.z)
while True:
              v=input()
              d=input()
              g=input()
              h=input()
              i=input()
              j=input()
              dell=Remo(v,d,g,h,i,j)
              dell.Output()
            
              
              
              
              
        
        
        


# In[ ]:


class Rampo:
    def __init__(self,a,b,c,d,e,f):
        self.z=a
        self.x=b
        self.v=c
        self.n=d
        self.m=e
        self.o=f
    def Output(self):
        print('enter the student ID number',self.z)
        print('enter the student name',self.x)
        print('/nenter the student father name',self.v)
        print('enter the mobilenumber',self.n)
        print('enter class name', self.m)
        print('enter the course_name',self.o)
while True:
        s=int(input())
        g=input()
        h=input()
        j=int(input())
        k=input()
        l=input()
    
sop= Rampo(s,g,h,j,k,l)
sop.Output()

    


# ### 

# In[ ]:


class Supermarket:
    def __init__(self,q,w,e,r,t,y,u):
        self.a=q
        self.s=w
        self.d=e
        self.f=r
        self.g=t
        self.h=y
        self.j=u
    def Output(self):
        print('enter the sugar',self.a)
        print('enter the salt',self.s)
        print('enter the maggi',self.d)
        print('enter the boost',self.f)
        print('enter the complex',self.g)
        print('enter the colgate',self.h)
        print('enter the patanjali',self.j)
while True:
    z=input()
    c =input()
    v=input()
    b=input()
    n=input()
    m=input()
    x=input()
    
sangi=Supermarket(z,c,v,b,n,m,x)
sangi.Output()
    
    


# In[ ]:


num=0
for i in range(2,num):
    if num%i == 0:
        print('not prime')
else:
    print('prime')
   


# In[4]:


##Reading and writing the files
with open('hello.txt','w') as f:
    print('hello world!',file=f)
    f.closed


# In[7]:


lines=[]
with open('hello.txt','r') as f:
    for line in f:
        lines.append(line)


# In[10]:


with open('hello.txt','w') as f:
    print('how are you guys?',file=f)
    print('how are you?', file=f)
    print('i hope that you guys are doing great',file=f)
lines=[]
with open('hello.txt','r') as f:
    for lines in f:
        lines.append(l)


# In[15]:


stripped =[]
for l in f:
    stripped.append(l.rstrip('/n'))
    stripped


# In[19]:


with open('hello.txt','r')as f:
    ful=f.read()


# In[23]:


print(r'c:\user\pc\ hello.txt')


# In[26]:


open('hello.txt','r')


# # modules

# In[ ]:





# In[37]:


import mymodule
mymodule.greaky('vishwanth')


# # exceptional handling using-Try except

# In[ ]:


#these are used when your program exceutes an error, when these occur,the python intrepreter stops the current process untill it is called
#exceptions cna be handlied using Try()

