def calcular_gastos_ingresos(contador, longitud, ingresos, gastos, beneficio, año_inicial, año_final):

    while contador < longitud:
        ingresos[contador] = float(input("Introduce tus ingresos del año " + str(año_inicial + contador) + "  "))
        gastos[contador] = float(input("introduce tus gastos del año " + str(año_inicial + contador) + " "))        
        beneficio[contador] = ingresos[contador] - gastos[contador]
        contador +=1

    #año_final = 23 como año_final no es un array/lista, no se modifica el valor de la variable original
    #print(año_final) imprime 23

def settear_contador():
    return 0



def main():

    año_inicial = int(input("introduce un año inicial: "))
    año_final = int(input("introduzca un año final: "))
    longitud = (año_final - año_inicial) + 1
    ingresos = [None] * longitud
    gastos = [None] * longitud
    contador = 0
    beneficio = [0] * longitud
    beneficio_positivo = [False] * longitud

    calcular_gastos_ingresos(0, longitud, ingresos, gastos, beneficio, año_inicial, año_final)
    #while contador < longitud:
    #    ingresos[contador] = float(input("Introduce tus ingresos del año " + str(año_inicial + contador) + "  "))
    #    gastos[contador] = float(input("introduce tus gastos del año " + str(año_inicial + contador) + " "))        
    #    beneficio[contador] = ingresos[contador] - gastos[contador]
    #    contador +=1

    #print("año final original " + str(año_final)) imprime el valor original dado que año_final no es un array/lista
    print(beneficio)
    contador = settear_contador()

    for aux in beneficio:
        if aux >= 0:
            beneficio_positivo[contador] = True
        contador += 1

    print(beneficio_positivo)

    contador = settear_contador()
    while contador < longitud:
        if beneficio_positivo[contador]:
            print("El año " + str(año_inicial + contador) + " tiene un beneficio positivo")
        contador += 1
    
    contador = 0
    while contador < longitud:
        if not beneficio_positivo[contador]:
            print("El año " + str(año_inicial + contador) + " tiene un beneficio negativo")
        contador += 1



if __name__ == "__main__":
    main()
