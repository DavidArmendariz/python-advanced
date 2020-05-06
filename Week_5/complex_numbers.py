#!/usr/bin/env python
# coding: utf-8

# In[6]:


import math
class Complex:
    # Part 1
    def __init__(self, re = 0, im = 0):
        if isinstance(re, (int, float)) and isinstance(im, (int, float)):
            self.re = re
            self.im = im
        else:
            raise TypeError

    def __str__(self):
        if self.im < 0:
            return f"{self.re}{self.im}i"
        else:
            return f"{self.re}+{self.im}i"
    
    # Part 2
    def __add__(self, other):
        if isinstance(other, (int, float)):
            re = self.re + other
            im = self.im
        elif isinstance(other, Complex):
            re = self.re + other.re
            im = self.im + other.im
        else:
            raise TypeError
        return Complex(re, im)
    
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            re = self.re - other
            im = self.im
        elif isinstance(other, Complex):
            re = self.re - other.re
            im = self.im - other.im
        else:
            raise TypeError
        return Complex(re, im)

    # Part 3
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            re = self.re * other
            im = self.im * other
        elif isinstance(other, Complex):
            re = self.re * other.re - self.im * other.im
            im = self.re * other.im + self.im * other.re
        else:
            raise TypeError
        return Complex(re, im)
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            re = self.re / other
            im = self.im / other
        elif isinstance(other, Complex):
            re = (self.re * other.re + self.im * other.im)/(other.re**2 + other.im**2)
            im = (self.im * other.re - self.re * other.im)/(other.re**2 + other.im**2)
        else:
            raise TypeError
        return Complex(re, im)

    # Part 4
    def __eq__(self, other):
        return self.re == other.re and self.im == other.im
    
    def __abs__(self):
        return math.sqrt(self.re**2+self.im**2)

