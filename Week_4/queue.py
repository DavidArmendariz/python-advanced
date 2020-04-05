#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Queue:
    def __init__(self):
        self.stack_push = []
        self.stack_pop = []
    
    def push(self, x):
        self.stack_push.append(x)
        self.stack_pop = [x] + self.stack_pop
    
    def pop(self):
        if len(self.stack_pop) == 0:
            raise IndexError("pop from an empty queue")
        element = self.stack_pop.pop()
        self.stack_push = self.stack_pop[::-1]
        return element
        

