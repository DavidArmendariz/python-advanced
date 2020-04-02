#!/usr/bin/env python
# coding: utf-8

# In[ ]:


words = dict()
result = []
while True:
    text = input()
    if text == "":
        break
    text = text.split()
    for word in text:
        if word not in words:
            words[word] = 0
        else:
            words[word] += 1
        result.append(words[word])
print(*result, sep=" ")


# In[ ]:




