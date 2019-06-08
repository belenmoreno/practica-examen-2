def main():

    numero = int(input("introduce un numero entero: "))
    aux = 0
    numero_estrellas = 1
    i = 0
    while (aux < numero):#numero de filas que pintamos
            while (i < numero_estrellas):#numero estrellas que pintamos
                print("*", end = '')
            print("\n")
            i = 0
            numero_estrellas += 2
            aux += 1
        
    


if __name__ == "__main__":
    main()
