#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N = int(input())
d = dict()
for _ in range(N):
    words = input().split()
    d[words[1]] = words[0]
request = input()
for key, val in d.items():
    if key == request:
        print(val)
    if val == request:
        print(key)

