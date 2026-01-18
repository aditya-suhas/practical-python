import csv
types=[str,int,float]
def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio=[]
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = types[1](row[1])
            price = types[2](row[2])
            holding=[row[0],nshares,price]
            portfolio.append({'name':row[0],'shares':nshares,'price':price})
    return portfolio
portfolio=read_portfolio('Data/portfolio.csv')
cost=sum([s['shares']*s['price']for s in portfolio])
print(cost)