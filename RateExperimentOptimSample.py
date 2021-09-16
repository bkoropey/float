#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy.optimize import linprog

obj = [-1, -1, -1, -1, -1, -1]

lhs_ineq = [[1, -1, 0, 0, 0, 0],  # D1: 8-6 Summer
            [0, 1, 0, 0, 0, 0],  # D1: 8-6 Winter
            [0, -1, 0, 0, 0, 0],  # D2: 8-10 Winter
            [0, 0, 1, -1.35, 0, 0],  # D2: 8-10 Summer
            [0, 0, 0, -1, 0, 0],  #
            [0, 0, 0, 1, 0, 0],  #
            [0, 0, 0, 0, 1, -3.1],  #
            [0, 0, 0, 0, 0, -1],  # D3: All Day Winter
            [0, 0, 0, 0, 0, -1]]  # D3: All Day Summer

rhs_ineq = [ 9.02,  # D1: 8-6 Summer
            1,  # 
             0,  # 
             0,  # 
             -1,  # 
             2,  # 
             0,  # 
             -1,  # 
             4]  # 

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
              method="revised simplex")
print(opt)


# In[ ]:




