from core import services
from datetime import datetime
import re

def validate_option(option, min, max):
    if not option.strip():
        raise ValueError("La opción ingresada es nula. Intente nuevamente.")

    if not option.isdigit():
        raise ValueError("Solo puede ingresar números. Intente nuevamente")

    option = int(option)
    if option < min or option > max:
        raise ValueError(f"Debe ingresar un número entre {min} y {max}.")
    return option

def validate_credential(user, password, users):
    if not user.strip():
        raise ValueError("El usuario no puede estar vacío.")

    if not re.fullmatch(r"[A-Za-z]+", user):
        raise ValueError("El usuario solo puede contener letras.")

    if not password.strip():
        raise ValueError("La contraseña no puede estar vacía.")

    try:
        for u in users:
            if u.get("user", "").strip().lower() == user.strip().lower() and u.get("password", "").strip() == password.strip():
                return True
        return False
    except Exception:
        raise ValueError("Error al validar credenciales. Verifique el formato del archivo CSV.")

def validate_password(password):
    if not password:
        raise ValueError("La contaseña no puede estar vacía. Intente nuevamente.")
    if not 8 <= len(password) <= 12:
        return False

    return all([
        re.search(r"[A-Za-z]", password),
        re.search(r"\d", password),
        re.search(r"[^\w\s]", password)
    ])

def _validate_employee_id_common(employee_id, must_exist=True):
    if not employee_id.strip():
        raise ValueError("El legajo no puede estar vacío. Intente nuevamente.")

    employees = services.get_employees()
    ids = [emp.get("employee_id") for emp in employees]

    if must_exist and employee_id not in ids:
        raise ValueError(f"No se encontró el legajo {employee_id} en el sistema.")
    elif not must_exist and employee_id in ids:
        raise ValueError(f"El legajo {employee_id} ya existe en el sistema.")

    return employee_id

def validate_employee_id(employee_id):
    return _validate_employee_id_common(employee_id, must_exist=False)

def validate_delete_employee_id(employee_id):
    return _validate_employee_id_common(employee_id, must_exist=True)

def validate_name(name):
    if not name.strip():
        raise ValueError("El nombre no puede estar vacío. Intente nuevamente.")
    if not re.fullmatch(r"[A-Za-zÀ-ÿÑñ\s]+", name):
        raise ValueError("El nombre solo puede contener letras y espacios.")
    return name

def validate_last_name(last_name):
    if not last_name.strip():
        raise ValueError("El apellido no puede estar vacío. Intente nuevamente.")
    if not re.fullmatch(r"[A-Za-zÀ-ÿÑñ\s]+", last_name):
        raise ValueError("El apellido solo puede contener letras y espacios.")
    return last_name

def validate_start_year(start_year):
    if not start_year.strip():
        raise ValueError("El año de ingreso no puede estar vacío. Intente nuevamente.")

    if not re.fullmatch(r"\d{4}", start_year):
        raise ValueError("El año debe contener 4 dígitos numéricos.")

    year = int(start_year)
    now = datetime.now().year
    if not 2015 <= year <= now:
        raise ValueError(f"El año debe estar entre 2015 y {now}.")
    return year

def validate_position(position):
    if not position.strip():
        raise ValueError("El puesto no puede estar vacío. Intente nuevamente.")
    if not re.fullmatch(r"[A-Za-zÀ-ÿÑñ\s]+", position):
        raise ValueError("El puesto solo puede contener letras y espacios.")
    return position

def validate_seniority(seniority):
    if not seniority.strip():
        raise ValueError("El seniority no puede estar vacío. Intente nuevamente.")
    if not re.fullmatch(r"[A-Za-zÀ-ÿÑñ\s]+", seniority):
        raise ValueError("El seniority solo puede contener letras y espacios.")
    return seniority

def _validate_project_id_common(project_id, must_exist=True):
    if not project_id.strip():
        raise ValueError("El número de proyecto no puede estar vacío. Intente nuevamente.")

    project_id_upper = project_id.upper()
    projects = services.get_projects()
    ids_upper = [prj.get("project_id").upper() for prj in projects if prj.get("project_id")]
    
    if must_exist and project_id_upper not in ids_upper:
        raise ValueError(f"No se encontró el ID del proyecto {project_id} en el sistema.")
    elif not must_exist and project_id_upper in ids_upper:
        raise ValueError(f"El ID del proyecto {project_id} ya existe en el sistema.")

    return project_id_upper

def validate_project_id(project_id):
    return _validate_project_id_common(project_id, must_exist=False)

def validate_project_client(client):
    if not client.strip():
        raise ValueError("El nombre del cliente no puede estar vacío. Intente nuevamente.")
    if not re.fullmatch(r"[A-Za-zÀ-ÿÑñ\s]+", client):
        raise ValueError("El nombre del cliente solo puede contener letras y espacios.")
    return client

def validate_project_name(project_name):
    if not project_name.strip():
        raise ValueError("El nombre del proyecto no puede estar vacío. Intente nuevamente.")
    if not re.fullmatch(r"[A-Za-zÀ-ÿÑñ\s]+", project_name):
        raise ValueError("El nombre del proyecto solo puede contener letras y espacios.")
    return project_name

def validate_project_leader(project_leader):
    if not project_leader.strip():
        raise ValueError("El nombre del proyecto no puede estar vacío. Intente nuevamente.")
    if not re.fullmatch(r"[A-Za-zÀ-ÿÑñ\s]+", project_leader):
        raise ValueError("El nombre del proyecto solo puede contener letras y espacios.")
    return project_leader

def validate_project_type(project_type):
    if not project_type.strip():
        raise ValueError("El nombre del proyecto no puede estar vacío. Intente nuevamente.")
    if not re.fullmatch(r"[A-Za-zÀ-ÿÑñ\s]+", project_type):
        raise ValueError("El nombre del proyecto solo puede contener letras y espacios.")
    return project_type

def _validate_date(date_str, campo):
    if not date_str.strip():
        raise ValueError(f"La {campo} no puede estar vacía. Intente nuevamente.")

    if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", date_str):
        raise ValueError("El formato de fecha es inválido. Utilice el formato dd/mm/aaaa")

    try:
        return datetime.strptime(date_str, "%d/%m/%Y")
    except ValueError:
        raise ValueError("La fecha ingresada no es válida.")

def validate_project_dates(project_start_date_str, project_end_date_str, is_modification=False):
    start_date = _validate_date(project_start_date_str, "fecha de inicio")

    if not is_modification:
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        if start_date < today:
            raise ValueError("La fecha de inicio debe ser mayor o igual a la fecha actual.")

    end_date = _validate_date(project_end_date_str, "fecha de finalización")
    if end_date <= start_date: 
        raise ValueError("La fecha de finalización debe ser mayor a la fecha de inicio.")

    return start_date, end_date

def validate_modify_project_id(project_id):
    return _validate_project_id_common(project_id, must_exist=True)

def validate_delete_project_id(project_id):
    return _validate_project_id_common(project_id, must_exist=True)

def validate_existing_task_id(task_id):
    if not task_id.strip():
        raise ValueError("El ID de Tarea no puede estar vacío.")
    
    tasks = services.get_tasks() 
    ids = [t.get("task_id").upper() for t in tasks if t.get("task_id")]
    
    if task_id.upper() not in ids:
        raise ValueError(f"No se encontró la Tarea {task_id}.")
    
    return task_id

def validate_employee_on_team(employee_id, project_id):
    team_assignments = services.get_team_assignments() 
    
    for assignment in team_assignments:
        if (assignment.get("employee_id") == employee_id and assignment.get("project_id") == project_id):
            return True

    raise ValueError(f"Validación fallida: El empleado {employee_id} no está asignado al proyecto {project_id}.")

def validate_task_seniority(employee_id, task_id):
    employee = services.get_employee_by_id(employee_id)
    task = services.get_task_by_id(task_id) 
    
    emp_seniority = employee.get("seniority", "").lower()
    task_seniority = task.get("seniority", "").lower()
    
    if task_seniority == "senior" and emp_seniority != "senior":
        raise ValueError(f"Validación fallida: La tarea {task_id} (Senior) no puede ser asignada a un empleado {emp_seniority}.")
    return True

def validate_task_client(project_id, task_id):
    project = services.get_project_by_id(project_id)
    task = services.get_task_by_id(task_id)
    
    if project.get("project_client") != task.get("client"): 
        raise ValueError(f"Validación fallida: La tarea {task_id} (Cliente: {task.get('client')}) "f"no pertenece al proyecto {project_id} (Cliente: {project.get('project_client')}).")
    return True

def validate_existing_assignment_id(assignment_id):
    if not assignment_id.strip():
        raise ValueError("El ID de Asignación no puede estar vacío.")

    services.get_assignment_by_id(assignment_id)
    
    return assignment_id.upper()

def _validate_task_id_common(task_id, must_exist=True):
    if not task_id.strip():
        raise ValueError("El ID de Tarea no puede estar vacío.")
    
    task_id_upper = task_id.upper()
    tasks = services.get_tasks()
    ids_upper = [t.get("task_id").upper() for t in tasks if t.get("task_id")]
    
    if must_exist and task_id_upper not in ids_upper:
        raise ValueError(f"No se encontró la Tarea {task_id}.")
    elif not must_exist and task_id_upper in ids_upper:
        raise ValueError(f"La Tarea {task_id} ya existe.")
        
    return task_id_upper

def validate_new_task_id(task_id):
    return _validate_task_id_common(task_id, must_exist=False)

def validate_task_description(description):
    if not description.strip():
        raise ValueError("La descripción no puede estar vacía.")
    return description