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
with open('Data_no_header.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        new_list.append(row[0].split(';'))  # Esto crea una lista de lo que hay en cada fila (le pongo que esta separado
        # por ; para que cada vez que vea ; añada un nuevo elemento a la fila

countE = 0
cLowNToHigh = 0
cLowEToHigh = 0
cLowWToHigh = 0

cLowNToLow = 0
cLowEToLow = 0
cLowWToLow = 0

cHighNToHigh = 0
cHighEToHigh = 0
cHighWToHigh = 0

cHighEToLow = 0

for row in new_list:
    if row[3] == 'E':
        if row[0] == 'Low' and row[4] == 'High':  # low norht to high north
            cLowNToHigh += 1
        if row[1] == 'Low' and row[5] == 'High':  # es 0 ya que se abre el semaforo entonces no suele subir
            cLowEToHigh += 1
        if row[2] == 'Low' and row[6] == 'High':
            cLowWToHigh += 1

        if row[0] == 'Low' and row[4] == 'Low':
            cLowNToLow += 1
        if row[1] == 'Low' and row[5] == 'Low':
            cLowEToLow += 1
        if row[2] == 'Low' and row[6] == 'Low':
            cLowWToLow += 1

        if row[0] == 'High' and row[4] == 'High':
            cHighNToHigh += 1
        if row[1] == 'High' and row[5] == 'High':
            cHighEToHigh += 1
        if row[2] == 'High' and row[6] == 'High':
            cHighWToHigh += 1

        if row[1] == 'High' and row[5] == 'Low':
            cHighEToLow += 1

        countE += 1

print("Low to high N,E,W")
print(cLowNToHigh)
print(cLowEToHigh)
print(cLowWToHigh)
print()
print("Low to low N,E,W")
print(cLowNToLow)
print(cLowEToLow)
print(cLowWToLow)
print()
print("High to high N,E,W")
print(cHighNToHigh)
print(cHighEToHigh)
print(cHighWToHigh)
print()
print("High to low E")
print(cHighEToLow)
print()
print("Check total for each")
print("Total for north: ", cLowNToHigh + cLowNToLow + cHighNToHigh)
print("Total for east: ", cLowEToHigh + cLowEToLow + cHighEToHigh + cHighEToLow)
print("Total for west: ", cLowWToHigh + cLowWToLow + cHighWToHigh)
