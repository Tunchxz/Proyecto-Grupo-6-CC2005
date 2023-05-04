import pandas as pd
from agregar import*

def validar_usuario():
    # Solicitar al usuario que ingrese su nombre de usuario y contraseña
    usuario = input('Nombre de usuario: ')
    contrasena = input('Contraseña: ')

    # Verificar si el usuario y la contraseña son válidos
    df_usuarios = pd.read_csv('usuarios.csv')
    if (df_usuarios['username'] == usuario).any() and (df_usuarios['password'] == contrasena).any():
        print('¡Inicio de sesión exitoso!')

        while True:
            print('¿Qué deseas realizar?')
            print('1. Ofrecer artículos')
            print('2. Ver mis publicaciones')
            print('3. Ver artículos disponibles')
            print('4. Bandeja de mensajes')
            print('5. Contratar un mensajero')
            print('6. Cerrar sesión')

            opcion = input('Ingresa el número de la opción que deseas realizar: ')

            if opcion == '1':
                agregar_articulo(usuario)  # Agregar el nombre de usuario como parámetro

            elif opcion == '2':
                ver_mis_publicaciones(usuario)

            elif opcion == '3':
                print("ver_articulos_disponibles()") # Esta función está próxima a desarrollarse

            elif opcion == '4':
                print("bandeja_de_mensajes(usuario)") # Esta función está próxima a desarrollarse

            elif opcion == '5':
                print("contratar_mensajero(usuario)") # Esta función está próxima a desarrollarse

            elif opcion == '6':
                print('¡Hasta pronto!')
                break

            else:
                print('Opción inválida. Por favor, ingresa un número del 1 al 6.')
    else:
        print('Nombre de usuario o contraseña incorrectos.')

def ver_mis_publicaciones(usuario):
    try:
        df_articulos = pd.read_csv('articulos.csv', usecols=['todo', 'usuario'])
    except IOError:
        print('Error: no se puede acceder al archivo de artículos.')
        return

    mis_articulos = df_articulos[df_articulos['usuario'] == usuario]['todo']

    if len(mis_articulos) == 0:
        print('No tienes artículos publicados.')
    else:
        print('Estos son tus artículos publicados:')
        print('\n'.join(mis_articulos))
    
    while True:
        opcion = input('\nPresiona "1" para regresar al menú principal')
        if opcion == '1':
            return
        else:
            print('Opción inválida. Por favor, intenta de nuevo.') 



