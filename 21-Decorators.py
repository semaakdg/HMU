#!/usr/bin/env python
# coding: utf-8

# In[1]:


def func(new_func):
    print("func started")
    new_func()
    print("func ended")


# In[2]:


def hello_func():
    print("hello world")


# In[3]:


func(hello_func)


# In[14]:


def new_func():
    print("new func")
    def new_func_2():
        print("new func 2")
    return new_func_2


# In[15]:


new_func()


# In[16]:


new_string = new_func()


# In[17]:


new_string()


# In[19]:


def decorator_function(func):
    
    def wrapper_function():
        
        print("wrapper started")
        
        func()
        
        print("wrapper stopped")
    
    return wrapper_function


# In[21]:


def func_new():
    print("hello world")


# In[23]:


example_function = decorator_function(func_new)


# In[25]:


example_function()


# In[30]:


@decorator_function
def func_new():
    print("hello world")


# In[31]:


func_new()


# In[ ]:




