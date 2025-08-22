#Hacer un algoritmo que se ingresa el tiempo registrado de dos autos que corrieron 
# una carrera. El tiempo se guardó como número decimal. Mostrar por pantalla cual 
# llegó primero
auto1=float(input(f"ingrese  tiempo auto 1 "))
auto2=float(input(f"ingrese  tiempo auto 2 " ))
if auto1<auto2:
    print(f"llego primero auto 1 con un timepo {auto1}")
else:
    print(f"llego primero auto 2 con un tiempo {auto2}")