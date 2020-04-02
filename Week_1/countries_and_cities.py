#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
countries = dict()
for i in range(n):
    info = input().split()
    country = info.pop(0)
    countries[country] = info
request_n = int(input())
requests = []
for i in range(request_n):
    requests.append(input())
for city in requests:
    for country, c in countries.items():
        if city in c:
            print(country)
            break

