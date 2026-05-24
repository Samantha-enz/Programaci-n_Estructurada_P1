
'''
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

def nombredeMifuncion(parametros):
#bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)
   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor
'''

#Funcion o procedimiento que borre pantalla(las funciones si o si llevan return )
def borrarPantalla():
   print("\033c")

#1.- Funcion que no recibe parametros y no regresa valor (Se comporta como procedimiento)
def funcion1():
   borrarPantalla()
   nombre=input("Escribe el nombre: ").strip().upper()
   apellidos=input("Escribir los apellidos: ").strip().upper()
   print(f"El nombre completo del alumno es:  {nombre} {apellidos}")

funcion1()


#Strip, quita los espacios antes del primer caracter y despues del ultimo
#upper: quiero que se guarde en mayuscula
#Las funciones estan antes de las invocaciones y  no aparecen en la terminal si no se manda llamar


 #3.- Funcion que recibe parametros y no regresa valor 
def funcion3(nom,ape):
  
   nombre=nom
   apellidos=ape
   print(f"El nombre completo del alumno es:  {nombre} {apellidos}")


#los parametros se pueden abreviar por ejemplo nombre puede abreviarse como nom, pero se tiene que  
#especificar por ejemplo en un renglon aparte nombre=nom

 #2.- Funcion que no recibe parametros y regresa valor
def funcion2():
   
   nombre=input("Escribe el nombre: ").strip().upper()
   apellido=input("Escribir los apellidos: ").strip().upper()
   return nombre,apellido




#Todo lo que regrese el sistema se guarda en una variable 

 #4.- Funcion que recibe parametros y regresa valor
def funcion4(nom,ape):
   
   return nom,ape




#Invocar las funciones
funcion1()

nombre=input("Escribe el nombre: ").strip().upper()
apellidos=input("Escribir los apellido: ").strip().upper()
funcion3(nombre,apellidos)

nombre,apellido=funcion2()
print(f"El nombre del alumno es: {nombre} {apellido}")

nombre=input("Nombre: ").strip().upper()
apellidos=input("Apellidos: ").strip().upper()
nom,ape=funcion4(nombre,apellidos)
print(f"El nombre completo del alumno es:  {nom} {ape}")


