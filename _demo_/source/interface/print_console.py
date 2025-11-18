def print_login():
    print(
        """
Acceso al Sistema
Seleccione una opción:
1. 🔐 Iniciar sesión
2. 🧾 Crear usuario
3. 🚪 Salir
        """
    )

def print_main_menu():
    print(
        """
Menú Principal
1. 👤 Gestión de Empleados
2. 🏗️  Gestión de Proyectos
3. 🔄 Gestión de Asignaciones
4. 📊 Consultas y Reportes
5. 🚪 Cerrar sesión
        """
    )

def print_employee_menu():
    print(
        """
Gestión de Empleados
1. 🆕 Alta de empleado
2. ❌ Baja de empleado
3. 📝 Modificar datos de un empleado
4. 🔙 Volver al menú principal
        """
    )

def print_new_employee():
    print(
        """
🆕 Vamos a registrar un nuevo empleado.
Por favor, complete los siguientes datos:
        """
    )

def print_add_new_user():
    print(
        """
¿Desea registrar otro empleado?
1. ✅ Sí, continuar
2. 🔙 No, volver al menú anterior
        """
    )

def print_delete_employee():
    print(
        """
🗑️ Vamos a dar de baja a un empleado.
Seleccione una opción:
1. 🔍 Ingresar legajo
2. 🔙 Volver al menú anterior
        """
    )

def print_delete_another_employee():
    print(
        """
¿Desea dar de baja a otro empleado?
1. ✅ Sí, continuar
2. 🔙 No, volver al menú anterior
        """
    )

def print_modify_employee():
    print(
        """
🛠️ Vamos a modificar los datos de un empleado.
Seleccione una opción:
1. ✏️ Ingresar legajo
2. 🔙 Volver al menú anterior
        """
    )

def print_employee_data(employee):
    if not employee:
        print("❌ Empleado no encontrado.")
        return

    print("\n📋 Datos del empleado:")
    print(f"🔢 Legajo     : {employee['employee_id']}")
    print(f"👤 Nombre     : {employee['name']} {employee['last_name']}")
    print(f"📅 Año ingreso: {employee['start_year']}")
    print(f"💼 Puesto     : {employee['position']}")
    print(f"⭐ Seniority  : {employee['seniority']}")

def print_project_menu():
    print("""
Gestión de Proyectos
1. 🆕 Crear proyecto
2. 📝 Modificar proyecto
3. ❌ Eliminar proyecto
4. 🔙 Volver al menú principal
        """
    )

def print_new_project():
    print(
        """
🆕 Vamos a crear un nuevo proyecto.
Por favor, complete los siguientes datos:
        """
    )

def print_add_new_project():
    print(
        """
¿Desea agregar otro proyecto?
1. ✅ Sí, continuar
2. 🔙 No, volver al menú anterior
        """
    )

def print_modify_project():
    print(
        """
🛠️ Vamos a modificar la información de un proyecto.
Seleccione una opción:
1. ✏️ Ingresar ID del proyecto
2. 🔍 Ver proyectos
3. 🔙 Volver al menú anterior
        """
    )

def print_project_data(project):
    if not project:
        print("❌ Proyecto no encontrado.")
        return

    print("\n📋 Datos del proyecto:")
    print(f"🔢 ID Proyecto: {project['project_id']}")
    print(f"👤 Cliente    : {project['project_client']}")
    print(f"🏗️ Nombre     : {project['project_name']}")
    print(f"👷 Líder      : {project['project_leader']}")
    print(f"🔩 Tipo       : {project['project_type']}")
    print(f"📅 Inicio     : {project['project_start_date']}")
    print(f"📅 Fin        : {project['project_end_date']}")

def print_project_list(projects):
    if not projects:
        print("\nℹ️ No hay proyectos registrados en el sistema.")
        return

    print("\n--- 📋 Lista de IDs de Proyectos ---")
    for prj in projects:
        print(f"  -> {prj['project_id']}")
    print("---------------------------------")

def print_delete_project():
    print(
        """
🗑️ Vamos a dar eliminar un proyecto.
Seleccione una opción:
1. 🔍 Ingresar ID del proyecto
2. 🔙 Volver al menú anterior
        """
    )

def print_delete_another_project():
    print(
        """
¿Desea eliminar otro proyecto?
1. ✅ Sí, continuar
2. 🔙 No, volver al menú anterior
        """
    )

def print_assignment_menu():
    print("""
Gestión de Asignaciones y Tareas
1. ➡️  Asignar Tarea a Empleado
2. 🔄  Actualizar Estado de Tarea
3. ✍️  Modificar / Desasignar Tarea
4. 📋  Gestionar Plantillas de Tareas
5. 🔙  Volver al Menú Principal
    """)

def print_assign_task():
    print("""
➡️  Vamos a asignar una nueva tarea
Por favor, seleccione el Proyecto, Empleado y Tarea.
    """)

def print_assign_another_task():
    print("""
¿Desea asignar otra tarea?
1. ✅ Sí, continuar
2. 🔙 No, volver al menú
    """)

def print_update_status():
    print("\n🔄 Actualizar Estado de Tarea")

def print_task_status_options(assignment):
    current_status = assignment.get("status")
    task_id = assignment.get("task_id")
    
    print(f"\nTarea: {task_id} (Asignación: {assignment.get('assignment_id')})")
    print(f"Estado actual: {current_status}")
    print("-" * 30)
    
    if current_status == "Sin Empezar":
        print("Seleccione una acción:")
        print("1. 🚀 Iniciar Tarea")
        print("2. 🔙 Cancelar")
    elif current_status == "En Curso":
        print("Seleccione una acción:")
        print("1. ✅ Completar Tarea")
        print("2. 🔙 Cancelar")
    else:
        print("ℹ️ Esta tarea ya está terminada. No hay más acciones.")
    
    return current_status

def print_modify_deassign():
    print("\n✍️ Modificar / Desasignar Tarea")

def print_modify_deassign_submenu(assignment):
    print(f"\nTarea: {assignment.get('task_id')}")
    print(f"Asignada a: {assignment.get('employee_id')}")
    print(f"Estado actual: {assignment.get('status')}")
    print("-" * 30)
    print("Seleccione una acción:")
    print("1. 👤 Modificar Empleado Asignado")
    print("2. ❌ Desasignar Tarea (Eliminar)")
    print("3. 🔙 Cancelar")

def print_task_template_menu():
    print("""
📋 Gestionar Plantillas de Tareas
1. 🆕 Crear nueva plantilla de tarea
2. 📝 Modificar plantilla de tarea
3. ❌ Eliminar plantilla de tarea
4. 🔙 Volver al menú anterior
    """)

def print_new_task_header():
    print("\n🆕 Creando nueva plantilla de tarea...")

def print_modify_task_header():
    print("\n📝 Modificando plantilla de tarea...")

def print_delete_task_header():
    print("\n❌ Eliminando plantilla de tarea...")

def print_reports_menu():
    print("""
📊 Consultas y Reportes
1. 📈 Ver Estadísticas Generales (Gráfico)
2. 🔍 Búsqueda Específica (Empleado/Proyecto/Tarea)
3. 🗂️ Ver Reporte Maestro (Empleados -> Proyectos -> Tareas)
4. 🔙 Volver al Menú Principal
    """)

def print_search_menu():
    print("""
🔍 Búsqueda Específica
1. 👤 Buscar Empleado por Legajo
2. 🏗️ Buscar Proyecto por ID
3. 📋 Buscar Plantilla de Tarea por ID
4. 🔙 Volver al Menú de Reportes
    """)

def print_master_report(report_data):
    print("\n--- 🗂️ Reporte Maestro del Sistema ---")
    for emp in report_data:
        print("\n" + "=" * 40)
        print(f"👤 EMPLEADO: {emp['name'].upper()} (Legajo: {emp['id']})")
        print(f"   Puesto: {emp['position']} ({emp['seniority']})")
        print("=" * 40)
        
        if not emp['projects']:
            print("  (Sin proyectos asignados en el sistema de equipos)")
            continue

        for proj in emp['projects']:
            print(f"  └── 🏗️ PROYECTO: {proj['name']} (ID: {proj['id']})")
            
            if not proj['tasks']:
                print("      (Sin tareas asignadas en este proyecto)")
            else:
                for task in proj['tasks']:
                    print(f"          └── 📋 TAREA: {task['name']} (ID: {task['id']})")
                    print(f"               Estado: {task['status']}")
    
    print("\n--- Fin del Reporte ---")

def print_task_template_data(task):
    if not task:
        print("❌ Plantilla de Tarea no encontrada.")
        return
    print("\n📋 Datos de la Plantilla de Tarea:")
    print(f"  ID Tarea : {task['task_id']}")
    print(f"  Nombre   : {task['task_name']}")
    print(f"  Cliente  : {task['client']}")
    print(f"  Seniority: {task['seniority']}")
    print(f"  Descrip. : {task['description']}")

def print_reports_menu():
    print("""
📊 Consultas y Reportes
1. 📈 Ver Estadísticas Generales (Gráfico)
2. 🔍 Búsqueda Específica (Empleado/Proyecto/Tarea)
3. 🗂️ Ver Reporte Maestro (Empleados -> Proyectos -> Tareas)
4. 🔙 Volver al Menú Principal
    """)

def print_search_menu():
    print("""
🔍 Búsqueda Específica
1. 👤 Buscar Empleado por Legajo
2. 🏗️ Buscar Proyecto por ID
3. 📋 Buscar Plantilla de Tarea por ID
4. 🔙 Volver al Menú de Reportes
    """)

def print_master_report(report_data):
    print("\n--- 🗂️ Reporte Maestro del Sistema ---")
    
    for emp in report_data:
        print("\n" + "=" * 40)
        print(f"👤 EMPLEADO: {emp['name'].upper()} (Legajo: {emp['id']})")
        print(f"   Puesto: {emp['position']} ({emp['seniority']})")
        print("=" * 40)
        
        if not emp['projects']:
            print("  (Sin proyectos asignados en el sistema de equipos)")
            continue

        for proj in emp['projects']:
            print(f"  └── 🏗️ PROYECTO: {proj['name']} (ID: {proj['id']})")
            
            if not proj['tasks']:
                print("      (Sin tareas asignadas en este proyecto)")
            else:
                for task in proj['tasks']:
                    print(f"          └── 📋 TAREA: {task['name']} (ID: {task['id']})")
                    print(f"               Estado: {task['status']}")
    
    print("\n--- Fin del Reporte ---")

def print_task_template_data(task):
    if not task:
        print("❌ Plantilla de Tarea no encontrada.")
        return
    print("\n📋 Datos de la Plantilla de Tarea:")
    print(f"  ID Tarea : {task['task_id']}")
    print(f"  Nombre   : {task['task_name']}")
    print(f"  Cliente  : {task['client']}")
    print(f"  Seniority: {task['seniority']}")
    print(f"  Descrip. : {task['description']}")

def _create_bar(value, total, bar_length=20):
    if total == 0:
        return "[ " + " " * bar_length + " ]"
    
    percentage = value / total
    filled_blocks = int(percentage * bar_length)
    empty_blocks = bar_length - filled_blocks
    bar = "█" * filled_blocks + " " * empty_blocks
    return f"[{bar}] {value} ({percentage:.0%})"

def print_statistics_report(stats):
    print("\n--- 📈 Estadísticas Generales ---")
    print(f"  👤 Empleados Totales: {stats['total_employees']}")
    print(f"  🏗️ Proyectos Totales: {stats['total_projects']}")
    print("-" * 30)
    print("  --- Estado de Tareas ---")
    
    total = stats['total_tasks']
    print(f"Sin Empezar: {_create_bar(stats['tasks_todo'], total)}")
    print(f"En Curso:    {_create_bar(stats['tasks_inprogress'], total)}")
    print(f"Terminadas:  {_create_bar(stats['tasks_done'], total)}")
    
    print("-" * 30)
    print(f"  📊 Porcentaje Completado: {stats['completion_percentage']:.2f} %")
    print("---------------------------------")

def print_back_to_menu():
    print("\n🔙 Volviendo al menú anterior...")

def print_warning(warning):
    print(f"\n⚠️  ATENCIÓN: {warning}")

def print_error(error):
    print(f"\n❌ ERROR: {error}")

