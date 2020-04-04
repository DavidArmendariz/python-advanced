#!/usr/bin/env python
# coding: utf-8

# In[13]:


total_size, users = [int(x) for x in input().split()]
sizes = sorted([int(input()) for _ in range(users)])
used_space, users_stored = 0, 0
for size in sizes:
    if used_space + size <= total_size:
        used_space += size
        users_stored += 1
    else:
        break
print(users_stored)


# In[ ]:




