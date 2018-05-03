#libreria para funciones matematicas
from math import pi
def cubo():
    print("****CUBO***")
    lado = int(input("Ingrese el lado del cubo por favor"))
    print("El volumen del cubo es: ", lado * lado * lado," unidades cúbicas")

def esfera():
    print("****ESFERA***")
    radio=float(input("ingrese el radio de la esfera  "))

    volumen=((4/3)*(pi))*(radio)**3
    print("el volumen de una esfera es :",volumen, " unidades cúbicas")


def VolPiramideTriang():
    BaseTriang=float(input("Ingrese el lado base del triángulo base de la pirámide: "))
    AlturaTriang=float(input("Ingrese la altura del triángulo base: "))
    AlturaPiram=float(input("ingrese la altura de la pirámide: "))
    volumen=(1/3)*((1/2)*BaseTriang*AlturaTriang)*AlturaPiram
    print("El volumen de la pirámide con base triangular es: ",volumen," unidades cúbicas")

def VolPiramideCuadran():
    LadoBase=float(input("Ingrese el lado de la base: "))
    AlturaPiram=float(input("Ingrese la altura de la pirámide"))
    Volumen=(1/3)*(LadoBase**2)*AlturaPiram
    print("El volumen de la pirámide con base cuadrangular es: ",Volumen," unidades cúbicas")




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
       print("")
       input("Pulsa una tecla para continuar")

    elif opcionMenu == "2":
        print ("**PIRÁMIDE DE BASE TRIANGULAR**")
        VolPiramideTriang()
        print("")
        input("Pulsa una tecla para continuar")


    elif opcionMenu == "3":
        print ("**PIRAMIDE DE BASE CUADRANGULAR**")
        VolPiramideCuadran()

        print("")
        input("Pulsa una tecla para continuar")


    elif opcionMenu == "4":
        esfera()
        input("Pulsa una tecla para continuar")

    elif opcionMenu == "0":
        break

    else:
        print ("")
        input("Opcion erronea...\nPulsa una tecla para continuar")

