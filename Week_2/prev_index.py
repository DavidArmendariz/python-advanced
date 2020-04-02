#!/usr/bin/env python
# coding: utf-8

# In[3]:


words = []
while True:
    text = input()
    if text == "":
        break
    text = text.split()
    words += text
words_dict = dict()
results = []
for i in range(len(words)):
    if words[i] not in words_dict:
        results.append(-1)
        words_dict[words[i]] = i
    else:
        results.append(words_dict[words[i]])
        words_dict[words[i]] = i
print(*results, sep=" ")


# In[ ]:




