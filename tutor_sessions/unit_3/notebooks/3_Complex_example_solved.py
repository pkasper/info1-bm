
# coding: utf-8

# In[ ]:

# Sample input: (x^2 - 6x + 5);  (4x^2 + 16x + 8)
def solve_quadr_equation(param_p, param_q):
    #1x2 = -(p/2) +- sqrt((p**2/4)-q)
    main_term = -(param_p / 2)
    root_pos = ((param_p ** 2)/4 - param_q) ** 0.5
    root_neg = root_pos * (-1)
    x_1 = round((main_term + root_pos), 2)
    x_2 = round((main_term + root_neg), 2)
    return (x_1, x_2)


# In[ ]:

x_1, x_2 = solve_quadr_equation(-6, 5)


# In[ ]:

x_1


# In[ ]:

x_2


# In[ ]:



