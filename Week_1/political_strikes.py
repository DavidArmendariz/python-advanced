#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N, K = [int(x) for x in input().split()]
strikes = []
for i in range(K):
    ai, bi = [int(x) for x in input().split()]
    days = [ai]
    i = 1
    while True:
        if (ai + i*bi) > N:
            break
        else:
            days.append(ai + i*bi)
        i += 1
    strikes.append(days)
holidays = []
i = 0
while True:
    if (6+7*i) > N:
        break
    else:
        holidays.append(6+7*i)
    if (7+7*i) > N:
        break
    else:
        holidays.append(7+7*i)
    i += 1
set_days = set(strikes[0])
for i in range(1, len(strikes)):
    set_days.update(strikes[i])
set_days.difference_update(holidays)
print(len(set_days))

