from core import services
from interface import print_console
from interface import input_handlers
from interface import read_console
from shared import utilities

def handle_log_option():
    try:
        users = services.get_users()

        if not any(user for user in users if user.get("user", "").strip() and user.get("password", "").strip()):
            print_console.print_warning("No hay registros de usuarios. Primero deberá crear uno.")
            handle_new_user_menu()
            return

        while True:
            credential = input_handlers.input_user_login()
            try:
                if utilities.validate_credential(credential["user"], credential["password"], users):
                    print(f"\nAcceso concedido. ¡Bienvenido, {credential['user'].upper()}!")
                    handle_main_menu()
                    break
                else:
                    print("\nUsuario o contraseña incorrectos. Intente nuevamente.")
            except ValueError as e:
                print(f"\nError de validación: {e}\n")

    except Exception as e:
        print_console.print_error(f"Error inesperado: {e}")

def handle_new_user_menu():
    try:
        users = services.get_users()
        credential = input_handlers.input_new_user(users)
        services.add_user(**credential)
        print(f"\nEl usuario {credential['user'].upper()} fue creado correctamente.")
        print("Por favor, inicie sesión con sus credenciales.")

    except FileNotFoundError:
        print_console.print_warning("No existe el archivo de usuarios. Se creará automáticamente.")
        services.add_user(**credential)

    except Exception as e:
        print(f"Error al crear el usuario: {e}")

def handle_main_menu():
    while True:
        print_console.print_main_menu()
        option = read_console.get_option(1, 5)
        match option:
            case 1:
                handle_employee_menu()
            case 2:
                handle_project_menu()
            case 3:
                handle_assignment_menu()
            case 4:
                handle_reports_menu()
            case 5:
                break

def handle_employee_menu():
    while True:
        print_console.print_employee_menu()
        option = read_console.get_option(1, 4)
        match option:
            case 1:
                handle_new_employee()
            case 2:
                handle_delete_employee()
            case 3:
                handle_modify_employee()
            case 4:
                print_console.print_back_to_menu()
                break

def handle_new_employee():
    try:
        while True:
            print_console.print_new_employee()
            employee_data = input_handlers.input_new_employee()
            try:
                services.add_employee(**employee_data)
                print(f"\n✅ Empleado {employee_data['name'].upper()} {employee_data['last_name'].upper()} agregado correctamente con legajo {employee_data['employee_id']}.")
                print_console.print_add_new_user()
                option = read_console.get_option(1, 2)
                if option == 2:
                    print_console.print_back_to_menu()
                    break
            except ValueError as e:
                print(f"\nError de validación: {e}\n")
    except FileNotFoundError:
        print_console.print_warning("Primero deberá crear un registro")
    except Exception as e:
        print_console.print_error(f"Error inesperado: {e}")

def handle_delete_employee():
    try:
        while True:
            print_console.print_delete_employee()
            option = read_console.get_option(1, 2)
            match option:
                case 1:
                    employee_id = input_handlers.input_delete_employee()
                    employee_to_delete = services.get_employee_by_id(employee_id)
                    print_console.print_employee_data(employee_to_delete)
                    confirm = input(f"¿Confirma eliminar el legajo {employee_id}? (S/N): ").strip().upper()
                    if confirm == "S":
                        services.delete_employee(employee_id)
                        print(f"\n✅ Legajo {employee_id} eliminado correctamente.")
                        print_console.print_delete_another_employee()
                        option = read_console.get_option(1, 2)
                        if option == 2:
                            print_console.print_back_to_menu()
                            break
                    else:
                        print("Operación cancelada.")
                case 2:
                    print_console.print_back_to_menu()
                    break
    except FileNotFoundError:
        print_console.print_warning("Primero deberá crear un registro")
    except Exception as e:
        print_console.print_error(f"Error inesperado: {e}")

def handle_modify_employee():
    try:
        while True:
            print_console.print_modify_employee()
            option = read_console.get_option(1, 2)
            match option:
                case 1:
                    employee_id = input_handlers.input_employee_id_for_modification()
                    employee = services.get_employee_by_id(employee_id)
                    print_console.print_employee_data(employee)

                    fields_to_update = input_handlers.input_employee_fields_to_modify(employee)

                    if fields_to_update:
                        services.modify_employee(employee_id, fields_to_update)
                        print("\n✅ Empleado modificado correctamente.")
                    else:
                        print("\nNo se realizaron modificaciones.")

                    print_console.print_back_to_menu()
                    break
                case 2:
                    print_console.print_back_to_menu()
                    break
    except FileNotFoundError:
        print_console.print_warning("Primero deberá crear un registro")
    except Exception as e:
        print_console.print_error(f"Error inesperado: {e}")
        
def handle_project_menu():
    while True:
        print_console.print_project_menu()
        option = read_console.get_option(1, 4)
        match option:
            case 1:
                handle_new_project()
            case 2:
                handle_modify_project()
            case 3:
                handle_delete_project()
            case 4:
                print_console.print_back_to_menu()
                break

def handle_new_project():
    try:
        while True:
            print_console.print_new_project()
            project_data = input_handlers.input_new_project()
            try:
                services.add_project(**project_data)
                print(f"\n✅ El proyecto {project_data['project_name'].upper()} del cliente {project_data['project_client'].upper()} agregado correctamente bajo el Id de proyecto {project_data['project_id']}.")
                print_console.print_add_new_project()
                option = read_console.get_option(1, 2)
                if option == 2:
                    print_console.print_back_to_menu()
                    break
            except ValueError as e:
                print(f"\nError de validación: {e}\n")
    except FileNotFoundError:
        print_console.print_warning("Primero deberá crear un registro")
    except Exception as e:
        print_console.print_error(f"Error inesperado: {e}")

def handle_modify_project():
    try:
        while True:
            print_console.print_modify_project()
            option = read_console.get_option(1, 3)
            match option:
                case 1:
                    project_id = input_handlers.input_project_id_for_modification()
                    project = services.get_project_by_id(project_id)
                    print_console.print_project_data(project)

                    fields_to_update = input_handlers.input_project_fields_to_modify(project)

                    if fields_to_update:
                        services.modify_project(project_id, fields_to_update)
                        print("\n✅ Proyecto modificado correctamente.")
                    else:
                        print("\nNo se realizaron modificaciones.")

                    print_console.print_back_to_menu()
                    break
                case 2:
                    projects = services.get_projects()

                    if not projects:
                        print_console.print_warning("No hay proyectos registrados para mostrar.")
                        input("\nPresione Enter para volver al menú...")
                        return
                    print("\n--- 📑 Mostrando Todos los Proyectos Registrados ---")
                            
                    for prj in projects:
                        print_console.print_project_data(prj)
                        print("-" * 40)
                    input("\nPresione Enter para volver al menú...")
                case 3:
                    print_console.print_back_to_menu()
                    break
    except FileNotFoundError:
        print_console.print_warning("Primero deberá crear un registro")
    except Exception as e:
        print_console.print_error(f"Error inesperado: {e}")

def handle_delete_project():
    try:
        while True:
            print_console.print_delete_project()
            option = read_console.get_option(1, 2)
            match option:
                case 1:
                    project_id = input_handlers.input_delete_project()
                    project_to_delete = services.get_project_by_id(project_id)
                    print_console.print_project_data(project_to_delete)
                    confirm = input(f"¿Confirma eliminar el proyecto con ID {project_id}? (S/N): ").strip().upper()
                    if confirm == "S":
                        services.delete_project(project_id)
                        print(f"\n✅ El proyecto con el ID {project_id} ha sido eliminado correctamente.")
                        print_console.print_delete_another_project()
                        option = read_console.get_option(1, 2)
                        if option == 2:
                            print_console.print_back_to_menu()
                            break
                    else:
                        print("Operación cancelada.")
                case 2:
                    print_console.print_back_to_menu()
                    break
    except FileNotFoundError:
        print_console.print_warning("Primero deberá crear un registro")
    except Exception as e:
        print_console.print_error(f"Error inesperado: {e}")

def handle_assignment_menu():
    while True:
        print_console.print_assignment_menu()
        option = read_console.get_option(1, 5)
        match option:
            case 1:
                handle_assign_task()
            case 2:
                handle_update_task_status()
            case 3:
                handle_modify_or_deassign_task()
            case 4:
                handle_task_template_menu()
            case 5:
                print_console.print_back_to_menu()
                break

def handle_assign_task():
    try:
        while True:
            print_console.print_assign_task()
            assignment_data = input_handlers.input_new_assignment()
            try:
                assignment_id = services.assign_task(**assignment_data)
                print(f"\n✅ La tarea {assignment_data['task_id']} asignada al empleado {assignment_data['employee_id']} se ha realizado con exito. El ID de la asignación es el {assignment_id}.")
                print_console.print_assign_another_task()
                option = read_console.get_option(1, 2)
                if option == 2:
                    print_console.print_back_to_menu()
                    break
            except ValueError as e:
                print(f"\nError de validación: {e}\n")
    except FileNotFoundError:
        print_console.print_warning("Primero deberá crear un registro")
    except Exception as e:
        print_console.print_error(f"Error inesperado: {e}")    

def handle_update_task_status():
    try:
        print_console.print_update_status()
        assignment_id = read_console.input_existing_assignment_id()
        assignment = services.get_assignment_by_id(assignment_id)
        
        current_status = print_console.print_task_status_options(assignment)
        new_status = ""
        option = 0

        if current_status == "Sin Empezar":
            option = read_console.get_option(1, 2)
            if option == 1:
                new_status = "En Curso"
        elif current_status == "En Curso":
            option = read_console.get_option(1, 2)
            if option == 1:
                new_status = "Terminada"
        else:
            input("\nPresione Enter para volver...")
            return

        if new_status:
            services.update_assignment_status(assignment_id, new_status)
            print(f"\n✅ ¡Éxito! Tarea {assignment_id} actualizada a '{new_status}'.")
        else:
            print("\nOperación cancelada.")

        input("\nPresione Enter para volver al menú...")
    except ValueError as e:
        print(f"\nError de validación: {e}\n")
    except FileNotFoundError:
        print_console.print_warning("Primero deberá crear un registro")
    except Exception as e:
        print_console.print_error(f"Error inesperado: {e}")

def handle_modify_or_deassign_task():
    try:
        print_console.print_modify_deassign()
        assignment_id = read_console.input_existing_assignment_id()
        assignment = services.get_assignment_by_id(assignment_id)
        current_status = assignment.get("status")

        if current_status != "Sin Empezar":
            print_console.print_error(f"La tarea está '{current_status}'. Solo se pueden modificar o desasignar tareas con estado 'Sin Empezar'.")
            input("\nPresione Enter para volver...")
            return

        print_console.print_modify_deassign_submenu(assignment)
        option = read_console.get_option(1, 3)
        match option:
            case 1:
                print("\nIngrese el ID del NUEVO empleado para esta tarea:")
                new_employee_id = input_handlers.input_delete_employee() 
                print("Validando nuevo empleado...")
                project_id = assignment.get("project_id")
                task_id = assignment.get("task_id")
                
                utilities.validate_employee_on_team(new_employee_id, project_id)
                utilities.validate_task_seniority(new_employee_id, task_id)
                
                services.modify_assigned_employee(assignment_id, new_employee_id)
                print(f"\n✅ ¡Éxito! Tarea {assignment_id} reasignada al empleado {new_employee_id}.")
            case 2:
                confirm = input(f"¿Está seguro que desea eliminar la asignación {assignment_id}? (S/N): ").upper()
                if confirm == "S":
                    services.deassign_task(assignment_id)
                    print(f"\n✅ ¡Éxito! Asignación {assignment_id} eliminada.")
                else:
                    print("\nOperación cancelada.")
            case 3:
                print("\nOperación cancelada.")
        input("\nPresione Enter para volver al menú...")

    except ValueError as e:
        print_console.print_error(f"{e}")
        input("\nPresione Enter para reintentar...")
    except FileNotFoundError:
        print_console.print_warning("No se encontró el archivo de asignaciones.")
    except Exception as e:
        print_console.print_error(f"Error inesperado: {e}")
        input("\nPresione Enter para volver al menú...")

def handle_task_template_menu():
    while True:
        try:
            print_console.print_task_template_menu()
            option = read_console.get_option(1, 4)
            
            match option:
                case 1:
                    print_console.print_new_task_header()
                    task_data = input_handlers.input_new_task_template()
                    task_id = services.add_task_template(task_data)
                    print(f"\n✅ ¡Éxito! Plantilla de Tarea {task_id} creada.")
                    input("\nPresione Enter para continuar...")
                case 2:
                    print_console.print_modify_task_header()
                    task_id = read_console.input_existing_task_id()
                    task = services.get_task_by_id(task_id)
                    
                    update_data = input_handlers.input_task_fields_to_modify(task)
                    if update_data:
                        services.modify_task_template(task_id, update_data)
                        print("\n✅ ¡Éxito! Plantilla de Tarea modificada.")
                    else:
                        print("\nℹ️ No se realizaron modificaciones.")
                    input("\nPresione Enter para continuar...")
                case 3:
                    print_console.print_delete_task_header()
                    task_id = read_console.input_existing_task_id()
            
                    confirm = input(f"¿Está seguro que desea eliminar la plantilla {task_id}? (S/N): ").upper()
                    if confirm == "S":
                        services.delete_task_template(task_id)
                        print(f"\n✅ ¡Éxito! Plantilla de Tarea {task_id} eliminada.")
                    else:
                        print("\nOperación cancelada.")
                    input("\nPresione Enter para continuar...")
                case 4:
                    print_console.print_back_to_menu()
                    break

        except ValueError as e:
            print_console.print_error(f"{e}")
            input("\nPresione Enter para reintentar...")
        except FileNotFoundError:
            print_console.print_warning("No se encontró el archivo de tareas.")
        except Exception as e:
            print_console.print_error(f"Error inesperado: {e}")
            input("\nPresione Enter para volver al menú...")

def handle_reports_menu():
    while True:
        print_console.print_reports_menu()
        option = read_console.get_option(1, 4) 
        match option:
            case 1:
                try:
                    stats = services.get_system_statistics()
                    print_console.print_statistics_report(stats)
                    input("\nPresione Enter para volver...")
                except Exception as e:
                    print_console.print_error(f"Error al generar reporte: {e}")
                    input("\nPresione Enter para volver...")
            case 2:
                handle_search_menu()
            case 3:
                handle_master_report()
            case 4:
                print_console.print_back_to_menu()
                break

def handle_search_menu():
    while True:
        print_console.print_search_menu()
        option = read_console.get_option(1, 4)
        try:
            match option:
                case 1:
                    emp_id = input_handlers.input_delete_employee()
                    data = services.get_employee_by_id(emp_id)
                    print_console.print_employee_data(data)
                case 2:
                    proj_id = input_handlers.input_project_id_for_modification()
                    data = services.get_project_by_id(proj_id)
                    print_console.print_project_data(data)
                case 3:
                    task_id = read_console.input_existing_task_id()
                    data = services.get_task_by_id(task_id)
                    print_console.print_task_template_data(data)
                case 4:
                    print_console.print_back_to_menu()
                    break
            if option != 4:
                input("\nPresione Enter para volver a la búsqueda...")

        except ValueError as e:
            print_console.print_error(f"{e}")
            input("\nPresione Enter para reintentar...")
        except Exception as e:
            print_console.print_error(f"Error inesperado: {e}")

def handle_master_report():
    try:
        print("\nGenerando reporte maestro... (esto puede tardar un momento)")
        report_data = services.get_master_report_data()
        print_console.print_master_report(report_data)
        input("\nPresione Enter para volver...")
    except FileNotFoundError:
        print_console.print_warning("Faltan archivos necesarios para el reporte.")
    except Exception as e:
        print_console.print_error(f"Error al generar reporte maestro: {e}")
        input("\nPresione Enter para volver...")

