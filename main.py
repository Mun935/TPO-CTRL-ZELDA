from validaciones import validarOpcion
from funciones import iniciarSesion, crearUsuario

def main():
    """
    Lanza el programa mostrando el menú principal.

    Muestra un menú de acceso al sistema y redirige al flujo correspondiente
    según la opción ingresada por el usuario. Llama a la función 'validarOpcion'
    del módulo 'validaciones' para asegurar que la entrada esté dentro del rango válido.

    Argumentos:
        None

    Returns:
        None
    """
    print(f"\nAcceso al sistema. Seleccione la opción que corresponda:")
    print(f"1 - Usuario existente.")
    print(f"2 - Nuevo usuario")
    print(f"3 - Salir")
    
    opcion = int(input(f"\nOpción elegida: "))
    opcion = validarOpcion(opcion, 1, 3)

    if opcion == 1:
        iniciarSesion()
    elif opcion == 2:
        crearUsuario()
    else:
        salirPrograma()
main()