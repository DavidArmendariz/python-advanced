#!/usr/bin/env python
# coding: utf-8

# In[ ]:


input_list = [int(x) for x in input().split()]
result_set = set()
for x in input_list:
    if x not in result_set:
        result_set.add(x)
        print("NO")
    else:
        print("YES")


# In[ ]:




