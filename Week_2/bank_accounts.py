#!/usr/bin/env python
# coding: utf-8

# In[13]:


accounts = dict()
results = []
while True:
    option = input()
    if option == "":
        break
    option = option.split()
    if option[0] == "DEPOSIT":
        account, amount = option[1], option[2]
        if account not in accounts:
            accounts[account] = int(amount)
        else:
            accounts[account] += int(amount)
    elif option[0] == "WITHDRAW":
        account, amount = option[1], option[2]
        if account not in accounts:
            accounts[account] = -int(amount)
        else:
            accounts[account] -= int(amount)
    elif option[0] == "BALANCE":
        account = option[1]
        if account in accounts:
            results.append(accounts[account])
        else:
            results.append("ERROR")
    elif option[0] == "TRANSFER":
        sender, receiver, amount = option[1], option[2], option[3]
        if sender not in accounts:
            accounts[sender] = -int(amount)
        else:
            accounts[sender] -= int(amount)
        if receiver not in accounts:
            accounts[receiver] = int(amount)
        else:
            accounts[receiver] += int(amount)
    elif option[0] == "INCOME":
        p = int(option[1])/100
        for client, amount in accounts.items():
            if amount >= 0:
                accounts[client] += int(p*amount)
print(*results, sep="\n")


# In[ ]:




