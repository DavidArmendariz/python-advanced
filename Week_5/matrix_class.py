#!/usr/bin/env python
# coding: utf-8

# In[19]:


from copy import deepcopy
class MatrixSizeError(Exception):
    pass
class Matrix:
    # Part 1
    def __init__(self, matrix):
        row_length = len(matrix[0])
        for row in matrix:
            if len(row) != row_length:
                raise MatrixSizeError
        self.matrix = deepcopy(matrix)
    
    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)
    
    def __getitem__(self, index):
        return self.matrix[index]
    
    # Part 2
    def __eq__(self, other):
        if isinstance(other, Matrix):
            for i, row in enumerate(self.matrix):
                for j, _ in enumerate(row):
                    if row[j] != other[i][j]:
                        return False
            return True
        else:
            raise TypeError
    
    def size(self):
        return (len(self.matrix), len(self.matrix[0]))
    
    # Part 3
    def __add__(self, other):
        if isinstance(other, Matrix):
            if other.size() != self.size():
                raise MatrixSizeError
            new_matrix = deepcopy(self.matrix)
            for i, row in enumerate(self.matrix):
                for j, _ in enumerate(row):
                    new_matrix[i][j] += other[i][j]
            return Matrix(new_matrix)
        else:
            raise TypeError
                
    
    def __sub__(self, other):
        if isinstance(other, Matrix):
            if other.size() != self.size():
                raise MatrixSizeError
            new_matrix = deepcopy(self.matrix)
            for i, row in enumerate(self.matrix):
                for j, _ in enumerate(row):
                    new_matrix[i][j] -= other[i][j]
            return Matrix(new_matrix)
        else:
            raise TypeError
    
    # Part 4
    def __mul__(self, other):
        if isinstance(other, Matrix):
            if other.size()[0] != self.size()[1]:
                raise MatrixSizeError
            row_size = self.size()[0]
            col_size = other.size()[1]
            common_size = self.size()[1]
            new_matrix = [[0 for _ in range(col_size)] for _ in range(row_size)]
            for i in range(row_size):
                for j in range(col_size):
                    element = 0
                    for k in range(common_size):
                        element += self.matrix[i][k]*other[k][j]
                    new_matrix[i][j] = element
            return Matrix(new_matrix)
        else:
            raise TypeError
    
    # Part 5
    def transpose(self):
        row_size, col_size = self.size()
        new_matrix = [[0 for _ in range(row_size)] for _ in range(col_size)]
        for i in range(row_size):
            for j in range(col_size):
                new_matrix[j][i] = self.matrix[i][j]
        return Matrix(new_matrix)
                
    
    # Part 6
    def tr(self):
        if self.size()[0] != self.size()[1]:
            raise MatrixSizeError
        trace = 0
        for i, row in enumerate(self.matrix):
            for j, element in enumerate(row):
                if i == j:
                    trace += element
        return trace
    
    def det(self):
        if self.size()[0] != self.size()[1]:
            raise MatrixSizeError
        def find_determinant(matrix):
            temp = Matrix(matrix)
            if temp.size() == (1,1):
                return matrix[0][0]
            else:
                s = 0
                for j, element in enumerate(matrix[0]):
                    new_matrix = deepcopy(matrix)
                    for k, _ in enumerate(new_matrix):
                        new_matrix[k].pop(j)
                    new_matrix.pop(0)
                    s += element*((-1)**(j))*find_determinant(new_matrix)
                return s
        return find_determinant(self.matrix)

