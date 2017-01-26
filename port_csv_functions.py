"""
port_csv_functions.py

example for parsing csv file and printing it's results
"""
import csv 
import glob

# by adding a * before a param, it forces keyword params
def portfolio_cost(filename, *, errors='warn'):
    '''
    Computes total shares * price for a CSV file with 
    name, date, shares, price data
    '''
    if errors not in { 'warn', 'silent', 'raise' }:
        raise ValueError("errors must be one of 'warn', 'silent' or 'raise'")
    total = 0.0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows) # skip the header row
        for rowno, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                if errors == 'warn':
                    # this kinda sucks - maybe a logging framework is better?
                    print('Row:', rowno, 'Bad row:', row)
                    print('Row:', rowno, 'Reason:', err)
                elif errors == 'raise':
                    raise # reraise the last exception
                else:
                    pass
                continue # skips to the next line
            total += row[2] * row[3]
    return total

# total = portfolio_cost('Data/portfolio.csv')
# print('Total cost:', total)

#files = glob.glob('Data/portfolio*.csv') # grab all files based on wildcard
#for filename in files:
#    print(filename, portfolio_cost(filename))

total = portfolio_cost('Data/missing.csv', errors='silent')
print('Total cost:', total)
