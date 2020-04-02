#!/usr/bin/env python
# coding: utf-8

# In[15]:


N = int(input())
conceived_numbers = set(range(1,N+1))
answers = []
while True:
    numbers_or_help = input()
    if numbers_or_help == "HELP":
        break
    numbers = [int(x) for x in numbers_or_help.split()]
    intersection = conceived_numbers.intersection(numbers)
    if len(intersection) <= (len(conceived_numbers) // 2):
        answers.append("NO")
        conceived_numbers.difference_update(numbers)
    else:
        answers.append("YES")
        conceived_numbers.intersection_update(numbers)
print(*answers, sep="\n")
print(*sorted(conceived_numbers), sep=" ")


# In[ ]:




