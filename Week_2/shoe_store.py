#!/usr/bin/env python
# coding: utf-8

# In[ ]:


foot_size = int(input())
sizes = sorted([int(x) for x in input().split()])

count = 0
previous_suitable_size = foot_size - 3

for size in sizes:
    if size >= previous_suitable_size + 3:
        previous_suitable_size = size
        count += 1
print(count)

