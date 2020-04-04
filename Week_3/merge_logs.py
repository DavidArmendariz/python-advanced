#!/usr/bin/env python
# coding: utf-8

# In[12]:


import json
filenames = input().split()
output = input()
lines = list()
for filename in filenames:
    with open(filename) as file:
        lines += list(map(lambda line: json.loads(line.rstrip()), file.readlines()))
lines.sort(key = lambda line: (line["date"], line["consumer_id"]))
with open(output, "w") as output_file:
    for line in lines:
        output_file.write(line["date"])
        output_file.write("\t")
        output_file.write(line["message"])
        output_file.write("\n")

