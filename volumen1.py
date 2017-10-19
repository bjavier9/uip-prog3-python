class Volumen(object):

    def vol_figura():
        print("escriba la figura")
        figura = input("")
        if figura == "cilindro":
            radio = int(input("introduce el valor del radio"))
            altura = int(input("intruduce el valor de la latura "))
            print(((3.14)**2)*(radio)*(altura))
        elif figura == "cono":
            radio = int(input("introduce el valor del radio"))
            altura = int(input("intruduce el valor de la latura "))
            print((1/3)*(3.14)*(altura)*(radio)**2)
        elif figura == "esfera":
            radio = int(input("introduce el valor del radio"))
            print(4/3*3.14*radio**3)
        else:
            print("tas mal papa")

if __name__ == '__main__':
    luisa = Volumen
    luisa.vol_figura()
