
# coding: utf-8

# In[ ]:

# Creating a pickle file with lists
import pickle
from numpy.random import normal, binomial


# In[ ]:

# Generating the input lists with random variables from distribution
# Standard normal distribution
# Short
normal_dist_short = normal(0.0, 1.0, 100)
normal_short = normal_dist_short.tolist()

# Long
normal_dist_long = normal(0.0, 1.0, 1000000)
normal_long = normal_dist_long.tolist()


# In[ ]:

# Binomial distribution, n = 100, p = 0.9
# Short
binom_dist_short = binomial(100, 0.9, 100)
binom_short = binom_dist_short.tolist()

# Long
binom_dist_long = binomial(100, 0.9, 100000)
binom_long = binom_dist_long.tolist()


# In[ ]:

# Pickling the results    
result_list = [normal_short, normal_long, binom_short, binom_long]
list_names = ['normal_short', 'normal_long', 'binom_short', 'binom_long']

for item in range(4):
    filename = list_names[item] + '.pickle'
    with open(filename, 'wb') as file:
        pickle.dump(result_list[item], file)


# In[ ]:

# How to get the data from pickle file (example)
with open('binom_short.pickle', 'rb') as file:
    current_list = pickle.load(file)


# In[ ]:

current_list


# In[ ]:



