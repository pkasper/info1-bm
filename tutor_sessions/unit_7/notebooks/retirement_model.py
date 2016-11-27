def calc_retirement_account(total_savings, monthly_burn_rate, interest):           
    """
        Calculates how long you can live from your savings
        
        The function returns a list of (year, cash_balance) tuples, where:
            year: a runnnig index, starting at 0
            cash_balance: the amount of cash you have after (years-1) years
                meant that the first tuple is like (0, 1000) because you still
                have 1000 in cash left
            The last tuple in the returned list has a negative cash_balance
    """
    return [(years, remaining) 
         for years, remaining 
         in enumerate(_retirement_generator(total_savings, monthly_burn_rate, interest))]
        
def calc_savings(income, ratio, income_increase, years, interest):
    """
        Calculates how much money you will yearly save to your bank account
        
        Returns a list of (year, savings) tuples, where:
            year: a running index, starting at 0
            savings: the amount of money you added to your bank account during
                that year
        Note: The sum of all savings is the amount of total savings at the
            end of the day
    """
    savings = [(year, interest**(years - year) * ((income*ratio) * 12))
        for year,income in _salary_generator(income, income_increase, years)]
    return savings
    

def _salary_generator(_base, _factor, _years):
    """Helper generator for calculate_savings"""
    current = _base
    
    for year in range(_years):
        yield year, current
        current = current * _factor
        
def _retirement_generator(_savings, _burn_rate, _interest):
    while True:
        _savings = (_savings - _burn_rate*12) * _interest
        yield _savings
        if _savings < 0:
            break
        