import csv

with open('\main.csv','r', encoding='utf-8') as csvfile:

    reader = csv.reader(csvfile)
    rows = [row for row in reader]
print (rows[4])