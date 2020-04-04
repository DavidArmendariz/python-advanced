#!/usr/bin/env python
# coding: utf-8

# In[29]:


from json import loads, JSONDecodeError
filename = input()
correct_status_200 = 0
correct_status_not_200 = 0
status_not_int = 0
no_status = 0
bad_lines = 0
with open(filename) as json_file:
    for line in json_file:
        try:
            log = loads(line)
        except JSONDecodeError:
            bad_lines += 1
        else:
            status = log.get("status")
            try:
                status = int(status)
            except ValueError:
                if status == "":
                    no_status += 1
                else:
                    status_not_int += 1
            except TypeError:
                no_status += 1
            else:
                if status == 200:
                    correct_status_200 += 1
                else:
                    correct_status_not_200 += 1
print(*[correct_status_200, correct_status_not_200, status_not_int, no_status, bad_lines], sep="\n")


# In[ ]:




