import pandas as pd

def agregar_usuario():
    # Solicitar al usuario que ingrese los valores para cada campo
    nombre = input('Ingrese su Nombre ')
    username = input('Ingrese el nombre de usuario: ')
    ocupacion = input('Ingrese la ocupación del usuario: ')
    email = input('Ingrese la dirección de correo electrónico del usuario: ')
    password = input('Ingrese la contraseña del usuario: ')

    # Leer el archivo CSV existente en un DataFrame
    try:
        df = pd.read_csv('usuarios.csv')
    except FileNotFoundError:
        # Si el archivo no existe, crear un DataFrame vacío
        df = pd.DataFrame()

    # Verificar si el nombre de usuario ya existe en el DataFrame
    if username in df['Username'].values:
        print('Error: El nombre de usuario ya existe en el archivo.')
        return

    # Crear un nuevo DataFrame con los datos del usuario
    usuario = pd.DataFrame({
        'Nombre': [nombre],
        'Username': [username],
        'Ocupación': [ocupacion],
        'Email': [email],
        'Password': [password]
    })

    # Agregar el nuevo usuario al DataFrame existente
    df = pd.concat([df, usuario], ignore_index=True)

    # Guardar el DataFrame actualizado en el archivo CSV
    df.to_csv('usuarios.csv', index=False)
