#!/usr/bin/env python
# coding: utf-8

# In[3]:


distances = sorted([int(x) for x in input().split()])
fares = sorted([int(x) for x in input().split()], reverse=True)
total = 0
for i in range(len(distances)):
    total += distances[i]*fares[i]
print(total)


# In[ ]:




