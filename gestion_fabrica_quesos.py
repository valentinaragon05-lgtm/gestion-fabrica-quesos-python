"""
SISTEMA DE GESTIÓN FÁBRICA DE QUESOS
"""

DESCUENTO = 0.90


def lista_productos():
    listapd = ["muzarella", "cremoso", "reggianito"]
    return listapd


def lista_precios():
    listapr = [7200, 6800, 12230]
    return listapr


def unirpp(listapd, listapr):  # union lista precios y productos
    lista = []
    for i in range(len(listapd)):
        lista.append([listapd[i], listapr[i]])
    return lista


def validar_producto(productos):
    print("Productos: ")
    for producto in productos:
        print(producto)
    prod = input("\n" "Ingrese producto (o fin): ")

    while prod not in productos and prod != "fin":
        print("ERROR. Producto incorrecto.")
        print("Productos:")
        for producto in productos:
            print(producto)
        prod = input("\n" "Ingrese producto (o fin): ")
    return prod


def kg():
    kilos = float(input("Kg solicitados: "))
    while kilos <= 0:
        print("ERROR. Los kg solicitados deben ser mayor que cero.")
        kilos = float(input("Kg solicitados: "))
    return kilos


def mod():
    modalidad = int(input("Modalidad (1=efectivo, 2=transferencia): "))
    while modalidad != 1 and modalidad != 2:
        print("ERROR. Modalidad incorrecta.")
        modalidad = int(input("Modalidad (1=efectivo, 2=transferencia): "))
    if modalidad == 1:
        modalidad = "efectivo"
    else:
        modalidad = "transferencia"
    return modalidad


def precio(lista, producto):
    preciolista = 0
    for nombre, valor in lista:
        if nombre == producto:
            preciolista = valor
    return preciolista


def unir_ventas(cliente, producto, kilos, modalidad, pfinal):
    lista_venta = [cliente, producto, kilos, modalidad, pfinal]
    return lista_venta


def registrar_venta(lprecios, preciotot, listado_ventas, cmuzza, compratot):
    productos = []
    for p in lprecios:
        productos.append(p[0])
    cliente = input("Ingrese el nombre del cliente (opcional): ")
    modalidad = mod()

    print("\n" "-----Ingrese los productos que desea registrar (fin para terminar)-----")
    producto = validar_producto(productos)
    while producto != "fin":
        kilos = kg()
        punitario = precio(lprecios, producto)  # precio por kg
        if modalidad == "efectivo":
            punitario = punitario * DESCUENTO
        pfinal = punitario * kilos
        preciotot = preciotot + pfinal
        compratot = compratot + 1
        if producto == "muzarella":
            cmuzza = cmuzza + 1
        venta = unir_ventas(cliente, producto, kilos, modalidad, pfinal)
        listado_ventas.append(venta)
        print("Se agrego el producto.")
        producto = validar_producto(productos)
    return lprecios, preciotot, listado_ventas, cmuzza, compratot


def mostrar_informe(preciotot, compratot, cmuzza):
    if preciotot >= 100000:
        print("Facturacion mayor a 100000. Se cumplio el estandar productivo.")
    else:
        print("Facturacion menor a 100000. No se cumplio el estandar productivo.")

    if compratot > 0:
        porcentaje = (cmuzza / compratot) * 100
        print("Porcentaje de muzarella en compras: ", cmuzza, "de", compratot, "(", round(porcentaje, 2), "%)")
    else:
        print("No se registraron ventas.")
    print("Facturación total:", round(preciotot, 2))


def ordenar(listado_ventas):
    listado_ventas.sort(key=lambda x: x[4], reverse=True)
    return listado_ventas


def mostrar_menu(lprecios, preciotot, listado_ventas, cmuzza, compratot):
    opcion = ""
    while opcion != "4":
        print("\n" "-----MENÚ-----")
        print("1) Registrar venta")
        print("2) Mostrar informe parcial del día")
        print("3) Listado de ventas de mayor a menor")
        print("4) Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            posicion = registrar_venta(lprecios, preciotot, listado_ventas, cmuzza, compratot)
            lprecios = posicion[0]
            preciotot = posicion[1]
            listado_ventas = posicion[2]
            cmuzza = posicion[3]
            compratot = posicion[4]
        elif opcion == "2":
            print("\n" "-----Informe parcial-----")
            mostrar_informe(preciotot, compratot, cmuzza)
        elif opcion == "3":
            if not listado_ventas:
                print("No hay ventas registradas.")
            else:
                ordenar(listado_ventas)
                print("\n" "-----Listado de ventas de mayor a menor-----")
                for venta in listado_ventas:
                    print("Cliente:", venta[0], "/ Producto:", venta[1], "/ Kg:", venta[2],
                          "/ Modalidad:", venta[3], "/ Precio: $", round(venta[4], 2))
        elif opcion != "4":
            print("ERROR. Opción inválida.")
    return lprecios, preciotot, listado_ventas, cmuzza, compratot


listapd = lista_productos()
listapr = lista_precios()
lprecios = unirpp(listapd, listapr)
listado_ventas = []
preciotot = 0
cmuzza = 0
compratot = 0
lprecios, preciotot, listado_ventas, cmuzza, compratot = mostrar_menu(
    lprecios, preciotot, listado_ventas, cmuzza, compratot)

print("\n" "-----Informe final-----")
mostrar_informe(preciotot, compratot, cmuzza)
if not listado_ventas:
    print("\n" "No se registraron ventas.")
else:
    ordenar(listado_ventas)
    print("\n" "La venta más grande fue: ")
    venta_max = listado_ventas[0]
    print(venta_max)

print("Fin del programa.")
