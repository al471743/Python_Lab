#calcular raiz cuadrada entera de un número.


numero = int(input("introduce un número para buscar su raiz entera"))

x = 1

while (x**2 < numero):
        x+=1


print (f"{x-1}") 
