prices = {} # Initial empty dict

with open('prices.csv', 'rt') as f:
    for line in f:
        if "," not in line:
            pass
        else:
            row = line.split(',')
            prices[row[0]] = float(row[1])
    for k,v in prices.items():
        print(f"{k}: {v}")