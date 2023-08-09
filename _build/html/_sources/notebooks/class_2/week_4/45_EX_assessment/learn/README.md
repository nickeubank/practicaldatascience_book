# Assessment: filtering and querying a dataset

In data science we frequently need to filter data as we've previously discussed: remove missing or anomalous values, remove predictors/features from a dataset, remove redundant values, etc. Additionally, we often want to query the data, exploring subsets of the larger dataset that meet certain criteria. We'll see later in this specialization that Pandas offers many excellent tools for doing that, but they're based on principles we've discussed here around matrix and vector operations. We've also discussed summarization strategies in this course. Let's bring all of these pieces together and create some tools for filtering and querying our data.

The goal of this exercise is to create a set of functions that are able to:
1. Remove data from a dataset that are greater than a certain value
2. Remove data from a dataset that are less than a certain value
3. Remove specific values from a dataset
4. Remove duplicate values in a dataset

Once we have the functions to accomplish this, we'll apply this to a dataset.

The first step is to create the functions. To help get you started, skeleton code is provided in the file `assessment.py` 

Once you have built your functions to filter the data, generate tests to verify that each function is working properly.

Once that is complete, it is time to test your data. The dataset that we will use will be a set of integer values ranging from 1 to 1000 (the code is provided in `assessment.py` - do not change the random seed).

Your goal is to filter the data in the following ways:
1. Remove values greater than 800
2. Remove values less than 25
3. Remove values equal to even integers
4. Remove all duplicates

Lastly, summarize the remaining data after your filtering is complete by computing the MEAN and MEDIAN of the REMAINING DATA.

To run your tests, you can run the command below:
```
python -m pytest
```

Once you're confident in your solution, hit the 

A few test cases have been provided to get you started