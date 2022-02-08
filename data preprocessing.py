#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pyforest')


# In[4]:


# here in the preprocessing detecting , filling and removing the null values.
import pyforest
data= pd.read_csv('housing_dataset.csv')
data


# In[5]:


display(data[data.ocean_proximity=='NEAR BAY'])


# In[11]:


#data visualization
import matplotlib.pyplot as plt
plt.barh(ind('ocean_proximity'),ind('population'),colors='b')
plt.xlabel('ocean_proximity')
plt.ylabel('population')
plt.gcf().set_size_inches(15,0)
plt.show()


# In[6]:


#(rows, columns): numpy
data.shape


# In[8]:


#checking null values

data.isna().sum()


# In[9]:


data.describe()


# In[10]:


#object antey string laga tesukovali
data.info()


# In[13]:


data.dtypes


# In[18]:


data


# In[21]:


#import label encounter
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
#Encode the labels under Ocean proximity
data['ocean_proximity']=label_encoder.fit_transform(data['ocean_proximity'])
#converting  nearbay is 1 and inland is 0
data['ocean_proximity'].value_counts()


# In[30]:


data=data.drop(['median_house_value'],axis=1)
data


# In[29]:


data['total_bedrooms'].isna().sum()


# In[33]:


#here we are taking the null value column and taking the median and fill null value such that it may remove 'NaN'value
data['total_bedrooms'].median()


# In[36]:


data['total_bedrooms']=data['total_bedrooms'].fillna(value=435)
data


# In[37]:


data['total_bedrooms'].isna().sum()


# In[40]:


data.isna().sum()


# In[31]:


data['median_income'].mean()


# In[32]:


data['households'].median()


# In[41]:


data


# In[42]:


data.head()


# In[43]:


data.tail()


# In[64]:


data=data.replace('median_income','average_income_per_person', regex=False)
data
data['median_income']=data['median_income'].replace('',"M",regex=True)
data


# In[62]:


data=data.replace(['\$',""],'',regex=True)
data['median_income']=data['median_income'].replace('M',"lakhs ",regex=True)


# In[63]:


data['median_income']=pd.to_numeric(data['median_income'])
data.head()


# In[67]:


data.dtypes


# In[12]:


data


# In[ ]:





# In[34]:


#data visualization
plt.plot(data['population'], data['total_rooms'])
plt.title('comparision')
plt.xlabel('ocean_proximity')
plt.ylabel('population')
plt.show()


# In[36]:


plt.plot(data['population'],data['households'])
plt.title('comparision')
plt.xlabel('population')
plt.ylabel('households')
plt.legend()
plt.show()


# In[37]:


data.head()

