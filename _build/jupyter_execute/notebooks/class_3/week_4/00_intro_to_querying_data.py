#!/usr/bin/env python
# coding: utf-8

# # Combining, grouping, and querying data

# ## Combining data
# Up to this point, we've assumed our data comes as a single table or file. While the data may need some cleaning up, they were loaded into one table or DataFrame. This is not always the case, since we frequently want to combined data from multiple sources. This week, we will explore different ways of combining data from across multiple sources and the `pandas` tools we can use to accomplish that. In particular, we'll explore how to:
# 1. **Concatenate**. Concatenate allows us to add rows or columns from one DataFrame to another. This could be useful if we have two datasets with medical patient data and and want to combine the two sets of patient datasets into one.
# 2. **Merge**. Merge allows us to combine the contents of two DataFrames. If we had two sets of patient data: one with data on recent vital signs records like heart rate, blood pressure, and temperature and a second set that contains past medical diagnoses (does the patient have asthma, anemia, etc.), and perhaps only some of the patients are contained in both. Merging is how we combine these datasets together into one.
# 
# ## Grouping data
# We will also discuss how efficiently group data based on the content of the columns of DataFrames using **Groupby**. With the `groupby` method, we split the dataset based on the contents of particular columns and perform calculations on those *groups* of data within the dataset, reporting summary values back for each group. For example, if we had the dataset mentioned above with patients' vital signs, perhaps we want to see what the typical heart rate was for patients with high blood pressure vs those with lower blood pressure. This can be efficiently accomplished through grouping our data appropriately.

# Many of the concepts we discuss in this section, and throughout this course, are similar to what you would encounter with a course on structured query language (SQL) or other relational database programming languages. In both cases we are managing datasets and trying to process them into the formats that are most useful for our application. As the process of manipulating data in these ways is a core prerequisite for being able to then analyze the data using statistical analysis or machine learning tools, these data management tools are critical to have in your programmer's toolkit.
# 
# ## Querying data
# The last topic we will cover in this course builds on a topic we have discussed in some detail previously, which is how to query data. **Queries** allow us to efficiently ask questions of our data. You are already familiar with the idea of asking questions of our data when we discussed subsetting in previous lessons. Those were queries of the data that allowed us to select subsets of data meeting specific criteria (e.g. what fraction of patients with high blood pressure also have high cholesterol? What fraction of patients with low cholesterol have high blood pressure?). While this is not a new concept, it is typically our end goal in combining or grouping data, so we discuss it again here. We will see that we can build quick textual expressions that allow us to compute complex queries on our data even more easily.
# 
# ## Examples of when these approaches are useful
# Merging data is a nearly ubiquitous task in data science. Imagine that you are a financial analyst, and you're trying to estimate the risk risk of default on a loan. You have one dataset that contains a list of loan applicants' credit history and another that contains their income. To make an informed decision, the analyst would need to *merge* the records of these two sets of data together. Alternatively, imagine you are a business analyst trying to evaluate trends throughout the year in sales, but the data on those transactions is divided up into monthly datasets. In this case, you would need to *concatenate* the data together into a single dataset before those trends could be evaluated. If that analyst wishes to then estimate the average sales by the seniority of each salesperson, they would need to *group* the data first by seniority to then calculate those group-specific sales values.
# 
# By the end of this week you will be able to combine datasets using the tools introduced in this section and query them using tools we've discussed previously and some new shortcuts introduced in this section to help you answer questions from the data.