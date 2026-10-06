#Escribe un programa bucle del 1 al 110 en 10 lineas (11 números por línea)
# múltiplo de 5 "losa" múltiplo de 7 "Wosa" múltiplo de 3 y 5 "CosaLosa" para
# múltiplos de 3 y 7 "CosaWosa"

cadena_numeros =""
x = 0
numero = 0 
for i in range(1, 111):
    if(i % 3 != 0 and i % 5 != 0 and i % 7 != 0):
        print(i, end=" ")

    else:
        if (i <=11):
            if(i % 3 == 0):
                print("Cosa", end=" ")
            if(i % 7 == 0):
                print("Wosa", end=" ")
            if(i % 5 == 0):
                print("Losa", end=" ")
        else:
            if(i % 5 == 0 and i % 3 == 0):
                print("CosaLosa", end=" ")
            if(i % 7 == 0 and i % 3 == 0 ):
                print("CosaWosa", end=" ")
            if(i % 3 == 0 and not(i% 5 !=0 and i% 7 !=0)):
                print("Cosa", end=" ")
    if(i % 11 ==0):
        print("\t")
                    
