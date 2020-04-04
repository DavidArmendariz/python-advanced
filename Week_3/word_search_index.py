#!/usr/bin/env python
# coding: utf-8

# In[18]:


import json

N = int(input())
words = sorted([input() for _ in range(N)])
search_index = dict()
for word in words:
    one_letter_prefix = word[0]
    two_letter_prefix = word[0] + word[1]
    if one_letter_prefix not in search_index:
        search_index.setdefault(one_letter_prefix, dict())
    search_index[one_letter_prefix][two_letter_prefix] =     search_index[one_letter_prefix].setdefault(two_letter_prefix, []) + [word]
output_file = input()
with open(output_file, "w") as file:
    json.dump(search_index, file)


# In[ ]:




