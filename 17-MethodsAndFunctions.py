#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_string = "andrew"


# In[2]:


my_string_upper = my_string.upper()


# In[3]:


my_string


# In[4]:


my_string_upper


# In[5]:


help(my_string.split)


# In[6]:


def hello_world():
    print("hello")
    print("world")    


# In[7]:


hello_world


# In[8]:


hello_world()


# ## input & return

# In[9]:


def hello_programming(name):
    print("hello")
    print(name)


# In[10]:


hello_programming("Python")


# In[11]:


hello_programming("Java")


# In[12]:


def hello_program(name="python"):
    print("hello")
    print(name)


# In[13]:


hello_program()


# In[14]:


hello_program("java")


# In[15]:


def summ(number1,number2):
    number3 = number1 + number2
    print(number3)


# In[16]:


summ(5,8)


# In[17]:


summ(10,-500)


# In[18]:


def summation(num1,num2,num3):
    return num1+num2+num3


# In[19]:


summation(10,20,30)


# In[20]:


my_result = summation(10,20,30)


# In[21]:


my_result


# In[22]:


my_integer = summ(10,20)


# In[23]:


my_integer


# In[24]:


type(my_integer)


# In[25]:


def control_string(s):
    if s[0] == "m":
        print("mmm")


# In[26]:


control_string("paris")


# In[27]:


control_string("metallica")


# In[28]:


def control_string(s):
    if s[0] == "m":
        print(s.capitalize())


# In[29]:


control_string("metallica")


# In[30]:


control_string("amsterdam")


# ## arbitrary arguments & key word arguments

# In[31]:


def summation_2(*args):
    return sum(args)


# In[32]:


summation_2(10,20,30)


# In[33]:


summation_2(50,60,70,80)


# In[34]:


def my_func(*args):
    print(args)


# In[35]:


my_func(10,20)


# In[37]:


my_func("a","b",1,2)


# In[38]:


def example_func(**kwargs):
    print(kwargs)


# In[39]:


example_func(run=100,swim=200,basketball=300)


# In[40]:


example_func(a=1,b=2)


# In[41]:


def keyword_func(**kwargs):
    if "Metallica" in kwargs:
        print("Heavy Metalll!")
    else:
        print("Rock is dead!!")


# In[42]:


keyword_func(Metallica=10,Madonna=5,Muslum=4)


# In[43]:


keyword_func(Madonna=8,Mickey=4)


# In[ ]:





# In[ ]:





# In[ ]:




