def main():

    numero_filas = int(input("introduce un numero entero: "))
    contador_filas_actuales = 0
    numero_estrellas = 1
    i = 0
    j = 0

    while contador_filas_actuales < numero_filas:#numero de filas que pintamos

        espacios = numero_filas - (contador_filas_actuales + 1)
        while j < espacios:#numero espacios que pintamos
            print(" ", end='')
            j += 1

        while i < numero_estrellas:#numero estrellas que pintamos
            print("*", end='')
            i += 1

        print("")
        numero_estrellas += 2
        i = 0
        j = 0
        contador_filas_actuales += 1


if __name__ == "__main__":
    main()
