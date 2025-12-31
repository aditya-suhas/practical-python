# report.py
import csv
import sys
def make_report(portfolio, prices):
    report = []
    owned_stocks=[]
    for i in portfolio:
        owned_stocks.append(i['name'])
    owned_stocks=set(owned_stocks)
    for item in portfolio:
        if item['name'] in owned_stocks:
            name = item['name']
            shares = item['shares']
            purchase_price = item['price']
            current_price = float(prices[name])
            change = current_price - purchase_price
            report.append((name, shares, "$"+str(current_price), round(change, 2)))
            owned_stocks.remove(item['name'])
        else:
            pass
        # We append a single tuple containing the data points
    return report
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
def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio=[]
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows):
            record=dict(zip(headers,row))
            nshares = int(record['shares'])
            price = float(record['price'])
            name=record['name']
            portfolio.append({'name':name,'shares':nshares,'price':price})
    return portfolio
if len(sys.argv)==2:
    filename=sys.argv[1]
else:
    filename='Data/portfolio.csv'
portfolio=read_portfolio(filename)
total = 0.0
stocks_owned=[]
for i in portfolio:
    total+=i['shares']*i['price']
    stocks_owned.append(i['name'])
stocks_owned=set(stocks_owned)
valstockowned=0
quantity={}
for i in portfolio:
    if i['name'] in stocks_owned:
        quantity[i['name']]=i['shares']
    else:
        pass
if len(sys.argv)==2:
    filename=sys.argv[1]
else:
    filename='Data/prices.csv'
prices=read_prices(filename)
current_value=0
for i in stocks_owned:
    valstockowned+=(float(prices[i])*int(quantity[i]))
gain=total-valstockowned
headers = ('Name', 'Shares', 'Price', 'Change')
portfolio = read_portfolio('./Data/portfoliodate.csv')
prices = read_prices('./Data/prices.csv')
report = make_report(portfolio, prices)
print("%10s %10s %10s %10s" % headers)
underline=("..........")
print(f"{underline} {underline} {underline} {underline}")
for r in report:
    print('%10s %10d %10.8s %10.2f' % r)
# Exercise 2.4
