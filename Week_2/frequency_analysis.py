#!/usr/bin/env python
# coding: utf-8

# In[21]:


words  = dict()
while True:
    line = input()
    if line == "":
        break
    line = line.split()
    for word in line:
        words[word] = words.setdefault(word, 0) + 1
sorted_words = sorted(words, key=lambda x: words[x], reverse=True)
results = []
for word in sorted_words:
    if word in results:
        continue
    results += sorted([k for k, v in words.items() if v == words[word]])
print(*results, sep="\n")


# In[13]:




