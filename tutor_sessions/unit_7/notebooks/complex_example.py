CURRENT_INCOME = 2500 # how much we make right now
REMAING_YEARS = 40 # how many more years do we work
SAVING_RATIO = 0.15 # what rate of our income do we save?
BURN_RATE_PER_MONTH = 2300 # how much money do we need once retired?
INCOME_INCREASE = 1.03
INTEREST = 1.01

import sys
import matplotlib.pyplot as plt
import numpy as np

from retirement_model import calc_savings, calc_retirement_account

def main():
    # call function calc_savings and save the result to an array
    savings = np.array(calc_savings(CURRENT_INCOME, SAVING_RATIO,
        INCOME_INCREASE, REMAING_YEARS, INTEREST))
    
    # accumulate row 1 by reason of showing increasing income
    savings[:,1] = np.add.accumulate(savings[:,1])
    
    # call function calc_retirement_account and also save output to abs
    # numpy array
    total_savings = savings[-1, 1]
    retirement = np.array(calc_retirement_account(total_savings,
        BURN_RATE_PER_MONTH, INTEREST))
    
    curve = np.concatenate(
        (savings, retirement + (REMAING_YEARS, 0)), axis=0)
    #scale down cash
    curve[:, 1] *= (1/1000)
    #shift right the years, cause we don't want to start at 0
    curve[:, 0] += 1
        
    plt.plot(curve[:,0], curve[:,1], color='blue',
        linestyle='solid', label='savings')
    
    plt.plot(REMAING_YEARS, curve[REMAING_YEARS-1, 1], color='red',
        marker='p', linestyle='', label='quit job')
    
    plt.legend(numpoints=1)
    plt.xlabel('Years')
    plt.ylabel('Cash Balance [1.000 \u20AC]')
    plt.ylim((0, np.max(curve[:,1]) * 1.1))
    plt.grid()
    plt.show()
        
if __name__ == '__main__':
    sys.exit(main())