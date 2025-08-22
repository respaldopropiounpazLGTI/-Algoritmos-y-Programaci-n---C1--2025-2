# Hacer un programa en el que se ingresa precio y calcula el precio final con el iva 
# (21%). Mostrar el resultado por pantalla
precio=float(input("ingrese precio "))
iva=precio*0.21
precio_final=precio+iva
print(f" precio comun {precio} +iva {iva} total {precio_final}")