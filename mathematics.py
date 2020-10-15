#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
def add(a,b):
    c=a+b
    return c
def sub(a,b):
    d=a-b
    return d
def minc(a,b):
    e=min(add(a,b))
    return e
def maxc(a,b):
    f=max(add(a,b))
    return f
def sortc(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x


# In[ ]:




