from iniciosesion import*
from entrar import*

def mostrar_menu():
    print('Menú:')
    print('1. Crear nuevo usuario')
    print('2. Iniciar sesión')
    print('3. Salir')

while True:
    mostrar_menu()

    opcion = input('Ingrese el número de la opción que desea: ')

    if opcion == '1':
        agregar_usuario()
    elif opcion == '2':
        validar_usuario()
    elif opcion == '3':
        break
    else:
        print('Opción inválida. Intente de nuevo.')
