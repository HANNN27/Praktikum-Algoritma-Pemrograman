# latihan konversi stuan temperature

# program konversi celcius ke satuan lain

print('\nPROGRAM KONVERSI TEMPERATURE\n')

celcius = float(input('Masukan celcius : '))
print(f'Suhu Adalah {celcius} Celcius')

# reamur
reamur = (4/5) * celcius
print(f'Suhu dalam reamur : {reamur}')

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print(f'Suhu dalam fahrenheit : {fahrenheit}')

#kelvin
kelvin = celcius + 273
print(f'Suhu dalam kelvin : {kelvin}')