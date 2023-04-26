#!/usr/bin/env python
# coding: utf-8

# In[1]:


number = 10

def multiply(num):
    number = 5
    return num * number


# In[2]:


multiply(10)


# In[3]:


print(number)


# In[4]:


a = 10
a = 5


# In[5]:


print(a)


# # LEGB 
# 
# # L -> Local
# # E -> Enclosing
# # G -> Global
# # B -> Built-in

# In[1]:


my_string = "john"
#Global

def my_func():
    my_string = "James"
    #Enclosing
    
    def my_func_2():
        
        #Local
        my_string = "Lars"
        print(my_string)
        
    my_func_2()


# In[2]:


my_func()


# In[3]:


my_string


# In[4]:


y = 10

def func_new(y):
    print(y)
    y = 5
    print(y)
    return y


# In[5]:


func_new(10)


# In[6]:


y = func_new(y)


# In[7]:


y


# In[8]:


y = 10

def func_new():
    global y
    y = 5
    print(y)


# In[9]:


func_new()


# In[10]:


y


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




