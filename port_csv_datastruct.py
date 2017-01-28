"""
port_csv_functions.py

example for parsing csv file and printing it's results
"""
import csv 
import json

# by adding a * before a param, it forces keyword params
def read_portfolio(filename, *, errors='warn'):
    '''
    Read a CSV file with name, date, shares, price data into a list.
    '''
    if errors not in { 'warn', 'silent', 'raise' }:
        raise ValueError("errors must be one of 'warn', 'silent' or 'raise'")
    portfolio = [] # List of records 
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
            # record = tuple(row)
            record = {
                'name' : row[0],
                'date' : row[1],
                'shares' : row[2],
                'price' : row[3]
            }
            portfolio.append(record)
    return portfolio 

portfolio = read_portfolio('Data/portfolio.csv')

#total = 0.0 
#for holding in portfolio:
#    total += holding['shares']  * holding['price']

#print('Total cost:', total)
data = json.dumps(portfolio) # parse maps into data
print(data)
port = json.loads(data) # take data and turn into json object

