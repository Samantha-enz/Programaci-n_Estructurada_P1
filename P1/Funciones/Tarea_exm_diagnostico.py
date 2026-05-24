def borrarPantalla():
   print("\033c")

def sueldo_trabajador():
    borrarPantalla ()
    t_trabajadores = 0
    t_sueldo = 0
    respuesta = "si"

    while respuesta == "si":
        nombre = input("Ingresa tú nombre: \n")
        h_trabajadas = int(input("Ingresa el número de horas trabajadas: \n"))
        s_hora = float(input("Ingresar sueldo por hora: \n"))
        sueldo = h_trabajadas*s_hora        

        match h_trabajadas:

            case h_trabajadas if h_trabajadas == 10:
                s_aumento = sueldo *20
            case h_trabajadas if h_trabajadas == 15:
                s_aumento = sueldo * 30
            case h_trabajadas if h_trabajadas == 20:
                s_aumento = sueldo *15
            case h_trabajadas if h_trabajadas > 25:   
                s_aumento = sueldo*.08
            case _:
                s_aumento = sueldo*0 

        t_neto = (h_trabajadas*s_hora)+s_aumento
        t_trabajadores +=1
        t_sueldo += t_neto
        
        print (f"Tú salario es: {sueldo} \nTienes un bono de aumento de: {s_aumento} ")

        respuesta=input("¿Deseas continuar?\n").lower().strip()    

    return t_sueldo, t_trabajadores

t_sueldo,t_trabajadores = sueldo_trabajador()

print(f"Trabajadores ingresados: {t_trabajadores}\nSueldo total neto de los trabajadores: {t_sueldo}")