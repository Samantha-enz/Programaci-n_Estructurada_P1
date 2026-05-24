'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones



print("\033c")
num = float(input("Ingresa numero de la tabla de multiplicar:  "))
con=1
tabla=num*con
print(num,"x ",con," = " , tabla)
con+=1

tabla=num*con
print(num,"x ",con," = " , tabla)
con+=1

tabla=num*con
print(num,"x ",con," = " , tabla)
con+=1

tabla=num*con
print(num,"x ",con," = " , tabla)
con+=1


tabla=num*con
print(num,"x ",con," = " , tabla)
con+=1

tabla=num*con
print(num,"x ",con," = " , tabla)
con+=1


tabla=num*con
print(num,"x ",con," = " , tabla)
con+=1

tabla=num*con
print(num,"x ",con," = " , tabla)
con+=1


tabla=num*con
print(num,"x ",con," = " , tabla)
con+=1


tabla=num*con
print(num,"x ",con," = " , tabla)
con+=1



  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control
  2.- Sin funciones



print("\033c")
num = int(input("Ingresas un número: \n"))

for i in range (1,11):
  res=num*i
  print(f"{num} X {i} = {res} ")


  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control solo while
  2.- Sin funciones



print("\033c")
num = int(input("Ingresas un número: \n"))
con =1 
while con <11:
  res=num*con
  print(f"{num} X {con} = {res} ")

  con+=1



  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- sin estructuras
    2.- con funciones

  

print("\033c")
def tabla(num_tab,n):
 mul=num_tab*n
 print(f"{num_tab} x {n} = {mul}")
 n+=1
 return n

#inicia aqui
num_tabla=int(input("Ingrese el numero de la tabla que desea multiplicar \n"))
num=1

n=tabla(num_tabla,num)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)


print("\033c")
def tabla(num_tab,n):
 mul=num_tab*n
 print(f"{num_tab} x {n} = {mul}")
 n+=1
 return n



#inicia aqui
num_tabla=int(input("Ingrese un número para multiplicar: \n"))
num=1

for n in range(10,0,-1):
  n=tabla(num_tabla,n)
'''
print("\033c")
def tabla(num,n):
  mul=num*n
  print(f"{num} X {n} = {mul}")
  n+1
  return n

#inicio
num=int(input("Ingresa un numero: "))
n=1

for i in range (1,11):
  i=tabla(num,i)


