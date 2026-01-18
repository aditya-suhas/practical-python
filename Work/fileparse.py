# fileparse.py
import csv
def parse_csv(filename, has_headers=True, silence_errors=True,selected=None,types=None):
    if selected:
        if has_headers==False:
            raise RuntimeError("select argument requires column headers")
    if not selected:
        selected=("name","shares","price")
    with open(filename) as f:
        rows=csv.reader(f,)
        records=[]
        if has_headers==True:
            headers=next(rows)
            for rowno,row in enumerate(rows, start=1):
                if not row:
                    continue
                if types:
                    try:
                        row = [func(val) for func, val in zip(types, row)]
                    except ValueError as e:
                        if silence_errors==True:
                            continue
                        else:
                            print(f"Couldn't convert {row}")
                            print(f"Line {rowno}: Reason {e}")
                            continue
                takeout=[]
                for i in headers:
                    if i in selected:
                        takeout.append(i)
                record=dict(zip(takeout,row))
                records.append(record)
        else:
            for row in rows:
                if not row:
                    continue
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                appenditem=tuple(row)
                records.append(appenditem)
    return records
selected=("name","shares","price")
portfolio=(parse_csv('Work/Data/missing.csv', types=[str,int,float], has_headers=True, silence_errors=True))
print(portfolio)
# Exercise 3.3
