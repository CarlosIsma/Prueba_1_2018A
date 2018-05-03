print("**Prueba Primer Bimestre**")
print("**Programacion Avanzada**")


def creartxt():
    archi = open('1.txt', 'w')
    archi.close()

def leertxt():
    archi=open('1.txt','r')
    linea=archi.readline()
    while linea!="":
        print (linea)
        linea=archi.readline()
    archi.close()


leertxt()

def grabartxt():
    archi=open('1.txt','a')
    archi.write('\nCarlos Ismael Lucero Chamaza\n')
    archi.write('\nEl resultado es: ')


grabartxt()