from datos import usuarios, empleados, tupla_empleados, proyectos, tupla_proyectos
from validaciones import validarOpcion, validarPass, buscarLegajo, legajoNoVacio, buscarIDProyecto, IDProyNoVacio

import getpass
import random

def cambiarDatosEmpleados(legajoActual, opcion):
    """
    Aplica un cambio sobre un empleado identificado por su legajo, según
    la opción de campo seleccionada en el menú.

    Parámetros:
        legajoActual (str): Legajo del empleado que se desea modificar.
        opcion (int): Opción del submenú de modificación:
            1 = legajo
            2 = nombre
            3 = apellido
            4 = puesto (área)
            5 = seniority

    Retorna:
        bool: True si el cambio se aplicó correctamente, False si hubo error
        (opción inválida, campo inválido o empleado no encontrado).

    Detalles:
        - Traduce la opción numérica a un nombre de campo (legajo, nombre, etc.).
        - Pide el nuevo valor por teclado.
        - Si el campo es 'legajo', valida que no esté vacío ni duplicado
          usando la función 'legajoNoVacio'.
        - Busca el índice de la columna a modificar con 'tupla_empleados'
          (diccionario campo -> índice).
        - Recorre la matriz 'empleados', encuentra la fila por 'legajoActual'
          y reemplaza el valor en la columna correspondiente.
    """
    if opcion == 1:
        campo = "legajo"
    elif opcion == 2:
        campo = "nombre"
    elif opcion == 3:
        campo = "apellido"
    elif opcion == 4:
        campo = "puesto"     
    elif opcion == 5:
        campo = "seniority"
    else:
        print(f"\nError. Opción inválida.")
        return False
    
    valorNuevo = input(f"\nNuevo valor para {campo}: ").strip()

    if campo == "legajo":
        valorNuevo = legajoNoVacio(valorNuevo)

    col = tupla_empleados.get(campo)
    if col is None:
        print(f"\nError. Campo inválido.")
        return False

    for fila in empleados:
        if fila[0] == legajoActual:
            fila[col] = valorNuevo
            print(f"\n{campo.capitalize()} actualizado.")
            return True

    print(f"\nNo se pudo actualizar {campo} (empleado no encontrado).")
    return False
    
def crearUsuario():
    """
    Permite crear un nuevo usuario en el sistema.

    Flujo:
        - Solicita al usuario ingresar un nombre de usuario.
            * Debe contener solo letras (validación con isalpha).
            * Se verifica que no exista previamente en la lista 'usuarios'.
        - Solicita al usuario crear una contraseña.
            * Se valida con la función 'validarPass' que cumpla con los requisitos:
                - Longitud entre 8 y 12 caracteres.
                - Contener letras, números y al menos un símbolo.
        - Si las validaciones son correctas:
            * El nuevo usuario se agrega a la lista 'usuarios' con su contraseña.
            * Se muestra un mensaje de confirmación.

    Notas:
        - La lista 'usuarios' tiene formato [[usuario, contraseña], ...].
        - Se utiliza 'getpass' para ocultar la contraseña al escribirla.
        - El nombre de usuario se guarda en minúsculas, pero se muestra en mayúsculas
          al confirmar la creación.
    """
    print("\n==============================================")
    print("===============   Nuevo usuario   ==============")
    print("==============================================\n")
    user_id = input("Elija un nombre de usuario: ").lower()

    while not user_id .isalpha():
        print(f"\nEl nombre de usuario {user_id} debe contener solo letras.\n")
        user_id = input("Elija un nombre de usuario: ").lower()

    existe_user_id = [u for u in usuarios if u[0] == user_id]
    
    while len(existe_user_id) > 0:
        print("\nEl usuario ya se encuentra registado.\n")
        user_id = input("Elija un nombre de usuario: ").lower()
        existe_user_id = [u for u in usuarios if u[0] == user_id]

        while not user_id .isalpha():
            print(f"El nombre de usuario {user_id} debe contener solo letras. Elija uno diferente.")
            user_id = input("Elija un nombre de usuario: ").lower()
            existe_user_id = [u for u in usuarios if u[0] == user_id]

    new_pass = getpass.getpass("Ingrese su contraseña: ").lower()
    while not validarPass(new_pass):
        print(f"La contraseña ingrsada debe tener entre 8 y 12 caracteres,")
        print(f"Debe incluir letras, números y al menos un símbolo.")
        new_pass = getpass.getpass("Ingrese su contraseña: ").lower()      

    usuarios.append([user_id, new_pass])

    print(f"\nEl usuario {user_id.upper()} fue creado correctamente.")
    print(f"Por favor inicie sesión con sus credenciales\n")

def iniciarSesion():
    """
    Permite a un usuario iniciar sesión en el sistema validando su nombre de usuario y contraseña.

    Flujo:
        - Solicita al usuario ingresar su nombre de usuario.
        - Verifica si el usuario existe en la lista 'usuarios'.
            * Si no existe, vuelve a solicitar hasta que se ingrese un usuario válido.
        - Solicita la contraseña correspondiente al usuario.
        - Valida que la contraseña coincida con la registrada en la lista 'usuarios'.
            * Si es incorrecta, vuelve a solicitar hasta que sea válida.
        - Una vez validadas las credenciales, muestra un mensaje de acceso correcto
          y redirige al menú principal.

    Notas:
        - La lista 'usuarios' se espera con formato: [[usuario, contraseña], ...]
        - Se utiliza 'getpass' para ocultar la contraseña al escribirla.
        - Convierte a minúsculas tanto el usuario como la contraseña para uniformidad.
    """
    nombreUsuario = input("\nPor favor, ingrese su usuario: ").lower()
    existe_usuario = [u for u in usuarios if u[0] == nombreUsuario]

    while len(existe_usuario) == 0:
        print(f"\nEl usuario ingresado no se encuentra registrado. Intente nuevamente.\n")
        nombreUsuario = input("Por favor, ingrese su usuario: ").lower()
        existe_usuario = [u for u in usuarios if u[0] == nombreUsuario]

    contraseñaUsuario = getpass.getpass("Ingrese su contraseña: ").lower()
    existe_usuario_contraseña = [u for u in usuarios if u[0] == nombreUsuario and u[1] == contraseñaUsuario]
    
    while len (existe_usuario_contraseña) == 0:
        print("\nLa contraseña ingresada es incorecta. Intente nuevamente.")
        contraseñaUsuario = getpass.getpass("\nIngrese su contraseña: ").lower()
        existe_usuario_contraseña = [u for u in usuarios if u[0] == nombreUsuario and u[1] == contraseñaUsuario]

    print(f"\nAcceso correcto. Redireccionando al menu principal...\n")
    menuPrincipal()

def gestionEmpleados():
    """
    Muestra el submenú de Gestión de Empleados y redirige a la opción seleccionada.

    Opciones disponibles:
        1 - Alta de empleado: permite dar de alta un nuevo registro de empleado.
        2 - Baja de empleado: permite eliminar un empleado existente.
        3 - Modificación de empleado: permite modificar los datos de un empleado.
        4 - Listado completo de empleados: muestra todos los empleados registrados.
        5 - Búsqueda por legajo: busca y muestra un empleado según su legajo.
        6 - Búsqueda por apellido: busca empleados que coincidan con un apellido.
        7 - Búsqueda por área: busca empleados filtrados por su área/puesto.
        8 - Búsqueda por seniority: busca empleados filtrados por nivel de seniority.
        9 - Volver al menú principal: retorna al menú principal del sistema.

    Flujo:
        - Muestra las opciones del submenú.
        - Solicita al usuario ingresar una opción.
        - Valida que la opción esté dentro del rango permitido (1 a 9).
        - Ejecuta la función correspondiente según la opción seleccionada.
    """
    print("===============================================")
    print("==========    Gestión de Empleados    =========")
    print("===============================================")
    print("1 - Alta de empleado")
    print("2 - Baja de empleado")
    print("3 - Modificación de empleado")
    print("4 - Listado completo de empleados")
    print("5 - Búsqueda de empleado por legajo")
    print("6 - Búsqueda de empleado por apellido")
    print("7 - Búsqueda de empleado por área")
    print("8 - Búsqueda de empleado por seniority")
    print("9 - Volver al menú principal")    

    opcion = int(input(f"\nOpción elegida: "))
    opcion = validarOpcion(opcion, 1, 9)

    if opcion == 1:
        altaEmpleado()
    elif opcion == 2:
        bajaEmpleado()
    elif opcion == 3:
        modificarEmpleado()
    elif opcion == 4:
        listarEmpleados()
    elif opcion == 5:
        buscarEmpleados(opcion)
    elif opcion == 6:
        buscarEmpleados(opcion)
    elif opcion == 7:
        buscarEmpleados(opcion)
    elif opcion == 8:
        buscarEmpleados(opcion)
    else:
        return

def altaEmpleado():
    """
    Permite dar de alta (registrar) un nuevo empleado en el sistema.

    Flujo:
        - Solicita al usuario los datos del nuevo empleado:
            * Nombre
            * Apellido
            * Año de ingreso
            * Puesto
            * Seniority
        - Genera un número de legajo aleatorio único entre 10000 y 11999.
        - Valida que el legajo no exista en la matriz 'empleados'.
        - Agrega el nuevo registro a la matriz 'empleados'.
        - Muestra confirmación de alta con los datos del empleado.
        - Permite al usuario:
            1) Dar de alta otro empleado (recursivo).
            2) Volver al menú de Gestión de Empleados.
    """
    print("===============================================")
    print("============    Alta de Empleados   ===========")
    print("===============================================")
    print(f"\nPara dar de alta a un empleado nuevo, complete los siguientes datos.")

    nombre = input(f"\nNombre: ")
    apellido = input(f"Apellido: ")
    año_ingreso = int(input(f"Año de ingreso a la compañía: "))
    puesto = input(f"Puesto que desempeña: ")
    seniority = input(f"Nivel de seniority: ")
    
    legajo = str(random.randint(10000, 11999))
    existe_legajo = [l for l in empleados if l[0] == legajo]
    while len(existe_legajo) > 0:
        legajo = str(random.randint(10000, 11999))
        existe_legajo = [l for l in empleados if l[0] == legajo]

    empleados.append([str(legajo), nombre, apellido, año_ingreso, puesto, seniority])

    print(f"\nEmpleado {nombre} {apellido} dado de alta con legajo {legajo}.\n")

    print("1 - Dar de alta otro empleado")
    print("2 - Volver al menú anterior")
    
    opcion = int(input(f"\nOpción elegida: "))
    opcion = validarOpcion(opcion,1,2)

    if opcion == "1":
        altaEmpleado()
    else:
        gestionEmpleados()

def bajaEmpleado():
    """
    Permite dar de baja (eliminar) un empleado del sistema.

    Flujo:
        - Muestra un submenú con opciones:
            1) Buscar un empleado por legajo y eliminarlo.
            2) Listar todos los empleados para seleccionar manualmente.
            3) Volver al menú anterior.
        - Si se busca por legajo:
            * Se obtiene el registro del empleado.
            * Se solicita confirmación al usuario antes de eliminarlo.
            * Si se confirma, se elimina el empleado de la matriz 'empleados'.
        - Si se listan los empleados:
            * Se muestran en pantalla todos los legajos y nombres.
            * Luego retorna al submenú de baja.
        - En cualquier caso, permite volver al menú de Gestión de Empleados.

    Notas:
        - La función es recursiva: tras una baja o listado vuelve a invocar `bajaEmpleado()`
          hasta que el usuario elija volver al menú anterior.
        - Utiliza la función `buscarLegajo()` para obtener el empleado a partir del legajo ingresado.
    """
    print("\n===============================================")
    print("============    Baja de Empleados   ===========")
    print("===============================================")
    print(f"\nPara dar de baja a un empleado, ingrese el número de legajo. En caso de no recordarlo, puede listar a los empleados.")
    print("1 - Buscar por legajo")
    print("2 - Listar empleados")
    print("3 - Volver al menú anterior")

    opcion = int(input(f"\nOpción elegida: "))
    opcion = validarOpcion(opcion, 1, 3)

    if opcion == 1:
        empleado = buscarLegajo()
        print(f"Empleado encontrado: {empleado[1]} {empleado[2]} - Legajo: {empleado[0]}")
        print("\n¿Desea eliminar al empleado seleccionado?")
        print("\n1 - Si")
        print("2 - No")

        opcion = int(input(f"\nOpción elegida: "))
        opcion = validarOpcion(opcion, 1, 2)

        if opcion == 1:
            empleados.remove(empleado)
            print(f"\nEl empleado con legajo Nº {empleado[0]} fue eliminado correctamente.")
            bajaEmpleado()
        else:
            bajaEmpleado()
    elif opcion == 2:
        for emp in empleados:
            print(f"Legajo: {emp[0]} - {emp[1].title()} {emp[2].title()}")
        bajaEmpleado()
    else:
        gestionEmpleados()

def modificarEmpleado():
    """
    Permite modificar los datos de un empleado existente en el sistema.

    Flujo:
        - Muestra un submenú inicial con opciones:
            1) Buscar empleado por legajo para modificar.
            2) Listar todos los empleados y volver a este menú.
            3) Volver al menú principal de gestión de empleados.
        - Si se busca por legajo:
            * Muestra los datos del empleado encontrado.
            * Pregunta si se desea modificar.
            * En caso afirmativo, muestra un submenú de modificaciones:
                1. Modificar legajo
                2. Modificar nombre
                3. Modificar apellido
                4. Modificar área (campo "puesto")
                5. Modificar seniority
                6. Volver al menú anterior
            * Después de cada cambio, pregunta si se quiere realizar otra modificación
              sobre el mismo empleado o salir del submenú.
        - Si se listan empleados:
            * Muestra legajo y nombre/apellido de todos.
            * Retorna al submenú de modificación.
        - Si se elige volver:
            * Retorna directamente al menú de gestión de empleados.

    Notas:
        - El bucle interno permite realizar múltiples cambios sobre el mismo empleado
          antes de volver al menú anterior.
        - La función `cambiarDatosEmpleados` se encarga de aplicar las modificaciones
          sobre la matriz 'empleados'.
    """
    print("\n===============================================================")
    print("============    Modificación de datos de Empleados   ===========")
    print("================================================================")
    print(f"\nPara dar modifcar el dato de un empleado, ingrese el número de legajo. En caso de no recordarlo, puede listar a los empleados.")
    print("1 - Buscar por legajo")
    print("2 - Listar empleados")
    print("3 - Volver al menú anterior")

    opcion = int(input(f"\nOpción elegida: "))
    opcion = validarOpcion(opcion, 1, 3)

    if opcion == 1:
        empleado = buscarLegajo()
        print(f"Empleado encontrado: {empleado[1]} {empleado[2]} - Legajo: {empleado[0]}")
        print("\n¿Desea modificar los datos del empleado seleccionado?")
        print("\n1 - Si")
        print("2 - No")

        opcion = int(input(f"\nOpción elegida: "))
        opcion = validarOpcion(opcion, 1, 2)

        if opcion == 1:
            while True:
                print("\n===============================================================")
                print("============    Modificación de datos de Empleados   ===========")
                print("================================================================")
                print(f"\nSeleccione la opción que desee: ")
                print("1 - Modificar legajo")
                print("2 - Modificar nombre")
                print("3 - Modificar apellido")
                print("4 - Modificar área")
                print("5 - Modificar seniority")
                print("6 - Volver al menú anterior")

                opcion = int(input(f"\nOpción elegida: "))
                opcion = validarOpcion(opcion, 1, 6)

                if opcion == 6:
                    return
                cambiarDatosEmpleados(empleado[0], opcion)

                print(f"\n¿Desea realizar otro cambio?")
                print("1 - Si")
                print("2 - No")
                opcion = int(input(f"\nOpción elegida: "))
                opcion = validarOpcion(opcion, 1, 2)

                if opcion == 2:
                    modificarEmpleado()
        else:
            return
    elif opcion == 2:
        for emp in empleados:
            print(f"Legajo: {emp[0]} - {emp[1].title()} {emp[2].title()}")
        modificarEmpleado()
    else:
        gestionEmpleados()

def listarEmpleados():
    print("\n===============================================")
    print("===========   Listado de Empleados   ==========")
    print("===============================================\n")

    print(f"{'Legajo':<8} | {'Nombre':<10} | {'Apellido':<12} | {'Ingreso':<7} | {'Área':<12} | {'Seniority':<12}")
    print("-" * 70)

    for e in empleados:
        print(f"{e[0]:<8} | {e[1]:<10} | {e[2]:<12} | {e[3]:<7} | {e[4]:<12} | {e[5]:<12}")

def buscarEmpleados(opcion):
    if opcion == 5:
        campo = 0
        criterio = input("Ingrese el legajo: ").strip()
    elif opcion == 6:
        campo = 2
        criterio = input("Ingrese el apellido: ").strip()
    elif opcion == 7:
        campo = 4
        criterio = input("Ingrese el area: ").strip()
    elif opcion == 8:
        campo = 5
        criterio = input("Ingrese el seniority: ").strip()
    
    resultado = [e for e in empleados if str(e[campo]).lower() == criterio.lower()]
    resultado = sorted(resultado, key=lambda e: (e[1].lower(), e[2].lower()))

    if not resultado:
        print("\nNo se encontraron empleados con ese criterio.\n")
    else:
        print("\nResultados de la búsqueda:\n")
    for e in resultado:
        print(f"Legajo: {e[0]} | {e[1]} {e[2]} | Ingreso: {e[3]} | Área: {e[4]} | Seniority: {e[5]}")
    
    return resultado
     
#-----------------PROYECTOS
def gestionProyectos():
    print("===============================================")
    print("==========    Gestión de Proyectos    =========")
    print("===============================================")
    print("1 - Crear proyecto")
    print("2 - Modificar proyecto")
    print("3 - Eliminar proyecto")
    print("4 - Dar por finalizado el proyecto")
    print("5 - Listar proyectos")
    print("6 - Volver al menú principal")    
    opcion = int(input(f"\nOpción elegida: "))
    opcion = validarOpcion(opcion, 1, 6)
    if opcion == 1:
        crearProyecto()
    if opcion == 2:
        modificarProyecto()
    if opcion == 3:
        eliminarProyecto()
    if opcion == 4:
        finalizarProyecto()
    if opcion == 5:
        listarProyectos()
    if opcion == 6:
        menuPrincipal()

def listarProyectos():
    #Modificar para que despues de mostrar los proyectos, vuelva a gestion de proyectos

    print("\n===============================================")
    print("===========   Listado de Proyectos   ==========")
    print("===============================================\n")


    print(f"{'ID':<6} | {'Cliente':<20} | {'Nombre Proyecto':<40} | {'Team Leader':<20} | {'Tipo':<15} | {'Inicio':<10} | {'Fin':<10}")
    print("-" * 120)

    for p in proyectos:
        print(f"{p[0]:<6} | {p[1]:<20} | {p[2]:<40} | {p[3]:<20} | {p[4]:<15} | {p[5]:<10} | {p[6]:<10}")

    gestionProyectos()

def cambiarDatosProyectos(IDActual, opcion):
    """
    Aplica un cambio sobre un proyecto identificado por su ID, según
    la opción de campo seleccionada en el menú.

    Parámetros:
        IDActual (str): ID del proyecto que se desea modificar.
        opcion (int): Opción del submenú de modificación:
            "empresa_cliente": 1,
            "nombre_proyecto": 2,
            "team_leader": 3,
            "tipo_proyecto": 4,
            "fecha_inicio": 5,
            "fecha_fin": 6
            
    Retorna:
        bool: True si el cambio se aplicó correctamente, False si hubo error
        (opción inválida, campo inválido o empleado no encontrado).

    Detalles:
        - Traduce la opción numérica a un nombre de campo (ID, nombre, etc.).
        - Pide el nuevo valor por teclado.
        - Si el campo es 'ID', valida que no esté vacío ni duplicado
          usando la función 'legajoNoVacio'.
        - Busca el índice de la columna a modificar con 'tupla_proyectos'
          (diccionario campo -> índice).
        - Recorre la matriz 'proyectos', encuentra la fila por 'IDActual'
          y reemplaza el valor en la columna correspondiente.
    """
    if opcion == 1:
        campo = "empresa_cliente"
    elif opcion == 2:
        campo = "nombre_proyecto"
    elif opcion == 3:
        campo = "team_leader"
    elif opcion == 4:
        campo = "tipo_proyecto"     
    elif opcion == 5:
        campo = "fecha_inicio" 
    elif opcion == 6:
        campo = "fecha_fin"
    else:
        print(f"\nError. Opción inválida.")
        return False
    
    valorNuevo = input(f"\nNuevo valor para {campo}: ").strip()

    if campo == "id":
        valorNuevo = IDProyNoVacio(valorNuevo)

    col = tupla_proyectos.get(campo)
    if col is None:
        print(f"\nError. Campo inválido.")
        return False    
    
    for fila in proyectos:
        if fila[0] == IDActual:
            fila[col] = valorNuevo
            print(f"\n{campo.capitalize()} actualizado.")
            return True
    
    print(f"\nNo se pudo actualizar {campo} (proyecto no encontrado).")
    return False

def modificarProyecto():
    """
Permite modificar los datos de un proyecto existente en el sistema.
    Flujo:
        - Muestra un submenú inicial con opciones:
            1) Buscar proyecto por ID_proy para modificar.
            2) Listar todos los proyectos y volver a este menú.
            3) Volver al menú principal de gestión de proyectos.
        - Si se busca por ID_proy:
            * Muestra los datos del proyecto encontrado.
            * Pregunta si se desea modificar.
            * En caso afirmativo, muestra un submenú de modificaciones:
                1. Modificar Empresa cliente
                2. Modificar Nombre del proyecto
                3. Modificar Team Leader
                4. Modificar Tipo de proyecto
                5. Modificar Fecha de inicio
                6. Modificar Fecha de fin
                7. Volver al menú anterior
            * Después de cada cambio, pregunta si se quiere realizar otra modificación
              sobre el mismo proyecto o salir del submenú.
        - Si se listan proyectos:
            * Muestra ID, Empresa_Cliente, Nombre_Proyecto de todos.
            * Retorna al submenú de modificación.
        - Si se elige volver:
            * Retorna directamente al menú de gestión de proyectos.

    Notas:
        - El bucle interno permite realizar múltiples cambios sobre el mismo proyecto
          antes de volver al menú anterior.
        - La función `cambiarDatosProyectos` se encarga de aplicar las modificaciones
          sobre la matriz 'proyectos'.
    """
    print("\n===============================================================")
    print("============    Modificación de datos de Proyectos   ===========")
    print("================================================================")
    print(f"\nPara dar modifcar el dato de un proyecto, ingrese el ID del proyecto. En caso de no recordarlo, puede listar los proyectos.")
    print("1 - Buscar por ID")
    print("2 - Listar proyectos")
    print("3 - Volver al menú anterior")

    opcion = int(input(f"\nOpción elegida: "))
    opcion = validarOpcion(opcion, 1, 3)

    if opcion == 1:
        proyecto = buscarIDProyecto()
        print(f"Proyecto encontrado: {proyecto[1]} {proyecto[2]}- ID: {proyecto[0]}")
        print("\n¿Desea modificar los datos del proyecto seleccionado?")
        print("\n1 - Si")
        print("2 - No")

        opcion = int(input(f"\nOpción elegida: "))
        opcion = validarOpcion(opcion, 1, 2)

        if opcion == 1:
            while True:
                print("\n===============================================================")
                print("============    Modificación de datos de Proyectos   ===========")
                print("================================================================")
                print(f"\nSeleccione la opción que desee: ")
                print("1 - Modificar Empresa cliente")
                print("2 - Modificar Nombre del proyecto")
                print("3 - Modificar Team Leader")
                print("4 - Modificar Tipo de proyecto")
                print("5 - Modificar Fecha de inicio")
                print("6 - Modificar Fecha de fin")
                print("7 - Volver al menú anterior")

                opcion = int(input(f"\nOpción elegida: "))
                opcion = validarOpcion(opcion, 1, 7)

                if opcion == 7:
                    return
                cambiarDatosProyectos(proyecto[0], opcion)

                print(f"\n¿Desea realizar otro cambio?")
                print("1 - Si")
                print("2 - No")
                opcion = int(input(f"\nOpción elegida: "))
                opcion = validarOpcion(opcion, 1, 2)

                if opcion == 2:
                    gestionProyectos()
        else:
            return 
    elif opcion == 2:
        for proy in proyectos:
            print(f"ID: {proy[0]} - {proy[1]} - {proy[2]}")
        gestionProyectos()
    else:
        gestionProyectos()

#[ID_Proyecto, Empresa_Cliente, Nombre_Proyecto, Team_Leader, Tipo_Proyecto, Fecha_Inicio, Fecha_Fin]
def crearProyecto():
    print("===============================================")
    print("============     Nuevo Proyecto     ===========")
    print("===============================================")
    print(f"\nPara crear un proyecto, complete los siguientes datos.")
    empresa = input(f"Nombre empresa: ")
    proyecto = input(f"Nombre proyecto: ")
    leader = input(f"Nombre Team Leader: ")
    tipo_proy = input(f"Tipo de proyecto: ")
    fecha_ini_proy = input(f"Fecha de inicio (AAAA-MM-DD): ")
    fecha_fin_proy = input(f"Fecha de fin (AAAA-MM-DD): ")
    # Verifica que la fecha de inicio sea anterior a la fecha de fin    
    while fecha_ini_proy >= fecha_fin_proy:
        print(f"\nLa fecha de inicio debe ser anterior a la fecha de fin. Intente nuevamente.")
        fecha_ini_proy = input(f"Fecha de inicio (AAAA-MM-DD): ")
        fecha_fin_proy = input(f"Fecha de fin (AAAA-MM-DD): ")
    
    # Toma el último ID
    ultimo_id = proyectos[-1][0]  
    new_id_list = list(filter(lambda x: x.isnumeric(), ultimo_id))
    new_id = int("".join(new_id_list))
    new_id_sumado = new_id + 1
    id_proy = f"PRJ{new_id_sumado:03d}"
    # Verifica que el id_proy nuevo no exista en la lista proyectos. Si existe, genera un nuevo ID
    # (esto es para evitar que se repita el ID de un proyecto ya existente)
    existe_id_proy = [p for p in proyectos if p[0] == id_proy]
    while len(existe_id_proy) > 0:
        new_id_sumado += 1
        id_proy = f"PRJ{new_id_sumado:03d}"
        existe_id_proy = [p for p in proyectos if p[0] == id_proy]
    
    # Agrega el nuevo proyecto a la lista
    proyectos.append([id_proy, empresa, proyecto, leader, tipo_proy, fecha_ini_proy, fecha_fin_proy])
    print(f"\nProyecto {proyecto} creado correctamente con ID {id_proy}.\n")

    #Vuelve a gestion de proyectos
    gestionProyectos()

def eliminarProyecto():
    print("===============================================")
    print("============   Eliminar Proyecto   ===========")
    print("===============================================")

    print(f"\nPara eliminar un proyecto, ingrese el ID del proyecto a eliminar.")

    id_proy = input(f"ID del proyecto: ").upper()

    # Verifica si el ID existe, si no existe, solicita que se ingrese un ID válido
    existe_proyecto = [p for p in proyectos if p[0] == id_proy]

    while len(existe_proyecto) == 0:
        print(f"\nEl ID de proyecto {id_proy} no existe. Intente nuevamente.")
        id_proy = input(f"ID del proyecto: ").upper()
        existe_proyecto = [p for p in proyectos if p[0] == id_proy]
    print(f"\nProyecto {id_proy} encontrado. Procediendo a eliminar...\n")

    # Elimina el proyecto
    proyectos.remove(existe_proyecto[0])
    print(f"\nProyecto {id_proy} eliminado correctamente.")

    gestionProyectos()
    
#---------------------------------------------------------------------

def menuPrincipal():
    """
    Muestra el menú principal del sistema TrackPoint y redirige a la opción seleccionada.

    Opciones disponibles:
        1 - Gestión de Empleados: accede al submenú de operaciones sobre empleados.
        2 - Gestión de Proyectos: accede al submenú de proyectos.
        3 - Gestión de Asignaciones: accede al submenú de asignaciones.
        4 - Consultas y Reportes: accede al submenú de reportes.
        5 - Utilidades: accede al submenú de herramientas adicionales.
        6 - Cerrar sesión: finaliza la sesión actual y sale del sistema.

    Flujo:
        - Muestra las opciones disponibles.
        - Solicita al usuario ingresar una opción.
        - Valida que la opción esté dentro del rango permitido (1 a 6).
        - Ejecuta la función correspondiente según la opción seleccionada.
    """
    print("===============================================")
    print("===============    TrackPoint    ==============")
    print("===============================================")
    print("1 - Gestión de Empleados")
    print("2 - Gestión de Proyectos")
    print("3 - Gestión de Asignaciones")
    print("4 - Consultas y Reportes")
    print("5 - Utilidades")
    print("6 - Cerrar sesión")

    opcion = int(input(f"\nOpción elegida: "))
    opcion = validarOpcion(opcion, 1, 6)

    if opcion == 1:
        gestionEmpleados()
    elif opcion == 2:
        gestionProyectos()
    elif opcion == 3:
        gestionAsignaciones()
    elif opcion == 4:
        consultasReportes()
    elif opcion == 5:
        utilidades()
    else:
        salirSistema()
