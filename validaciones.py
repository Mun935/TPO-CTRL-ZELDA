from datos import empleados, proyectos

def validarOpcion(opcion, minimo, maximo):
    """
    Valida que una opción numérica esté dentro de un rango permitido.

    Mientras la opción no se encuentre entre el mínimo y el máximo (inclusive),
    solicita al usuario que ingrese nuevamente un valor válido.

    Args:
        opcion (int): Valor inicial ingresado por el usuario.
        minimo (int): Valor mínimo permitido.
        maximo (int): Valor máximo permitido.

    Returns:
        int: La opción validada que se encuentra dentro del rango especificado.
    """
    while opcion < minimo or opcion > maximo:
        print(f"\nLa opción ingresada no es correcta. Intente nuevamente.")
        opcion = int(input(f"\nOpción elegida: "))
    return opcion

def validarPass(password):
    """
    Verifica si una contraseña cumple con los criterios de seguridad definidos.

    Una contraseña válida debe:
    - Tener entre 8 y 12 caracteres.
    - Incluir al menos una letra.
    - Incluir al menos un número.
    - Incluir al menos un símbolo (carácter no alfanumérico).

    Args:
        password (str): La contraseña a validar.

    Returns:
        bool: True si la contraseña es válida, False en caso contrario.
    """
    if 8 <= len(password) <= 12:
        tiene_letra = any(c.isalpha() for c in password)
        tiene_numero = any(c.isdigit() for c in password)
        tiene_simbolo = any(not c.isalnum() for c in password)
        return tiene_letra and tiene_numero and tiene_simbolo
    return False

def buscarLegajo():
    """
    Busca un empleado por legajo y lo retorna.

    Pide el legajo al usuario y valida contra la lista de empleados.
    Repite hasta encontrar una coincidencia.

    Args:
        empleados (list[list]): Matriz de empleados, donde cada empleado es una lista.

    Returns:
        list: El registro del empleado encontrado.
    """
    legajo= input("\nIngrese el legajo: ").strip()
    empleado = [e for e in empleados if e[0] == legajo]

    while len(empleado) == 0:
        print(f"\nNo se han encontrado empleados.")
        legajo = input("\nIngrese el legajo: ")
        empleado = [e for e in empleados if e[0] == legajo]

    empleado = empleado[0]
    return empleado

def buscarIDProyecto():
    """
    Busca un proyecto por su ID en la lista de empleados.

    Pide el ID del proyecto al usuario y valida contra la lista de proyectos.
    Repite hasta encontrar una coincidencia.

    Parámetros:
        proyectos (list[list]): Matriz de proyectos, donde cada proyecto es una lista.

    Retorna:
        list: El registro del proyecto encontrado, o una lista vacía si no se encuentra.
    """
    proyecto = input("\nIngrese el ID del proyecto: ").strip()
    idProyecto = [p for p in proyectos if p[0] == proyecto]

    while len(idProyecto) == 0:
        print(f"\nNo se han encontrado proyectos.")
        proyecto = input("\nIngrese el ID del proyecto: ").strip()
        idProyecto = [p for p in proyectos if p[0] == proyecto]
    
    idProyecto = idProyecto[0]
    return idProyecto

def legajoNoVacio(valorNuevo):
    """
    Valida que el legajo ingresado sea correcto.

    Parámetros:
        valorNuevo (str): El legajo ingresado por el usuario.

    Retorna:
        str: Un legajo válido, que no esté vacío y no exista en la lista de empleados.

    Detalles:
        - Mientras el valor sea una cadena vacía ("") o ya exista en la matriz 'empleados',
          se solicita nuevamente al usuario que ingrese otro legajo.
        - El bucle solo termina cuando se obtiene un legajo único y no vacío.
    """
    while any(e[0] == valorNuevo for e in empleados) or valorNuevo == "":
        if valorNuevo == "":
            print("El legajo no puede estar vacío.")
        else:
            print("Ese legajo ya existe. Ingrese otro.")
        valorNuevo = input("Nuevo legajo: ").strip()
    return valorNuevo

def IDProyNoVacio(valorNuevo):
    """
    Valida que el ID del proyecto ingresado sea correcto.

    Parámetros:
        valorNuevo (str): El ID del proyecto ingresado por el usuario.

    Retorna:
        str: Un ID de proyecto válido, que no esté vacío y no exista en la lista de proyectos.  
    Detalles:
        - Mientras el valor sea una cadena vacía ("") o ya exista en la matriz 'proyectos',
          se solicita nuevamente al usuario que ingrese otro ID de proyecto.
        - El bucle solo termina cuando se obtiene un ID de proyecto único y no vacío.
    """
    while any(p[0] == valorNuevo for p in proyectos) or valorNuevo == "":
        if valorNuevo == "":
            print("El ID del proyecto no puede estar vacío.")
        else:
            print("Ese ID de proyecto ya existe. Ingrese otro.")
        valorNuevo = input("Nuevo ID del proyecto: ").strip()
    return valorNuevo