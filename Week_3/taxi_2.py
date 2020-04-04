#!/usr/bin/env python
# coding: utf-8

# In[24]:


distances = sorted(enumerate(map(int, input().split())), key = lambda x: x[1])
fares = sorted(enumerate(map(int, input().split())), key = lambda x: x[1], reverse = True)
orders = sorted(zip(distances, fares), key = lambda x: x[0][0])
indices = map(lambda x: x[1][0], orders)
print(*indices, sep=" ")

