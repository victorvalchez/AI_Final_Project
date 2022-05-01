"""import pandas as pd

data = pd.read_csv('Data.csv', header=0, sep=';')

print(data.sort_values('GreenLight'))  # para ordenar de menor a mayor, en este caso por letras
count = 0
for column in data:
    if column[column[:3] == 'N']:
        if column[column[:0] == 'Low'] and column[column[:4] == 'High']:
            count += 1

print(count)
"""
import csv
new_list = []
with open('Data_no_header.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        new_list.append(row[0].split(';'))  # Esto crea una lista de lo que hay en cada fila (le pongo que esta separado
        # por ; para que cada vez que vea ; añada un nuevo elemento a la fila

cLowNToHigh = 0
cLowEToHigh = 0
cLowWToHigh = 0
for row in new_list:
    if row[3] == 'E':
        if row[0] == 'Low' and row[4] == 'High':
            cLowNToHigh += 1
        if row[1] == 'Low' and row[5] == 'High':
            cLowEToHigh += 1
        if row[2] == 'Low' and row[6] == 'High':
            cLowWToHigh += 1


print(cLowNToHigh)
print(cLowEToHigh)
print(cLowWToHigh)
