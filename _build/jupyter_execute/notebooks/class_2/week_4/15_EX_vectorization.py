#!/usr/bin/env python
# coding: utf-8

# # Exercise: Speeding up matrix operations
# 
# We just explored how to vectorize some simple array operations and the speed and syntactic benefits of doing so. Let's explore a related, but more challenging process: 2D matrix operations. Say that we have two matrices, $A$ and $B$ and we want to create a new matrix $C = A - B$ that is the element-wise difference between matrices $A$ and $B$. 
# 
# Let's assume these are all square matrices, so the number of rows equals the number of columns, and we'll call that value $N$. This implies the matrices are all the same general shape of $N \times N$:
# $$ A = \begin{bmatrix}
# a_{0,0} & a_{1,0} & \cdots & a_{0,N}\\
# a_{1,0} & a_{1,1} & \cdots & a_{1,N}\\
# \vdots & \vdots & \ddots & \vdots\\
# a_{N,0} & a_{N,0} & \cdots & a_{N,N}
# \end{bmatrix}$$ 
# 
# $$ B = \begin{bmatrix}
# b_{0,0} & b_{1,0} & \cdots & b_{0,N}\\
# b_{1,0} & b_{1,1} & \cdots & b_{1,N}\\
# \vdots & \vdots & \ddots & \vdots\\
# b_{N,0} & b_{N,0} & \cdots & b_{N,N}
# \end{bmatrix}$$
# 
# $$ C = \begin{bmatrix}
# c_{0,0} & c_{1,0} & \cdots & c_{0,N}\\
# c_{1,0} & c_{1,1} & \cdots & c_{1,N}\\
# \vdots & \vdots & \ddots & \vdots\\
# c_{N,0} & c_{N,0} & \cdots & c_{N,N}
# \end{bmatrix}$$
# 
# where $c_{i,j} = a_{i,j} - b_{i,j}$
# 
# Create matrices A and B by running the code below. In this case, $N = 1,000$ so there are 1 million elements in each matrix.

# In[1]:


import numpy as np
np.random.seed(88) # Set this random seed so the matrices will not change between runs
N = 1000
A = np.random.rand(N,N) # This creates an N x N matrix
B = np.random.rand(N,N)


# 2.  Create a function `diff_nonvectorized` that uses loops rather than vectorization to compute matrix $C$. You will need to use nested `for` loops for this solution

# In[9]:


def diff_nonvectorized(A,B):
    C = np.zeros(A.shape)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            C[i,j] = A[i,j] - B[i,j]
    return C


# 3. Next, create a function `diff_vectorized` that uses vectorization rather than loops to compute matrix $C$.

# In[10]:


def diff_vectorized(A,B):
    return A - B


# 4. Always test your code before applying it. Let's apply it to a toy example below with `A_toy` and `B_toy` so that we can calculate the output by hand and verify the result. If correct, your function should return a 2x2 matrix with all 1's.

# In[11]:


A_toy = np.array([[2,3],[4,5]])
B_toy = np.array([[1,2],[3,4]])


# In[12]:


diff_nonvectorized(A_toy,B_toy)


# In[13]:


diff_vectorized(A_toy,B_toy)


# 5. With the functions working, let's compare their speed. Apply each function to the actual data `A` and `B` and time the run, averaged over 5 runs. Below is the timing function from the last lesson to use for this exercise (adapted slightly to allow for two function arguments):

# In[14]:


import time

def timer(function,argument1,argument2,num_runs):
    total_time = 0
    # Rerun the code num_runs times
    for i in range(num_runs): 
        t0 = time.time() # Capture the initial time
        function(argument1,argument2) # Run the function we're timing
        t1 = time.time() # Capture the final time
        total_time += t1-t0
    return total_time / num_runs # Return the average across the runs


# In[17]:


num_runs = 5

time_nonvectorized = timer(diff_nonvectorized,A,B,num_runs)
time_vectorized = timer(diff_vectorized,A,B,num_runs)

print('Nonvectorized code took ',time_nonvectorized, 's')
print('Vectorized code took    ',time_vectorized, 's')
print('Vectorized code was ', time_nonvectorized/time_vectorized ,' times faster')


# 6. How much was the change in execution speed? How much coding was required for the vectorized versus the non-vectorized solution?
