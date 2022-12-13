#!/usr/bin/env python
# coding: utf-8

# In[6]:


""" 

Created by Saifullah Zadran

"""

import numpy as np

arr1 = np.random.randint (100, size = [6, 3])
print (arr1)

arr2 = np.random.randint (100, size = [1])
print (arr2)


arr3 = (arr1 * arr2)
print (arr3)


# In[7]:


arr1 = np.random.randint (20, size = [3, 2])
print (arr1)

arr2 = np.random.randint (20, size = [3, 1])
print (arr2)


arr3 = (arr1 * arr2)
print (arr3)


# In[9]:


arr1 = np.random.randint (20, size = [2, 1, 3])
print (arr1)

arr2 = np.random.randint (20, size = [2, 3])
print (arr2)


arr3 = (arr1 * arr2)
print (arr3)


# In[10]:


arr1 = np.random.randint (50, size = [5, 2])
print (arr1)

arr2 = np.random.randint (50, size = [2, 1])
print (arr2)


arr3 = (arr1 * arr2)
print (arr3)


# In[15]:


arr1 = np.random.randint (50, size = [5, 2, 4])
print (arr1)

arr2 = np.random.randint (50, size = [3, 1])
print (arr2)


arr3 = (arr1 * arr2)
print (arr3)


# In[ ]:




