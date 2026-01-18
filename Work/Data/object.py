import csv
types = [str, float, str, str, float, float, float, float, int]
with open('Data/dowstocks.csv', 'rt')as f:
    rows=csv.reader(f)
    headers=next(rows)
    row=next(rows)
    converted=[func(val) for func,val in zip(types,row)]
    record=dict(zip(headers,converted))
print(record)
print(record['name'])