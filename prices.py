import csv
import sys
def read_prices(filename):
    file=None
    prices={}
    with open(filename, 'rt')as f:
        file=csv.reader(f)
        for row in file:
            if len(row) < 2:
                pass
            else:
                prices[row[0]]=row[1]
        return prices
if len(sys.argv)==2:
    filename=sys.argv[1]
else:
    filename='Data/prices.csv'
output=read_prices(filename)
print(output)
print(output['IBM'])