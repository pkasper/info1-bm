
# coding: utf-8

# In[1]:


raise BlockingIOError("Test")


# In[3]:


try:
    raise BlockingIOError("Error: Test")
except BlockingIOError as ex:
    print(ex)


# In[8]:


try:
    open("/tmp/not_existing_file")
except NameError:
    print("NameError caught!")
except FileNotFoundError:
    print("Error: please provide a valid file!")
except OSError:
    print("OSError")
    raise
# don't catch all errors!!!
# except:
#     print("Caught all! :)")

else:
    print("test else")
finally:
    print("cleaning up")


# In[9]:


def funny_function(test):
    if True:
        # error
        raise SyntaxError("spelling not right")

try:
    funny_function("bla blub")
except SyntaxError:
    print("error found, change user")
finally:
    print("cleaning up this mess")
    


# In[14]:


def funny_function(test):
    if True:
        # error
        try:
            raise SyntaxError("spelling not right")
        except:
            print("just kidding")
            raise

try:
    funny_function("bla blub")
except SyntaxError:
    print("error found, change user")
else:
    print("everything running smoothly")
finally:
    print("cleaning up this mess")
    


# In[12]:


def funny_function(test):
    if True:
        # error
        try:
            print("all fine")
        except NameError:
            print("just kidding")
            raise

try:
    funny_function("bla blub")
except SyntaxError:
    print("error found, change user")
else:
    print("everything running smoothly")
finally:
    print("cleaning up this mess")
    
print(":)")


# In[15]:


def funny_function(test):
    if True:
        # error
        try:
            raise SyntaxError("spelling not right")
        except:
            print("just kidding")
            raise
        finally:
            print("oj oj oj")

try:
    funny_function("bla blub")
except SyntaxError:
    print("error found, change user")
else:
    print("everything running smoothly")
finally:
    print("cleaning up this mess")
    


# In[16]:


def myfunction(value):
    assert value < 100
    assert 0 < value
    return value**2


# In[17]:


myfunction(5)


# In[18]:


myfunction(1000)


# In[ ]:


def myfunction(value):
    assert value < 100
    assert 0 < value
    raise ValueError()
    return value**2

