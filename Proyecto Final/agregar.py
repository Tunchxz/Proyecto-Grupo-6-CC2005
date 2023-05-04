import pandas as pd
def agregar_articulo(usuario):
    # Solicitar al usuario que ingrese los artículos que está ofreciendo
    print('¡Preparemos tu publicación!')
    articulos = input('¿Qué artículo(s) estás ofreciendo? ')

    # Crear un nuevo DataFrame con la fila de artículos y el nombre del usuario
    df = pd.DataFrame({'todo': [articulos], 'usuario': [usuario]})

    # Guardar los artículos en un archivo CSV
    try:
        df.to_csv('articulos.csv', mode='a', header=False, index=False)
    except IOError:
        print('Error: no se puede acceder al archivo de artículos.')
        return

    # Preguntar qué artículo desea obtener a cambio
    articulo_deseado = input('¿Qué artículo deseas obtener a cambio? ')

    # Verificar si el artículo deseado está en el archivo CSV "articulos.csv"
    try:
        df_articulos = pd.read_csv('articulos.csv')
    except IOError:
        print('Error: no se puede acceder al archivo de artículos.')
        return

    if articulo_deseado in df_articulos['todo'].tolist():
        print('¡Genial! Ya has encontrado un intercambio.')
    else:
        # Crear un nuevo DataFrame con la fila de la petición
        df_peticiones = pd.DataFrame({'todo': [articulo_deseado]})

        # Guardar la petición en un archivo CSV
        try:
            df_peticiones.to_csv('peticiones.csv', mode='a', header=False, index=False)
        except IOError:
            print('Error: no se puede acceder al archivo de peticiones.')
            return

        print('Se ha registrado tu petición. ¡Buena suerte encontrando un intercambio!')

