import csv
with open('people.csv','r') as file:
    data=csv.DictReader(file)
    for row in data:
        print(row['name'])