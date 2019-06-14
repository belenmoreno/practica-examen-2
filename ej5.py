def facturacion(facturas, NIF, mes):
    
   
    facturas_filtradas = []
    for factura in facturas:
        if factura["nif"] == NIF and factura["mes"] == mes:
            facturas_filtradas.append(factura)

    for aux in facturas_filtradas:
        aux["total"] = (aux["cantidad"] * aux["iva"] / 100) + aux["cantidad"]
    return facturas_filtradas

    
    
    #creamos directamente la lista con los diccionarios dentreo
    

    

    

def main(): 

    pregunta = input("introduce tu nif")
    pregunta2 = input("introduce un mes")

    facturas = [{
        "nif":"12345",
        "mes":"noviembre",
        "cantidad":2000,
        "iva":5
    },
    {
        "nif":"67890",
        "mes":"diciembre",
        "cantidad":3000,
        "iva":6
    },
    {
        "nif":"101112",
        "mes":"enero",
        "cantidad":5000,
        "iva":7
    },
    {
         "nif":"202122",
         "mes":"febrero",
         "cantidad":6000,
         "iva":8
    }]


    print(facturacion(facturas, pregunta, pregunta2))

if __name__ == "__main__":
    main()
