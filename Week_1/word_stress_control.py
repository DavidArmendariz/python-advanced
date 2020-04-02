#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N = int(input())
words = dict()
for _ in range(N):
    word = input()
    if word.lower() not in words:
        words[word.lower()] = [word]
    else:
        words[word.lower()] += [word]
text = input().split()
mistakes = 0
for word in text:
    lowercase_word = word.lower()
    if lowercase_word in words:
        if word not in words[lowercase_word]:
            mistakes += 1
    else:
        accents = [x for x in word if x.isupper()]
        if len(accents) != 1:
            mistakes += 1
print(mistakes)


# In[ ]:




