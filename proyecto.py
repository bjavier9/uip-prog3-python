import pickle

c=0

def agregar(dic):
    x = input("Pregunta: ")
    y = input("Respuesta: ")
    dic[x] = y

def cargar_datos():
    try:
        with open("parcial.dat", "a") as f:
            return pickle.load(f)
    except (OSError, IOError) as e:
        return dict()

def guardar_datos(dic):
    with open("parcial.dat", "a") as f:
        pickle.dump(dic, f)


def main():
    dic = cargar_datos()
    menu ='''
    1. Parcial
    2. Añadir preguntas.
    3. Guardar y salir.
    '''

    while True:
        print(menu)
        decision = input("¿Que quieres hacer?: ")
        if decision == "1":
            for x in range(0,1,3):
                global c
                for es, ing in dic.items():
                    resp = input('Escribe en ingles "{}": '.format(es))
                    if resp == ing:
                        print ("Correcto.")
                    else:
                        print ('Incorrecto, es "{}".'.format(ing))
                        c = c + 1

            print ("errastes: ",c)
            main()
        elif decision == "2":
            agregar(dic)
        elif decision == "3":
            guardar_datos(dic)
            break
        else:
            print('Opción inválida, intentelo de nuevo.')

if __name__ == '__main__':
    main()