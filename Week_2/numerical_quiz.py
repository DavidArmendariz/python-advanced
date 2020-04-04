#!/usr/bin/env python
# coding: utf-8

# In[10]:


n = int(input())
words = [input() for _ in range(n)]
def decompose(x):
    return sum([int(x[i])-int(x[len(x)-i-1]) for i in range(len(x)//2)])
words.sort(key=lambda word: (decompose(word), abs(int(word))))
print(*words, sep="\n")

