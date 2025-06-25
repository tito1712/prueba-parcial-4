def mostrar_menu():
    print('Menu Principal')
    print('1.Comprar entrada')
    print('2.Consultar compra')
    print('3.Cancelar compra')
    print('4.salir')
Compradores =[]
while  True:
    mostrar_menu()
    try:
        op = int(input('Elegir una opcion: '))
    except ValueError:
        print('Opcion invalida')
    if op ==1:
        while True:
            try:
                nombre_comprador=input('Inggrese El nombre de comprador')
                if nombre_comprador.isdigit():
                    print('Nombre no permitido intente de nuevo')
                elif nombre_comprador == "":
                        print('Nombre no permitido intente de nuevo')
                else:
                    break
            except:
                print('Nombre no permitido intente de nuevo')
