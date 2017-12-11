pi = 3.14159265359
class Esfera(object):
    def __init__(x, r):
        x.radio = r
        x.volumen = 0

    def obtvol(x):
        r = x.radio
        x.volumen = (4 / 3) * pi * (r ** 3)
        return x.volumen


class Cilindro(object):
    def __init__(x, r, h):
        x.radio = r
        x.altura = h
        x.volumen = 0


    def obtvol(x):
        r = x.radio
        h = x.altura
        x.volumen = pi * (r ** 2) * h
        return x.volumen


class Cono(object):
    def __init__(x, r, h):
        x.radio = r
        x.altura = h
        x.volumen = 0

    def obtvol(x):
        r = x.radio
        h = x.altura
        x.volumen = (1 / 3) * pi * (r ** 2) * h
        return x.volumen
if __name__ == '__main__':
 while True :
        print("Ingrese la figura geometrica que desee encontrar 1\nCilindro, \n 2-Cono \n 3- Esfera \n 4-salir ")
        op = input()

        if op == "1":
            print("     Esfera")
            r = int(input("Ingrese el radio de la esfera: "))
            s = Esfera(r)
            print("El volumen de la esfera es: ", s.obtvol())
        elif op == "2":
            print("     Cono")
            r = int(input("Ingrese el radio de el cono: "))
            h = int(input("Ingrese la altura de el cono: "))
            d = Cono(r, h)
            print("El volumen de el cono es: ", d.obtvol())
        elif op == "3":
            print("     Cilindro")
            r = int(input("Ingrese el radio de el cilindro: "))
            h = int(input("Ingrese la altura de el cilindro: "))
            c = Cilindro(r, h)
            print("El volumen de el cilindro es: ", c.obtvol())
        elif op == "4":
            break

