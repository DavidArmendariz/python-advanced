#!/usr/bin/env python
# coding: utf-8

# In[6]:


class FlashError(Exception):
    pass

class FlashMaxFileSizeError(FlashError):
    pass

class FlashMemoryLimitError(FlashError):
    pass

class Flash:
    def __init__(self, capacity, max_file_size = None):
        self.capacity = capacity
        self.max_file_size = max_file_size
        self._size = 0

    def write(self, v):
        if self.max_file_size and v > self.max_file_size:
            raise FlashMaxFileSizeError
        if v + self._size > self.capacity:
            raise FlashMemoryLimitError
        self._size += v


# In[ ]:




