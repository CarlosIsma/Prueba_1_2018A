#libreria para funciones matematicas
from math import pi
def cubo():
    print("****CUBO***")
    lado = int(input("ingrese un numero por favor"))
    print("El volumen del cubo es: ", lado * lado * lado)

def esfera():
    print("****ESFERA***")
    lado1=float(input("ingrese el radio de la esfera  "))

    lado1=((4/3)*(pi))*(lado1)**3
    print("el volumen de una esfera es :",lado1)


def menu():

    print("Selecciona la figura a calcular el volumen")
    print("\t1 - Cubo")
    print("\t2 - Piramide de base triangular")
    print("\t3 - Piramide de base cuadrangular")
    print("\t4 - Esfera")
    print("\t0 - salir")
while True:

    menu()

    opcionMenu = input("Ingresa una opcion >> ")

    if opcionMenu == "1":

       cubo()
    elif opcionMenu == "2":
        print ("**PIRAMIDE DE BASE TRIANGULAR**")

        input("Has pulsado la opción 2...\npulsa una tecla para continuar")
    elif opcionMenu == "3":
        print ("**PIRAMIDE DE BASE CUADRANGULAR**")
        input("Has pulsado la opción 3...\npulsa una tecla para continuar")
    elif opcionMenu == "4":
        esfera()
    elif opcionMenu == "0":
        break
    else:
        print ("")
        input("Opcion erronea...\npulsa una tecla para continuar")

