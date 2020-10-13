import csv
import pandas as pd

file = pd.read_csv(r'74181.isc')
file.to_csv (r'74181.csv', index=None)

with open('74181.csv') as csv_file:
    reader = csv.reader(csv_file,delimiter=' ')
    for row in reader:
        print(row)
