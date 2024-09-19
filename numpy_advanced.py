#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a=np.array([1,2,3])
b=[4,7,8,12]
print(type(a))
print(a.shape)
print(b)
print(type(b))


# In[2]:


b=np.array([[1,2,3],[4,5,6]])
print(b.shape)
print(b[0,0],b[0,1],b[1,0])


# In[3]:


print(a[0],a[1],a[2])
a[0]=5
print(a)


# In[7]:


import numpy as np
a=np.zeros((2,2))
print(a)


# In[8]:


b=np.ones((1,2))
print(b)


# In[9]:


c=np.full((2,2),7)
print(c)


# In[10]:


d=np.eye(2)
print(d)


# In[11]:


e=np.random.random((2,2))
print(e)


# In[12]:


f=np.random.randint((2,2))
print(f)


# In[13]:


g=np.random.linspace
print(g)


# In[14]:


import numpy as np
np.linspace(2.0, 3.0, num=5)


# In[16]:


np.linspace(2.0, 3.0, num=5, endpoint=False)


# In[17]:


np.linspace(2.0, 3.0, num=5, retstep=True)


# In[18]:


a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b=a[:2,1:3]
print(b)


# In[21]:


c=a[:,:]
d=a[:2,1:3]
print(d)
print(c)


# In[26]:


#Assignment1


# In[24]:


e=a[0:2,1:2]
print(e)


# In[27]:


f=a[2:3,0:2]
print(f)


# In[29]:


g=a[:2,1:]
print(g)


# In[33]:


h=a[-3:-1,-2:-1]
print(h)


# In[32]:


i=a[-2:1,1:2]
print(i)


# In[34]:


a=np.array([[1,2],[3,4],[5,6]])
print(a[[0,1,2],[0,1,0]])


# In[36]:


a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
b=np.array([0,2,0,1])
print(b)


# In[37]:


import numpy as np
a=np.array([[1,2],[3,4],[5,6]])
bool_idx=(a>2)
print(bool_idx)


# In[39]:


print (a[bool_idx])


# In[40]:


print(a[a>2])


# In[41]:


x=np.array([1,2])
print(x.dtype)


# In[42]:


x=np.array([1.0,2.0])
print(x.dtype)


# In[44]:


x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])
print(x+y)
print(np.add(x,y))


# In[45]:


print(np.multiply(x,y))


# In[46]:


print(np.divide(x,y))


# In[47]:


print(np.sqrt(x))


# In[48]:


print(x*y)


# In[49]:


print(x/y)


# In[50]:


v=np.array([1,2,3])
print(v)
print(v.T)


# In[51]:


x=np.array([[1,2],[3,4]])
print(x)
print(x.T)


# In[52]:


import numpy as np
from numpy import linalg as LA
eigenvalues, eigenvectors = LA.eig(np.diag((1, 2, 3)))
eigenvalues


# In[53]:


eigenvectors


# In[ ]:




