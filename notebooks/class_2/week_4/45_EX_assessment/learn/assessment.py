# Generate the 10000 random numbers [DO NOT MODIFY THIS CODE]
import numpy as np
np.random.seed(14) # This guarantees the code will generate the same set of random numbers whenever executed
random_integers = np.random.randint(1,high=1000, size=(500))

#Insert your own code below here

print(random_integers[:100]) # Prints the first 100 numbers to get a sense for the data. Feel free to delete this

#this is the skeleton code from the question prompt above
def remove_greater_than(array, threshold):
    '''remove entries in `array' greater than `threshold' '''
    pass

def remove_less_than(array, threshold):
    '''remove entries in `array' less than `threshold' '''        
    pass

def remove_if_equal(array, value_list):
    '''remove entries in `array' that equal any value in `value_list' '''
    pass

def remove_duplicates(array, value_list):
    '''remove duplicate entries in `array' leaving only one of each '''
    pass


# Use these exact variable names below for your filtered mean and median

# FILTERED_MEAN = ???
# FILTERED_MEDIAN = ???