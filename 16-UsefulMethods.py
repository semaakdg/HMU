#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list = [1,2,3,4,5,6,7]


# In[ ]:





# In[2]:


for number in my_list:
    print(number)


# ## range

# In[3]:


range(20)


# In[4]:


list(range(20))


# In[5]:


for number in list(range(20)):
    print(number * 5 )


# In[9]:


for num in list(range(5,21,4)):
    print(num)


# ## enumerate

# In[15]:


index = 0
for number in list(range(5,15)):
    print(f"no: {number} ix: {index}")
    index += 1


# In[16]:


for element in enumerate(list(range(5,15))):
    print(element)


# In[17]:


for (index,number) in enumerate(list(range(5,15))):
    print(index)
    print(number)


# ## random

# In[18]:


from random import randint


# In[19]:


randint(0,1000)


# In[20]:


randint(0,1000)


# In[21]:


my_list_2 = list(range(0,10))


# In[22]:


my_list_2


# In[23]:


from random import shuffle


# In[24]:


shuffle(my_list_2)


# In[25]:


my_list_2


# ## zip

# In[26]:


sport_list = ["run","swim","basketball"]


# In[27]:


calories_list = [100,200,300]


# In[28]:


day_list = ["monday","tuesday","wednesday"]


# In[32]:


new_list = list(zip(sport_list,calories_list,day_list))


# In[33]:


new_list


# In[34]:


for element in new_list:
    print(element)


# ## list advanced

# In[38]:


new_list = []
my_string = "metallica"

for element in my_string:
    new_list.append(element)


# In[39]:


new_list


# In[40]:


new_list = [element for element in my_string]


# In[41]:


new_list


# In[47]:


new_list_2 = [number**5 for number in list(range(0,10))]


# In[48]:


new_list_2


# In[ ]:




