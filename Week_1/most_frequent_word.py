#!/usr/bin/env python
# coding: utf-8

# In[24]:


words = dict()
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
max_frequency = max(words.values())
mode = []
for key, val in words.items():
    if val == max_frequency:
        mode.append(key)
mode.sort()
print(mode[0])

