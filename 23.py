palabra = "secreto"
i = 1
secret= input("Ingrese la palabra secreta: ")
while 1==1:

   if secret.lower() != palabra:
    print("Incorrecto")
    secretx= input("Ingrese la palabra secreta: ")
   else:
    print("correcto")
    break

   if secretx.lower() != palabra:
    print("Incorrecto")
    secretxx= input("Ingrese la palabra secreta: ")
   else:
    print("correcto")
    break

   if secretxx.lower() != palabra:
    print("Incorrecto")
    secretxxx= input("Ingrese la palabra secreta: ")
   else:
    print("correcto")
    break

    if secretxx.lower() != palabra:
        print("perdiste")
    else:
        print("ganastes")