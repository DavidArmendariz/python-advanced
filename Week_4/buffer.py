#!/usr/bin/env python
# coding: utf-8

# In[34]:


class Buffer:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.sequence = []

    def add(self, *a):
        for arg in a:
            self.sequence.append(arg)
            if len(self.sequence) == self.maxsize:
                print(sum(self.sequence))
                self.sequence.clear()
                
    def get_current_part(self):
        return self.sequence

