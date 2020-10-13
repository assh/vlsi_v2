import csv
import pandas as pd

file = pd.read_csv(r'74181.isc')
file.to_csv (r'kl_input.csv', index=None)

with open('kl_input.csv') as csv_file:
    files = open('inputs.txt','a')
    reader = csv.reader(csv_file,delimiter=' ')
    for row in reader:
        print(row)
        if (row[2] == 'inpt'):
            strr = ""
            for i in range(len(row)):
                strr = strr+row[i]+' '
            strr = strr+'\n'
            files.write(strr)

    files.close()

