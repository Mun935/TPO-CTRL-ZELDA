from shared import utilities
import msvcrt
import random

def get_option(min, max):
    while True:
        try:
            option = input("Opción elegida: ")
            return utilities.validate_option(option, min, max)
        except Exception as e:
            print(f"\nOpción inválida. {e}")

def input_hide(prompt=""):
    print(prompt, end="", flush=True)
    password = ""
    while True:
        ch = msvcrt.getwch()
        if ch == "\r":
            print()
            break
        elif ch == "\b":
            if password:
                password = password[:-1]
                print("\b \b", end="", flush=True)
        else:
            password += ch
            print("*", end="", flush=True)
    return password

def input_user():
    return input("Ingrese su usuario: ")

def input_password():
    return input_hide("Ingrese su contraseña: ")

def input_employee_id():
    while True:
        try:
            employee_id = str(random.randint(100000, 119999))
            return utilities.validate_employee_id(employee_id)
        except Exception as e:
            print(f"Error: {e}")

def _input_field(prompt, validation_fn):
    while True:
        try:
            value = input(prompt)
            return validation_fn(value)
        except Exception as e:
            print(f"Error: {e}")

def input_name():
    return _input_field("Nombre: ", utilities.validate_name)

def input_last_name():
    return _input_field("Apellido: ", utilities.validate_last_name)

def input_start_year():
    return _input_field("Año de ingreso: ", utilities.validate_start_year)

def input_position():
    return _input_field("Puesto: ", utilities.validate_position)

def input_seniority():
    return _input_field("Seniority: ", utilities.validate_seniority)

def input_delete_employee():
    return _input_field("Legajo: ", utilities.validate_delete_employee_id)

def input_field_modification(field_name, current_value):
    new_value = input(f"{field_name} actual es '{current_value}'. Ingrese nuevo valor (o presione Enter para mantener): ")
    return new_value.strip()

def input_project_id():
    while True:
        try:
            id = random.randint(000, 999)
            project_id = f"PRJ{id:03d}"
            return utilities.validate_project_id(project_id)
        except Exception as e:
            print(f"Error: {e}")

def input_project_client():
    return _input_field("Cliente: ", utilities.validate_project_client)

def input_project_name():
    return _input_field("Nombre del proyecto: ", utilities.validate_project_name)

def input_project_leader():
    return _input_field("Líder del proyecto: ", utilities.validate_project_leader)

def input_project_type():
    return _input_field("Tipo de proyecto: ", utilities.validate_project_type)

def input_project_dates():
    while True:
        try:
            start_str = input("Fecha de inicio del proyecto: ")
            end_str = input("Fecha de finalización del proyecto: ")
            start_date, end_date = utilities.validate_project_dates(start_str, end_str)
            return start_date, end_date
        except Exception as e:
            print(f"Error: {e}")

def input_list_project():
    return _input_field("ID Proyecto: ", utilities.validate_modify_project_id)

def input_project_field_modification(field_name, current_value):
    new_value = input(f"{field_name} actual es '{current_value}'. Ingrese nuevo valor (o presione Enter para mantener): ")
    return new_value.strip()

def input_delete_project():
    return _input_field("Legajo: ", utilities.validate_delete_project_id)

def input_existing_task_id():
    return _input_field("ID Tarea: ", utilities.validate_existing_task_id)

def input_existing_assignment_id():
    return _input_field("ID Asignación: ", utilities.validate_existing_assignment_id)

def input_new_task_id():
    while True:
        try:
            number = random.randint(100, 999)
            task_id = f"TAR{number}"
            return utilities.validate_new_task_id(task_id)
        except Exception as e:
            print(f"Info: {e}, generando nuevo ID...")

def input_task_name():
    return _input_field("Nombre de la Tarea: ", utilities.validate_project_name)

def input_task_client():
    return _input_field("Cliente: ", utilities.validate_project_client)

def input_task_seniority():
    return _input_field("Seniority: ", utilities.validate_seniority)

def input_task_description():
    return _input_field("Descripción: ", utilities.validate_task_description)