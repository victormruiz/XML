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
        calle=input("Escribe el nombre y número de la calle: ")
        buscar=doc.xpath("//direccion/text()")
        nombres=doc.xpath("//nombre/text()")
        bandera=False
        for x, y in zip(buscar, nombres):
            if x == calle:
                print(y)
                bandera=True
        if bandera==False:
            print("No hay aparcamientos disponibles en esa calle y ese número")
    elif opcion == 4:
        import re
        lista=[]
        nombres=doc.xpath("//nombre/text()")
        for i in nombres:
            limite=input("Hasta cuanto estás dispuesto a gastarte?: ")
            precios=(doc.xpath('//aparcamiento[nombre="%s"]/preciosPlantas/precioPlanta/text()' % i))
            for x in precios:
                x=re.sub("\D", "", x)
                x=x[ 1:len(x) - 2]
                if limite <= x:
                    print(i)




    elif opcion == 5:
        bandera=False
        telefono=input("Escribe el número de teléfono: ")
        telefonocomunidad=doc.xpath("//telefonoAdminComunidadUsuarios/text()")
        telefonoconcesionario=doc.xpath("//telefonoInfoConcesionario/text()")
        for x, y in zip(telefonocomunidad,telefonoconcesionario):
            if x==telefono:
                imagenes=doc.xpath('//aparcamiento[telefonoAdminComunidadUsuarios="%s"]/fotos/foto/text()' % telefono)
            if y==telefono:
                imagenes=doc.xpath('//aparcamiento[telefonoInfoConcesionario="%s"]/fotos/foto/text()' % telefono)
        if len(imagenes != 0):
            for i in imagenes:
                print(i)
        else:
            print("No hay imágenes asociadas a ese telefono")




    elif opcion == 0:
        print("Saliendo del programa.")
    else:
        print("")
        print("Opción no permitida")
    print("Elige el ejercicio que quieres comprobar")
    print("1.- ejercicio 1")
    print("2.- ejercicio 2")
    print("3.- ejercicio 3")
    print("4.- ejercicio 4")
    print("5.- ejercicio 5")
    print("0.- salir")
    opcion=int(input("¿opcion?: "))
