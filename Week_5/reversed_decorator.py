#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from functools import wraps
def reversed_dec(func):
    @wraps(func)
    def inner(*args, **kwargs):
        return func(*reversed(args), **kwargs)
    return inner

