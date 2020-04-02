#!/usr/bin/env python
# coding: utf-8

# In[32]:


def modify_list(a):
    indexes = []
    # first, we capture the indexes of the odd elements to be removed
    for i in range(len(a)):
        if a[i] % 2 != 0:
            indexes.append(i)
    # now, we remove those indexes in reverse order
    for index in sorted(indexes, reverse=True):
        del a[index]
    # finally, we divide by two the even numbers
    for i in range(len(a)):
        if a[i] % 2 == 0:
            a[i] //= 2

