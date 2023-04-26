#!/usr/bin/env python
# coding: utf-8

# ## class

# In[1]:


my_list = list()


# # instance & attribute

# In[2]:


# snake= my_string
# camel= myString


# In[52]:


class Musician():
    
    job = "musician"
    
    def __init__(self,name,age,instrument):
        self.name = name
        self.age = age
        self.instrument = instrument
        
    #Method
    
    def sing(self):
        print(f"We are the champions! {self.instrument}")


# In[53]:


my_musician = Musician("James", 50, "Guitar")


# In[54]:


my_musician.age


# In[55]:


my_musician.name


# In[56]:


my_musician.instrument


# In[57]:


my_musician.job = "singer"


# In[58]:


my_musician.job


# In[59]:


my_musician.sing()


# In[76]:


class DogYears():
    
    year_factor = 7
    
    def __init__(self,age=5):
        self.age = age
        self.age_multiplied = age * 7
    
    def calculation(self):
        return self.age * DogYears.year_factor


# In[77]:


my_dog = DogYears()


# In[78]:


my_dog.calculation()


# In[79]:


my_dog.age_multiplied


# # inheritance

# In[80]:


class Class1():
    
    def __init__(self):
        print("Class 1 created")
    
    def method_1(self):
        print("method 1")
    
    def method_2(self):
        print("method 2")


# In[81]:


my_instance = Class1()


# In[82]:


my_instance.method_1()


# In[83]:


my_instance.method_2()


# In[91]:


class Class2(Class1):
    
    def __init__(self):
        Class1.__init__(self)
        print("Class 2 created")
    
    def method_3(self):
        print("method 3")
        
    #override
    
    def method_1(self):
        print("method 1 override")


# In[92]:


my_instance_2 = Class2()


# In[93]:


my_instance_2.method_2()


# In[94]:


my_instance_2.method_3()


# In[96]:


my_instance_2.method_1()


# In[97]:


my_instance.method_1()


# # Polymorphism

# In[98]:


class Apple():
    
    def __init__(self,name):
        self.name = name
    
    def information(self):
        return self.name + " 100 calories"


# In[99]:


class Banana():
    
    def __init__(self,name):
        self.name = name
    
    def information(self):
        return self.name + " 200 calories"


# In[100]:


banana = Banana("banana")


# In[101]:


apple = Apple("apple")


# In[102]:


banana.information()


# In[103]:


apple.information()


# In[104]:


fruit_list = [banana,apple]


# In[105]:


for fruit in fruit_list:
    print(fruit.information())


# In[106]:


def get_info(fruit):
    print(fruit.information())


# In[107]:


get_info(banana)


# In[108]:


get_info(apple)


# In[ ]:




