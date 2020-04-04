#!/usr/bin/env python
# coding: utf-8

# In[4]:


purchases = dict()
while True:
    line = input()
    if line == "":
        break
    customer, item, quantity = line.split()
    quantity = int(quantity)
    if customer not in purchases:
        purchases[customer] = {item: quantity}
    else:
        if item not in purchases[customer]:
            purchases[customer][item] = quantity
        else:
            purchases[customer][item] += quantity
customers_sorted = sorted(purchases)
for customer in customers_sorted:
    items_sorted = sorted(purchases[customer])
    print(f"{customer}:")
    for item in items_sorted:
        print(f"{item} {purchases[customer][item]}")


# In[ ]:




