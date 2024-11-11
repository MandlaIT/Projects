#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np

def calculate(var):
    if len(var)  != 9:
        raise ValueError("List must contain nine numbers.")
    
    vals = np.array(var).reshape(3,3)
    calculations = {}
    
    for key, method in {
        'mean': 'mean',
        'variance': 'var',
        'standard deviation': 'std',
        'max': 'max',
        'min': 'min',
        'sum': 'sum'
    }.items():
        calculations[key] =[
            getattr(vals, method)(axis=0).tolist(),
            getattr(vals, method)(axis=1).tolist(),
            getattr(vals, method)()
        ]
    return calculations


# In[13]:


TestError = calculate([0,1,3,4,5,6,7,8])


# In[15]:


Test = calculate([0,1,2,3,4,5,6,7,8])
Test


# In[ ]:




