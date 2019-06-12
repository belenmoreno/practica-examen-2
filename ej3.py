def calcula_numero(numero):

    dic_irregulares = {
            "10":"diez",
            "11":"once",
            "12":"doce",
            "13":"trece",
            "14":"catorce",
            "15":"quince",
            "20":"veinte",
            "30":"treinta",
            "40":"cuarenta",
            "50":"cincuenta",
            "60":"sesenta",
            "70":"setenta",
            "80":"ochenta",
            "90":"noventa"
        }

    dic_unidades = {
        "0":"cero",
        "1":"uno",
        "2":"dos",
        "3":"tres",
        "4":"cuatro",
        "5":"cinco",
        "6":"seis",
        "7":"siete",
        "8":"ocho",
        "9":"nueve"
    }

    dic_decenas = {
        "1":"dieci",
        "2":"venti",
        "3":"treinta y ",
        "4":"cuarenta y ",
        "5":"ciencuenta y ",
        "6":"sesenta y ",
        "7":"setenta y ",
        "8":"ochenta y ",
        "9":"noventa y "
    }
    
    dic_centenas = {
        "1":"ciento ",
        "2":"doscientos",
        "3":"trescientos",
        "4":"cuatrocientos",
        "5":"quinientos",
        "6":"seiscientos",
        "7":"setecientos",
        "8":"ochocientos",
        "9":"novecientos"
    }

    numero_string = str(numero)
    
    #print(len(numero_string))
    #len calcula la longitud 

    if len(numero_string) == 1:
        print(dic_unidades[numero_string])

    elif len(numero_string) == 2:
        if numero_string in dic_irregulares:
            print(dic_irregulares[numero_string])

        else:
            print(dic_decenas[numero_string[0]] + dic_unidades[numero_string[1]])
    else:
        if numero == 100:
            print("cien")
        else:
            aux = int(numero_string[1] + numero_string[2])
            print(dic_centenas[numero_string[0]], end='')
            calcula_numero(aux)





def main():
    numero = int(input("introduce un numero entero entre 0 y 999: "))
    calcula_numero(numero)



if __name__ == "__main__":
    main()
