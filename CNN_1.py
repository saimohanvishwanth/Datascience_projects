#!/usr/bin/env python
# coding: utf-8

# # Create CNN model and optimize it using keras tuner

# In[75]:


get_ipython().system('pip install tensorflow')



# In[76]:


get_ipython().system('pip install keras')


# In[77]:


import tensorflow as tf
from tensorflow import keras
import numpy as np


# In[78]:


fashion_mnist = keras.datasets.fashion_mnist


# In[79]:


(train_images, train_labels),( test_images, test_labels)= fashion_mnist.load_data()


# we have to convert the grayscale images in to pixcels.for each pixcel range would be 0-255

# In[80]:


train_images = train_images/255.0
test_images = test_images/255.0


# for CNN we have to reshape the data

# In[81]:


train_images[0].shape


# In[82]:


train_images = train_images.reshape(len(train_images),28,28,1)
test_images = test_images.reshape(len(test_images),28,28,1)


# In CNN , we use keras.Sequential, under this we add conv2D layer along with flatten layer and dense layer. here in "hp.int" will create range of intergers where your min value is 64.

# In[87]:


def build_model(hp):
    model = keras.Sequential([
     keras.layers.Conv2D(
        filters = hp.Int("conv_1_filter", min_value = 32, max_value=128, step=16),
        kernel_size =hp.Choice("conv_1_kernel",values = [3,5]),
        activation = "relu",
        input_shape=(28,28,1)
        ),
        #secound dimensional 2D layer
        keras.layers.Conv2D(
        filters=hp.Int("conv_2_filter",min_value = 32, max_value =64, step=16),
        kernel_size=hp.Choice("conv_2_kernel",values= [3,5]),
        activation = "relu"
        ),
        # we are adding 2nd flatten layer
        keras.layers.Flatten(),
        keras.layers.Dense(
            units=hp.Int("dense_1_unts",min_value = 32,max_value =128, step=16),
            activation = "relu"
        ),
        # we are adding last Dense layer, activation we are using softmax where we get value in terms of probability
        keras.layers.Dense(10,activation ="softmax")
    ])
    #hp.choice is the learning rate
    model.compile(optimizer = keras.optimizers.Adam(hp.Choice("learning_rate", values = [1e-2, 1e-3])),
                  loss ="sparse_categorical_crossentropy",
                  metrics = ["accuracy"])
    return model


# In[88]:


from kerastuner import RandomSearch
from kerastuner.engine.hyperparameters import HyperParameters


# In[89]:


#now run the random search
tuner_search=RandomSearch(build_model,
                            objective ="val_accuracy",
                            max_trials=5,
                            directory ="output",project_name = "Mnist Fashion")


# In[ ]:


tuner_search.search(train_images,train_labels, epochs =3, validation_split =0.1)


# In[ ]:


model = tuner_search.get_best_models(num_models=1)[0]


# In[ ]:


model.sumary()


# In[ ]:


moel.fit(train_images, train_labels, epochs =10, validation_split =0.1, initial_epochs=3)

