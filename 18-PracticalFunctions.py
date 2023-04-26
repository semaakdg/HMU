#!/usr/bin/env python
# coding: utf-8

# In[1]:


def divide(number):
    return number / 2


# In[2]:


divide(10)


# In[3]:


my_list=[1,2,3,4,5,6,7,8]


# In[8]:


my_new_list = []
for num in my_list:
    my_new_list.append(divide(num))
print(my_new_list)    


# ## map

# In[11]:


list(map(divide,my_list))


# In[15]:


def control_string(string):
    return "Metallica" in string


# In[17]:


control_string("Metallica kdlfkd")


# In[22]:


my_artist_list = ["Metallica", "Madonna", "Queen", "Megadeth", "Muslum","Metallica2"]


# In[23]:


list(map(control_string,my_artist_list))


# ## filter

# In[24]:


list(filter(control_string,my_artist_list))


# ## lambda

# In[29]:


multiply = lambda number:number * 3


# In[32]:


multiply(5)


# In[33]:


my_list_3 = [3,5,7,9]


# In[34]:


list(map(lambda num:num*4,my_list_3))


# In[ ]:




