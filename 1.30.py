#A un trabajador le pagan según sus horas trabajadas y la tarifa está a un valor por 
# hora. Si la cantidad de horas trabajadas es mayor a 40 horas, la tarifa por hora se 
# incrementa en un 50% por considerar que son horas extras. Desarrollar un programa 
# que calcule el salario del trabajador dadas las horas trabajadas y la tarifa 
horas_trabajadas=int(input("ingrese horas trabajadas "))
precio_horas=10
horas_extras=5
sueldo=horas_trabajadas*precio_horas
extras=precio_horas*horas_extras
totla=sueldo+extras

print(f"como trabajo {horas_trabajadas} cobra {sueldo}")
if horas_trabajadas>40:
    print(f"al suekdo comun se le agrega las extras por horas {extras} ")
    print(f" en total cobra {totla}")
    
    
    