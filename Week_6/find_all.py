#!/usr/bin/env python
# coding: utf-8

# In[28]:


import re
lines = list()
regexp = re.compile(r'<i>(.*?)</i>')
while True:
    line = input()
    if line == "":
        break
    lines += regexp.findall(line)
print(*lines, sep="\n")

