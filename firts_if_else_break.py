"""Ejemplo bucles"""
data = list()
while True:
    entrada = float(input("siguiente dato(-999 para terminar)?:"))
    if entrada != -999.0:
        data.append(entrada)
    else:
        break

for dato in data:
    print ("Dato: ", dato)