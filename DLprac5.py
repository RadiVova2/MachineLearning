
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])


# In[10]:


def sigmoid(x):
    return 1/(1+np.exp(-x))

A1 = np.dot(X,W1)+B1
Z1 = sigmoid(A1)
print(Z1)


# In[6]:





# In[7]:




