#!/usr/bin/env python
# coding: utf-8

# In[ ]:


first_line = input().split()
second_line = input().split()
xor = {('0', '1'): '1', ('1', '0'): '1', ('1', '1'): '0', ('0', '0'): '0'}
tuples = zip(first_line, second_line)
result = list(map(lambda x: xor[x], list(tuples)))
print(*result, sep=" ")

