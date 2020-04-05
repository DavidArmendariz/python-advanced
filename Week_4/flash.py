#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Flash:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0

    def write(self, v):
        if v + self.size > self.capacity:
            raise ValueError
        else:
            self.size += v

