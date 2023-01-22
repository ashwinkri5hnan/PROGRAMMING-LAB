import csv
with open('haha.csv','r') as f:
    r=csv.reader(f)
for row in r:
    print(row)