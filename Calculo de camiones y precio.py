men1 = 1
camion = 765000
total1 = 0
total2 = 0
cil1 = 0
cil2 = 0
cil3 = 0
bol1 = False
bol2 = False
totalca1 = 0
totalca2 = 0
totalca3 = 0
kil1 = 0
kil2 = 0
kil3 = 0
while men1 == 1:
    try:
        nombrecli = input("Ingrese su nombre: ")
        letrasn = len(nombrecli)
    except ValueError:
        print("Por favor, ingrese solo letras.")
        continue
    if letrasn < 3:
         print("Por favor ingrese mas de 3 digitos.")
         continue
    print("_"*32)   
    try:
        teflcon = int(input("Ingrese su numero de contacto: "))
        numn = len(str(teflcon))
        men2 = 2
    except ValueError:
        print("Por favor solo ingrese numeros enteros.")
        continue
    if numn < 8:
        print("Ingrese entre 8 y 9 digitos, por favor ingrese los datos nuevamente.")
        continue
    elif numn > 9:
        print("Ingrese entre 8 y 9 digitos, por favor ingrese los datos nuevamente.")
        continue
    print("_"*32)
    while men2 == 2:
        try:
         print("1.- Compra entrega camion estandar.")
         print("2.- Compra entrega carga especifica.")
         print("3.- Continuar con el pedido o salir de la aplicacion.")
         elecc = int(input("Ingrese una opcion del 1 al 3: "))
        except ValueError:
            print("Debe de ingresar numeros.")
            continue
        if elecc == 1:
         try:
            print("El precio por camion es de $765.000")
            cantc = int(input("Ingrese la cantidad de camiones que desea."))
            total1 = camion*cantc+total1
            bol1 = True
         except ValueError:
             print("Por favor solo ingrese numeros enteros.")
         continue
        while elecc == 2:
            try:
                print("Esta distribuccion se realizara con una carga especifica.")
                print("1.- Cilindros de 5 kilos.")
                print("2.- Cilindros de 15 kilos.")
                print("3.- Cilindros de 45 kilos.")
                print("4.- Volver")
                cilinop = int(input("Por favor seleccione el tipo de cilindro (1 - 3): "))
            except ValueError:
                print("Por favor solo ingrese numeros enteros del 1 al 4.")
            if cilinop == 1:
                try: 
                  cant1 = int(input("Ingrese la cantidad de cilindros: "))
                  totalca1 = cant1+totalca1
                  kil1 = 5*totalca1
                  bol2 = True
                  continue
                except ValueError:
                    print("Por favor ingrese un numer entero.")
                    continue
            elif cilinop == 2:
                try:
                  cant2 = int(input("Ingrese la cantidad de cilindros: "))
                  totalca2 = cant2+totalca2
                  kil2 = 15*totalca2
                  bol2 = True
                  continue
                except ValueError:
                    print("Por favor ingrese un numero entero. ")
            elif cilinop == 3:
                try:
                    cant3 = int(input("Ingrese la cantidad de cilindros: "))
                    totalca3 = cant3+totalca3
                    kil3 = 45*totalca3
                    bol2 = True
                    continue
                except ValueError:
                    print("Por favor ingrese un numero entero. ")
            elif cilinop == 4:
                break
        if elecc == 3:
          total2 = kil1+kil2+kil3
          kilos1 = (total2+(cantc*450))
          camionestx = total2/450
          cantc1 = cantc+camionestx

          if camionestx == float:
            total4 = total2-450
            totaldinero = total4*1700+100000+765000
            print("_"*32)
            print("Cliente: ", nombrecli, "", sep= " | ")
            print("Telefono: ", teflcon, "", sep= " | ")
            print("Cantidad de kilos: ", kilos1, "", sep=" | " )
            print("Camiones: ", round(cantc1), "", sep= " | ")
            print("Valor total: ", round(total1), "", sep= " | ")
            print("_"*32)
            repetir = int(input("¿Desea realizar otro pedido?"))
          elif camionestx == int:
            print("_"*32)
            print("Cliente: ", nombrecli, "", sep= " | ")
            print("Telefono: ", teflcon, "", sep= " | ")
            print("Cantidad de kilos: ", kilos1, "", sep=" | " )
            print("Camiones: ", (cantc1), "", sep= " | ")
            print("Valor total: ", (total1), "", sep= " | ")
            print("_"*32)
            repetir = int(input("¿Desea realizar otro pedido?"))
            if repetir == 1:
             men1 = 1
             men2 = 1
             camion = 765000
             total1 = 0
             total2 = 0
             cant1 = 0
             cant2 = 0
             cant3 = 0
             cil1 = 0
             cil2 = 0
             cil3 = 0
             bol1 = False
             bol2 = False
             totalca1 = 0
             totalca2 = 0
             totalca3 = 0
             kil1 = 0
             kil2 = 0
             kil3 = 0
             continue
            else:
             men1 = 0
             men2 = 0
             print("Gracias.")
        else:
           print("Debe de ser un numero entre 1 y 3.")
           continue

            