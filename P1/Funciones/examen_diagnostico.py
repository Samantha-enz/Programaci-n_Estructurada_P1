#Programa que pide al empleado ingresar su nombre, horas trabajadaas y sueldo
#por día y segun los dias da un aumento.
#Función para borrar pantalla
def borrarPantalla():
    print("\033c")

#Funcion para calcular sueldo base
def sueldoBase(h,s):
    sb= h*s

    return sb
#Entrada
borrarPantalla()
opc="S"
trabajadores=0
acum_suel_neto=0
while opc== "S":
    nombre=input("Nombre: ")
    horas_trab=int(input("Horas trabajadas: "))
    sueldo=float(input("Sueldo por Horas trabajadas: "))

    sueldo_base=sueldoBase(horas_trab,sueldo)
#Proceso
    aumento=0
    if horas_trab==10:
        aumento=0.20
    elif horas_trab==15:
        aumento=0.30
    elif horas_trab==20:
        aumento=0.15  
    elif horas_trab>25:
        aumento=0.08
    else:
        aumento=0

    
    aumento_pagar=aumento*sueldo_base
    suel_neto=sueldo_base+aumento_pagar
     
    trabajadores+=1  
    acum_suel_neto+=suel_neto
#Salida   
    print(f"El aumento es: {aumento_pagar}\nY el sueldo neto cobrado es: {suel_neto}")
    opc=input("¿Deseas realizar otra vez (S/N)?: ").upper().strip()
  
print(f"El total de trabajadores es: {trabajadores}\nY el sueldo neto acumulado es: {acum_suel_neto}")