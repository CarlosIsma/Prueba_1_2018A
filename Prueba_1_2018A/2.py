print("**Prueba Primer Bimestre**")
print("**Programacion Avanzada**")


def creartxt():
    archi = open('2.txt', 'w')
    archi.close()

def grabartxt():
    archi=open('2.txt','a')
    archi.write("Cadena Normal: Carlos Lucero\n")
    archi.write("\nCadena Invertida: ")
    def invert():
        a="  Carlos Lucero"
        n=(len(a)-1)
        while n!=1:
            i=str(a[n])
            archi.write(str(i))
            n=n-1

    invert()

creartxt()

grabartxt()



