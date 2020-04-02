#!/usr/bin/env python
# coding: utf-8

# In[8]:


option = input()
parties = dict()
while True:
    x = input()
    if x == "VOTES:":
        break
    parties.setdefault(x, 0)
while True:
    x = input()
    if x == "":
        break
    parties[x] += 1
total = sum(parties.values())
for party, count in parties.items():
    if int((count/total)*100) >= 7:
        print(party)

