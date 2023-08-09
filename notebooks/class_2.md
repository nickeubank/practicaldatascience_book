# Class Two: Representing Data: Objects, collections, and their uses for computation (Numpy)

## Overall learning objectives (mapped to specialization learning objectives):
- Introduce data structures for representing data
- Learn programming practices (vectorization, subsetting) for matrices
- Describe the components and packages of the Python ecosystem

## WEEK ONE

(Drew and Genevieve on OOP, Sets, and Dicts)

## WEEK TWO @nickeubank

- Theme: Welcome to arrays and matrices, the foundational data structures for computation
- Learning objectives: 
  - Understand why arrays are key to data science; 
  - Arrays/matrices and the basic idea of 0, 1, 2, or 3+ dimensional collections
  - learn basics of subsetting and manipulating arrays

### Overview

- Data science stack: Python -> numpy -> pandas

### Data structures for computation (numpy)

- **Why numpy**
  - Easier to use for computational programming
  - Faster than equivalent operations using Python lists
  - Wide array of mathematical functions available in the library
  - Integrates nicely with many other computational and plotting packages

- **Importing Packages**
  - Remember how you saw `import` before? Here's some more cool tricks.
  - Packages, modules, and methods/functions
  - Import statements and the multiple ways of importing or referencing modules and functions
  - Aliases

- **Vectors**
  - Why vectors? 
    - For science, need multiple measurements of any outcome!
    - Timeseries data (you've seen before with heartrates, but here's as arrays not lists)
    - Collections of attributes representing a sample
  - What is vector? (single-typed, concept of order)
  - Vector math / operations (modelled [after this?](https://cm4ss.com/html/intro_to_vectors.html))
  - Subsetting vectors (by index, by logicals) (modelled [after this?](https://cm4ss.com/html/manipulating_vectors.html))
  - Editing vectors

## WEEK THREE @nickeubank

- **Views v. copies**
  - What is a view vs a copy
  - Shallow vs deep copies
  - When does a function return a view and when does it return a copy
 
- **Matrices**
  - Why matrices?
    - Often we want to measure different outcomes for the same units of analysis, so we can stack vectors to make a matrix
    - Many forms of data are inherently in a matrix form (i.e. imagery data)
      - Links back to "everything is a number" from D&G
    - There are computational benefits to vector operations (to be discussed later)
  - Matrix math ([modeled after this?](https://cm4ss.com/html/intro_to_matrices.html))
    - Common operations: transpose, dot products (vectors), matrix multiplication (a collection of dot products), and element-wise operations
  - Subsetting matrices: just 2 dimensional extension of vectors ([modeled after this?](https://cm4ss.com/html/manipulating_matrices.html))
    - Indexing: accessing individual elements, accessing subsets through slicing, logical indexing, fancy indexing
    - Reminders around views/copies

## WEEK FOUR @kylebradbury

- **How to summarize information in arrays?**
  - Counting, summing, averaging
  - Generating histograms

- **Vectorization**
  - Why does it matter?
    - Speed / efficiency
    - Keeps code more compact and legible for easier maintenance
    - It's how the math behind many techniques are represented (so easier to translate)
  - In practice
    - Demonstrate performance speedup through example [See example 2/3 of the way down](https://github.com/kylebradbury/python/blob/master/python_3.1_numpy.ipynb)
    - Solve your data problem using your best logic and practices, you can always add vectorization later to improve performance

- **Working with random numbers** (maybe here, maybe not?)
  - Why are random numbers useful?
  - How to generate random numbers using Numpy

### Package Management (maybe here maybe not?)

- pip / conda
- Environments: maybe not full tutorial, but demystify / overview
  - conda v. virtualenv v. pyenv
