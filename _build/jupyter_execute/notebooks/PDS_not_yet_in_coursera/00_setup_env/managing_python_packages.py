#!/usr/bin/env python
# coding: utf-8

# # Managing Python Packages
# 
# Unlike in R (where you install packages from *within* R using the `install.packages()` command), Python packages have to be installed and managed from *outside* of Python on the command line. 
# 
# There are two major tools for installing and managing packages in Python: `conda` and `pip`. 
# 
# ### conda
# 
# Conda is the package management tool created by Anaconda, and is usually the place to start when you want to install something. 
# 
# To install a package using `conda`, go to your command line and type `conda install [name of package]`. i.e. if you want to install pandas, you would type `conda install pandas`. 
# 
# Conda will then evaluate what all it needs to install to give you `pandas`. This includes things like also installing packages that `pandas` relies on, or updating existing software you have installed to make it compatible with `pandas`. It will form a plan, then ask you if you want it to execute. It won't do anything till you say "yes". 
# 
# Conda can also be used to install specific version of packages (e.g. `conda install scipy=0.15.0`), remove packages (`conda remove [package]`), and update packages (`conda update [package name]`). You can see all software you have installed with `conda list`. 
# 
# **Environments:** Conda also supports what are called environments. An environment is like an isolated installation of Python living in a little bubble on your computer where you can experiment with packages without breaking your "working" installation, or have installations of different version of python, and more. We won't get into those here, but [you can read up if you'd like here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
# 
# ### pip
# 
# pip is the older python package manager, and there are still some packages you can install with pip you can't install with conda (though it is *much* more common to have a package you can't install with pip you can install with conda, which is why you should always start with conda). 
# 
# pip has a similar syntax to conda: just run `pip install [package name]` from the command line. 
