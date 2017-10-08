
# coding: utf-8

# In[ ]:

# Opening the file and reading the data
import pickle
with open('small_list.pickle', 'rb') as file:
    number_list = pickle.load(file)


# In[ ]:

# Calculate the mean from a list of numbers 


# In[ ]:

def calc_median(elem_list):
    elem_list.sort()
    length = len(elem_list)
    half_length = int(length / 2)
    
    # Even number of elements in list
    if length % 2 == 0:
        first = elem_list[half_length - 1]
        second = elem_list[half_length]
        median = (first + second) / 2
    
    else:
        median = elem_list[half_length - 1]
    
    return median


# In[ ]:

calc_median(number_list)

