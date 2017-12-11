if __name__ == '__main__':
   print("linea de comando que controla los recursos humanos")
   print("elija su opcion")
while True:
    print("\nMENU de registro \n 1- agregar colaborador \n 2- visualizar \n 3-eliminar \n 4-salir")
    op = input()
    if op == "1":
       archivo = open("recursoshumanos.csv" , "a")
       nombre = input("escribe tu nombre: ")
       cedula = input("escribe tu cedula: ")
       departamento = input("departamento: ")
       labor = input("labor: ")
       salario = input("escribe tu salario: ")

       archivo.write(nombre)
       archivo.write(", ")
       archivo.write(cedula)
       archivo.write(", ")
       archivo.write(departamento)
       archivo.write(", ")
       archivo.write(labor)
       archivo.write(", ")
       archivo.write(salario)
       archivo.write("\n ")
       archivo.close()
    elif op == "2":
       print("mostrar registro")
       archivo = open("recursoshumanos.csv","r")
       print (archivo.read())
       archivo.close()
    elif op == "3":
        print("eliminar archivo")
        archivo = open("recursoshumanos.csv")
        archivo.truncate()
        print("registro eliminados")
    elif op=="4":
        break
