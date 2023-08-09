# Generate the 10000 random numbers 
import numpy as np
np.random.seed(14) # This guarantees the code will generate the same set of random numbers whenever executed
random_integers = np.random.randint(1,high=1000, size=(500))
#------[DO NOT MODIFY THE CODE ABOVE]--------------------------------------

print(random_integers[:100]) # Prints the first 100 numbers to get a sense for the data

def remove_greater_than(array, threshold):
    '''remove entries in `array' greater than `threshold' '''
    return array[array <= threshold]

def remove_less_than(array, threshold):
    '''remove entries in `array' less than `threshold' '''        
    return array[array >= threshold]

def remove_if_equal(array, value_list):
    '''remove entries in `array' that equal any value in `value_list' '''
    for v in value_list:
        array = array[array != v]
    return array

def remove_duplicates(array):
    '''remove duplicate entries in `array' leaving only one of each '''
    return np.unique(array)

# Filter the data
data = random_integers
data = remove_greater_than(data,800)
even_integers_through_1000 = np.arange(2, 1001, 2)
data = remove_if_equal(data,even_integers_through_1000)
data = remove_duplicates(data)

FILTERED_MEAN = np.mean(data)
FILTERED_MEDIAN = np.median(data)