#!/usr/bin/env python
# coding: utf-8

# # Review of Matrices
# 
# ## Matrix Basics
# 
# - Like vectors, matrices are also a type of numpy array. Unlike vectors—which consist of data organized in a single dimension—matrices consist of data organized along two dimensions in a grid. 
# - Like all numpy arrays, matrices are *homogenously typed*, meaning the data they hold must always be of the same type.
# - All numpy arrays consist of a single-dimensional string of data and information on how that data should be "folded" to create an array. A vector is just data that is not folded, while a matrix is data that is folded into a grid. 
# - The shape of an array can be found in the `.shape` attribute.
# - How an array is folded can be modified with the `.reshape()` method.
# 
# ## Subsetting Matrices
# 
# - Subsetting matrices is just like subsetting vectors, except with two entries between the square brackets instead of one: `[ , ]`.
# - The first entry in the square brackets relates to a location along the x-axis (rows), the second to the y-axis (columns).
# - You must always pass two locations to subset a matrix. If you want all rows or all columns, simply pass a `:` (e.g., to get all of the columns in the first row, you would pass `my_matrix[0, :]`).
# - Like vectors, you can subset using simple indexing using index values or ranges. This will return a view.
# - Like vectors, you can also subset with fancy indexing or a Boolean vector.
# - You can mix how you subset, and use a Boolean for rows and an index for columns.
# - Subsetting on both rows and columns allows you to edit matrices in very powerful ways. 
