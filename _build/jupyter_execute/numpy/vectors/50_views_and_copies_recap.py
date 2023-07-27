#!/usr/bin/env python
# coding: utf-8

# ## Review of Views and Copies
# 
# The last reading on views and copies covered a lot, so here's a brief summary of the key takeaways:
# 
# - When an array is subset using simple indexing (i.e., by passing an index or range of indices denoted with a `:`), the result is just a reference to the original array's data. This is called a *view*.
# - Because the view created through simple indexing is sharing data with the original array, changes to one will also impact the other.
# - While we often only refer to the newly created array as a "view," the relationship between the original array and the view is symmetric, meaning changes to either may impact the other (if the change impacts an entry that is shared).
# - When you create a subset using *fancy indexing* or Boolean subsetting with a logical test, numpy will create a copy, not a view.
# - A view can be converted into a copy with `.copy()`.
# - Creating a view is much faster than creating a copy; with that said, for most sizes of datasets you will encounter in life, both are exceedingly fast.
