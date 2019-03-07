from lxml import etree
doc = etree.parse('aparcamientos.xml')

print("Elige el ejercicio que quieres comprobar")
print("1.- ejercicio 1")
print("2.- ejercicio 2")
print("3.- ejercicio 3")
print("4.- ejercicio 4")
print("5.- ejercicio 5")
print("0.- salir")
opcion=int(input("¿opcion?: "))
while opcion >=0 :
    if opcion == 1:
        nombres=doc.xpath("//nombre/text()")
        print("Estos son los aparcamientos que hay:")
        for i in nombres:
            print (i)
    elif opcion == 2:
        contar=doc.xpath("//nombre/text()")
        print("La cantidad de aparcamientos que hay son",len(contar))
    elif opcion == 3:
        calle=input("Escribe el nombre de la calle: ")
        buscar=doc.xpath("//direccion/text()")
        nombres=doc.xpath("//nombre/text()")
        for x, y in zip(buscar, nombres):
            if x == calle:
                print(y)
    elif opcion == 4:
        #abanico1=input("Escribe el limite inferior del abanico: ")
        #abanico2=input("Escribe el limite superior del abanico: ")
        precios=doc.xpath("//preciosplantas/precioplanta/text()")
        for i in precios:
            print (i)
            #if abanico1 >= i and abanico2 < i:
            #    print("yes")
    elif opcion == 5:
        telefono=input("Escribe el número de teléfono: ")
        telefonocomunidad=doc.xpath("//telefonoAdminComunidadUsuarios/text()")
        telefonoconcesionario=doc.xpath("//telefonoInfoConcesionario/text()")
        for x, y in zip(telefonocomunidad,telefonoconcesionario):
            if x==telefono:
                imagenes=doc.xpath('//aparcamiento[telefonoAdminComunidadUsuarios="%s"]/fotos/foto/text()' % telefono)
            if y==telefono:
                imagenes=doc.xpath('//aparcamiento[telefonoInfoConcesionario="%s"]/fotos/foto/text()' % telefono)
        for i in imagenes:
            print(i)
    elif opcion == 0:
        print("Saliendo del programa.")
    else:
        print("Opción no permitida")
    print("Elige el ejercicio que quieres comprobar")
    print("1.- ejercicio 1")
    print("2.- ejercicio 2")
    print("3.- ejercicio 3")
    print("4.- ejercicio 4")
    print("5.- ejercicio 5")
    print("0.- salir")
    opcion=int(input("¿opcion?: "))
