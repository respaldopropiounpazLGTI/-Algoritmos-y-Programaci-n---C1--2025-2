"""Hacer un algoritmo donde se Ingresan los siguientes datos de 5 alumnos: 
 ●   nota (float), 
 ●   Edad = (entero) 
 Mostrar por pantalla la mejor nota y qué edad tenía."""
 
mejor_nota=0
edad_mejor_nota=0
for i in range(5):
    nota=float(input(f"ingrese nota {i+1} :"))
    edad=int(input(f"ingrese edad {i+1} : "))
    if nota>mejor_nota:
        mejor_nota=nota
        edad_mejor_nota=edad
        
        
        
print(f"la mejor nota es {mejor_nota} y la edad ed {edad_mejor_nota}")        
        
        
        