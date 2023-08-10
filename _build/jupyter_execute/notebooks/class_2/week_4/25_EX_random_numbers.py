#!/usr/bin/env python
# coding: utf-8

# # Exercise 1: Calculating the mean and variance of common random variables
# Earlier we discussed summary statistics.
# 
# 1. Given what we discussed about the standard normal and uniform (between 0 and 1) distribution in the previous lesson, what would you anticipate the mean of each distribution was?
# 2. Generate 10,000 samples from a standard normal distribution using the `numpy` `randn` and `rand` methods and calculate their means to check your guesses

# In[4]:


import numpy as np

normal = np.random.randn(10000)
uniform = np.random.rand(10000)
print('Normal mean = ', np.mean(normal))
print('Uniform mean = ', np.mean(uniform))


# # Exercise 2: Phrase templates to randomly generate a story
# Using the list below randomly sample 5 words with replacement (duplicates are allowed). Then, randomly place them into the places indicated with blanks (i.e. "_____") in the following sentence (this will be a preview of an exercise to come later in this series):
# 
# "In eons past, there lived a wise woman who was very proud of the ancient _____ that she protected. When a village elder came to ask her advice on how to best ensure of strong harvest and offered her the _____ as an offering, her eyes opened wide and she shouted one word, "_______". She called the village together and for the next 100 days, at her urging, the villagers searched the forest for a ______. On the 101st day, the youngest child of the village found what they had been looking for and all rushed to the wise woman to give it to her. With a smile from ear-to-ear, and singing songs of celebration, the wise woman looked about her kinfolk and said, "Now has come the time of feasting - no one shall ever go without a _____ again!" There was much rejoicing."

# In[5]:


word_list =np.array(['SMALL BUT FEROCIOUS CAT','WORM OF EXTRAORDINARY SIZE','TWO-HEADED DRAGON','GREAT BEAR-BEAST','GHOST','WIZARD',
                     'BILLY GOAT','SASQUATCH','BARNACLE','HORSERADISH','SALMON','BLUEBERRY PIE','HAMBURGER','NEVERENDING-GOBLET','ALPACA','HUMMINGBIRD',
                     'BALLOON','LIGHTNING STRIKE'])


# An example of one possible output story would be:
# 
# >In eons past, there lived a wise woman who was very proud of the ancient APPLICATION that she protected. When a village elder came to ask her advice on how to best ensure of strong harvest and offered her the ANNOUNCEMENT as an offering, her eyes opened wide and she shouted one word, "VARIANT". She called the village together and for the next 100 days, at her urging, the villagers searched the forest for a BATTERY. On the 101st day, the youngest child of the village found what they had been looking for and all rushed to the wise woman to give it to her. With a smile from ear-to-ear, and singing songs of celebration, the wise woman looked about her kinfolk and said, "Now has come the time of feasting - no one shall ever go without EMPIRE again!" There was much rejoicing.

# 1. Create a function to pick random words from a list of words. 
#     - The function should take as inputs the list of words and the number of words you want to randomly pick from the list. 
#     - Draw random integers that represent the index of the words in the list and use those indices. Use `np.random.randint` to draw random numbers that correspond to the indices of the words in your list. For example, if you had a list that had 3 words ['this', that', 'other'], then your indices would be 0, 1, and 2, and you would want to randomly draw from those three possible values.
#     - Using the indices that you drew from your list and your knowledge of indexing techniques with `numpy` - select the words that correspond to those indices and return them from your function.
# 2. Test your function to ensure it outputs the correct number of words and that they appear to be randomly chosen words from the list
# 3. Format the text with blanks above into an f-string and insert the words into the string programmatically. Recall that an f-string allows you to integrate variables into your string with ease by allowing you to enclose variables you want to add to the string in brackets within the string. For an example see below:

# In[6]:


word = "(I'm the string!)"
number = 42
print(f"I want to insert a string here {word} and number {number}")


# 4. Lastly, run your code multiple times and see that the added words vary from run to run.

# In[7]:


import numpy as np

def pick_words(wordlist,numwords):
    # Determine how many words there are in the list
    N = len(wordlist)
    
    # Generate numword random integers between 0 and N-1
    random_indices = np.random.randint(0, high=N, size=numwords).astype(int)
    
    # Get the words using the indices you generated
    return word_list[random_indices]

# Get the words    
word = pick_words(word_list,5)

# Insert the words into the string and print it
print(f"In eons past, there lived a wise woman who was very proud of the ancient {word[0]} that she protected. When a village elder came to ask her advice on how to best ensure of strong harvest and offered her the {word[1]} as an offering, her eyes opened wide and she shouted one word, \"{word[2]}\". She called the village together and for the next 100 days, at her urging, the villagers searched the forest for a {word[3]}. On the 101st day, the youngest child of the village found what they had been looking for and all rushed to the wise woman to give it to her. With a smile from ear-to-ear, and singing songs of celebration, the wise woman looked about her kinfolk and said, \"Now has come the time of feasting - no one shall ever go without a {word[4]} again!\" There was much rejoicing.")

