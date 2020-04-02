#!/usr/bin/env python
# coding: utf-8

# In[29]:


N = int(input())
whitelist = set(range(1, N+1))
blacklist = set()
while True:
    question = input()
    if question == "HELP":
        break
    else:
        numbers = [int(x) for x in question.split()]
        numbers = set([x for x in numbers if (x <= N and x >= 1)])
    answer = input()
    if answer == "YES":
        whitelist.intersection_update(numbers)
    elif answer == "NO":
        blacklist.update(numbers)
        whitelist.difference_update(blacklist)
print(*sorted(whitelist), sep=" ")


# In[ ]:




