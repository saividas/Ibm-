#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
info=np.array(['p','a','n','d','a','s'])
print(info)


# In[6]:


import pandas as pd
x=['Python','Pandas']
df= pd.DataFrame(x)
print(df)


# In[8]:


import pandas as pd
import numpy as np
a=pd.Series(['java','c','c++',np.nan])
a.map({'java':'core'})


# In[ ]:


import pandas as pd
import numpy as np
a=pd.Series(['java','c','c++',np.nan])
a.map({'java':'core'})
a.map('I like{}')


# In[9]:


s=pd.Series(["a","b","c"],
name="vals")
s.to_frame()


# In[10]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
emp=['parker','john','smith','william']
id=[102,107,109,114]
emp_series=pd.Series(emp)
id_series=pd.Series(id)
frame={'Emp':emp_series,'ID':id_series}
result=pd.DataFrame(frame)
print(result)


# In[11]:


info={'IDI':[101,102,103],'Department':['B.sc','B.tech','M.tech']}
df=pd.DataFrame(info)
print(df)


# In[13]:


import pandas as pd
info={'one':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f']), 'two':pd.Series([1,2,3,4,5,6,7,8],index=['a','b','c','d','e','f','g','h'])}
d1=pd.DataFrame(info)
print(d1)


# In[ ]:


#Assignment Dictionary


# In[17]:


import pandas as pd
info={'name':['x','y','z'],'age':[4,5,6],'city':['Kolkata','Delhi','Chennai']}
pd.DataFrame(info)


# In[ ]:





# In[18]:


x=[['x','y','z'],[1,2,3]]
pd.DataFrame(x)


# In[21]:


import pandas as pd
info={'one':pd.Series([1,2],index=['a','b']), 'two':pd.Series([1,2,3],index=['a','b','c'])}
df=pd.DataFrame(info)
print(df)
print("Delete the first column:")
del df['one']
print(df)
print("Delete the another column:")
df.pop('two')
print(df)
print(df.loc['b'])


# In[29]:


x={'stud.name':['x','y','z','a','b','c','d','e'],
'stud.id':[1,2,3,4,5,6,7,8],'dept':['FET','FET','FOS','FMG','FET','FOS','FET','FMG'],
'Grade':[1,2,3,4,5,6,7,8]}
 
df=pd.DataFrame(x)


    


# In[30]:


#assignment - 3
import pandas as pd

# Create a dictionary with StudentName, StudentID, department, and Grade
student_data = {
    "StudentName": ["John", "Alice", "Bob", "Eve", "Charlie"],
    "StudentID": [101, 102, 103, 104, 105],
    "department": ["CS", "EE", "CS", "ME", "EE"],
    "Grade": ["Pass", "Pass", "Fail", "Pass", "Pass"]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(student_data)

# Retrieve values using department names
cs_students = df[df["department"] == "CS"]
ee_students = df[df["department"] == "EE"]
me_students = df[df["department"] == "ME"]

print("CS Students:")
print(cs_students)
print("\nEE Students:")
print(ee_students)
print("\nME Students:")
print(me_students)

# Retrieve the iloc of 2
second_row = df.iloc[2]
print("\nSecond Row:")
print(second_row)

# Retrieve the ID of the student
student_id = df.loc[2, "StudentID"]
print("\nStudent ID of second row:", student_id)


# In[35]:


import pandas as pd
lungcancer=pd.read_csv("C:\Lungcancer.csv")
print(lungcancer)
lungcancer.shape
lungcancer.info
lungcancer.head
lungcancer.tail
lungcancer.value_counts(dropna=False)



# In[36]:


lungcancer.value_counts(dropna=False)


# In[ ]:


lungcancer.apply(pd.Series)


# In[37]:


lungcancer.isnull()


# In[38]:


lungcancer.notnull()


# In[ ]:




