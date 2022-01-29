#!/usr/bin/env python
# coding: utf-8

# In[4]:


#one d array
import numpy as np
a=np.array([1,2])
a


# In[6]:


#2d array
import numpy as np
a=np.array([[1,2],[3,4]])
a


# In[3]:


#3d array
import numpy as np
a=np.array([[[1,2],[3,4],[4,5]]])
a


# In[10]:


#shape()
g=np.array([1,2,3,4],dtype= int)
g.shape


# In[18]:


#an array of evenly spaced numbers
import numpy as np
a=np.arange(1,10)
b=np.arange(1,22)
print(a)
b


# In[23]:


#array of zeros 
import numpy as np
c=np.zeros(12)
c


# In[30]:


#array of zeros with including dtype and warning function
import numpy as np
import warnings
warnings.filterwarnings('ignore')
s=np.zeros(8 , dtype=float)
s


# In[31]:


#convert list in to array
v=['name',12,3.3,454]
d=np.array(v)
d


# In[37]:


#array from list to tuples
import numpy as np
f=[(1,2,3.3),[4,5,6,7]]
b=np.asarray(f)
b


# In[38]:


#slicing in numpy 
a=np.arange(13)
print(a)
s=slice(2,3,4.5)
a[2]


# In[51]:


import numpy as np
s=np.arange(14)
b=s[1 : 13 : 3]
b


# In[62]:


#adding of two array in numpy
a=np.array([1.1,2.3,4,5,67,898])
b=np.array([20,20,30,40,50,60])
c= np.ravel([a + b])
np.ravel(c)


# In[68]:


import numpy as np
l=np.arange(0,20,5)
print(l.shape)



# In[75]:


#Trignometry in numpy
import numpy as np
l=np.array([10,20,40,50,40])
print('sine of different angles')
print(np.sin(l))
print(np.cos(l))
print(np.tan(l))
print(np.tan(l)**2)


# In[97]:


#arranging arrays and shaping in to matrix
import numpy as np
a=np.arange(25,dtype=float).reshape(5,5)
print('first array')
a


# In[104]:


print('secound array')
h=np.array([1,2,3,4,5])
print(h)


# In[105]:


print('add two arrays')
print(np.add(a,h))


# In[114]:


print('subtraction of two arrays')
print(np.subtract(a,h))
print('mul of two arrays')
print(np.multiply(a,h))
print('dividing of two arrays')
print(np.divide(a,h))


# In[130]:


import numpy as np
s=np.array([[[2,9,6,7],[3,6,8,3],[1,5,8,3]]])
print('or array is ')
print(s)
print('aplying a min function again:')
print(np.min(a,0))
print(np.max(h,0))


# In[131]:


import numpy as np
arr=np.array([1,3,5,30],dtype=float)
g=arr.itemsize
g


# In[137]:


#np.sqrt()method
import numpy as np
arr1=np.sqrt([1,2,3,4,54,4,44,4])
arr2=np.sqrt([5,6.7,34,65,23,90,42])
print("squareroot of arr1: ",arr1)
print("squareroot of array2: ", arr2)


# In[146]:


#nupy sum() method : axis =0(up, down), axis=1(left, right)
import numpy as np
ar=[20,53,233,367,12,35]
print("sum of the arr",np.sum(ar,dtype=int))
print('sum of the arr(float32):',np.sum(ar,dtype=float))
print('/n sum of arr(axis=0)', np.sum(ar, axis=0))
print('/n sum of arr(axis=1)',np.sum(ar, axis=1))


# In[155]:


import numpy as np
y=np.arange(10).reshape(2,5)
print(k)


# In[ ]:




