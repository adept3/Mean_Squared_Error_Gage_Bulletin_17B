
# coding: utf-8

# In[24]:

import numpy as np


# In[25]:

def MSE_G(A, B, N):
    return 10**(A-(B*(np.log10(N/10.0))))


# In[26]:

def A(G):
    if abs(G) > 0.90:
        A = -0.52 + (0.30 * abs(G))
    else:
        A = -0.33 + (0.08 * abs (G))
    return A


# In[27]:

def B(G):
    if abs(G) > 1.50:
        B = 0.55
        return B
    else:
        B = 0.94 - (0.26 * abs (G))
        return B


# In[28]:

MSE_G(A(0.0),B(0.0),20)


# In[34]:

x = float(input("Enter Regional Skew: "))
y = int(input("Enter Regional Skew Record Length: "))
value = MSE_G(A(x),B(x),y)
print('The MSE with parameters', x, 'and', y, 'is', value, '.')


# In[ ]:



