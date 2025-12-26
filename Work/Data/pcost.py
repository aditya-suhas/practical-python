import csv
import sys
def portfolio_cost(filename):
    amount=0
    with open(filename, 'rt') as f:
        next(f)
        rows = csv.reader(f)
        for line in rows:
            try:
                amount+= (float(line[1])*float(line[2]))
            except ValueError:
                print("Please check for missing values!")
    return amount

if len(sys.argv)==2:
    filename=sys.argv[1]
else:
    filename='portfolio.csv'
cost= portfolio_cost('portfolio.csv')
print("Total cost:", cost)