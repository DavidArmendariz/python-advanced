#!/usr/bin/env python
# coding: utf-8

# In[2]:


words = input().split()
scores = map(float, input().split())
result = filter(lambda x: x[0] > 0.5, zip(scores, words))
print(*map(lambda x: x[1], sorted(result, key=lambda x: (x[0],x[1]), reverse=True)), sep="\n")


# In[ ]:




