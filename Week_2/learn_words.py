#!/usr/bin/env python
# coding: utf-8

# In[6]:


N = int(input())
words = dict()
for n in range(N):
    word = input()
    length = len(word)
    words[length] = words.get(length, []) + [word]
for length in sorted(words):
    for word in sorted([x[::-1] for x in words[length]]):
        print(word[::-1])


# In[ ]:




