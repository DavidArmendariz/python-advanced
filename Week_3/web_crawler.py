#!/usr/bin/env python
# coding: utf-8

# In[69]:


import json
filename = input()
with open(filename) as file:
    data = json.loads(file.readline())
sites = []
def find_sites_recursively(data, url=""):
    if data == dict():
        sites.append(url[1:])
    else:
        for key in data:
            find_sites_recursively(data[key], f"{url}/{key}")
find_sites_recursively(data)
print(*sorted(sites), sep="\n")


# In[ ]:




