def cotizacion(ruta_fichero):
    try:
        f = open(ruta_fichero, 'r')
    except FileNotFoundError:
        print("Ruta del fichero incorrecta")
        return

    linea_uno = f.readline()
    campos = linea_uno.split(', ')
    diccionario = {
        campos[0]:[],
        campos[1]:[],
        campos[2]:[],
        campos[3]:[],
        campos[4]:[],
        campos[5]:[]
    }

    for linea in f:
        linea = linea.split(', ')
        j = 0
        for i in linea:
            i = i.replace(',', '.').replace('\n', '')
            #print(i)
            diccionario[campos[j]].append(i)
            j += 1

    return diccionario
    f.close()

def main(): 
    pregunta = input("introduce la ruta del fichero ")
    respuesta = cotizacion(pregunta)
    print(respuesta)

if __name__ == "__main__":
    main()
