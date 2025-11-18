from infrastructure import storage
from shared import utilities
import random

def get_users():
    return storage.read_data("usuarios.csv")

def add_user(user, password):
    new_data = {
        "user": user,
        "password": password
    }
    storage.append_data("usuarios.csv", new_data)

def get_employees():
    return storage.read_data("empleados.csv")

def get_employee_by_id(employee_id):
    employees = get_employees()
    for emp in employees:
        if emp.get("employee_id") == str(employee_id):
            return emp
    raise ValueError(f"No se encontró el legajo {employee_id}")

def add_employee(employee_id, name, last_name, start_year, position, seniority):
    utilities.validate_employee_id(employee_id)
    new_employee = {
        "employee_id": str(employee_id),
        "name": name,
        "last_name": last_name,
        "start_year": str(start_year),
        "position": position,
        "seniority": seniority
    }
    storage.append_data("empleados.csv", new_employee)
    return employee_id

def delete_employee(employee_id):
    employees = get_employees()
    employee_id = str(employee_id)
    
    updated_list = [e for e in employees if e.get("employee_id") != employee_id]
    
    if len(updated_list) == len(employees):
        raise Exception(f"No se encontró el legajo {employee_id}")

    storage.delete_data("empleados.csv", updated_list)
    return True

def modify_employee(employee_id, update_data):
    employees = get_employees()
    employee_id = str(employee_id)

    modified = False
    for emp in employees:
        if emp.get("employee_id") == employee_id:
            emp.update(update_data)
            modified = True
            break

    if not modified:
        raise Exception(f"No se encontró el legajo {employee_id}")
    
    storage.delete_data("empleados.csv", employees)
    return True

def generate_unique_employee_id():
    employees = get_employees()
    existing_ids = {e.get("employee_id") for e in employees}
    
    while True:
        new_id = str(random.randint(100000, 119999))
        if new_id not in existing_ids:
            return new_id
        
def get_projects():
    return storage.read_data("proyectos.csv")

def get_project_by_id(project_id):
    projects = get_projects()
    for prj in projects:
        if prj.get("project_id") == str(project_id):
            return prj
    raise ValueError(f"No se encontró el número de proyecto {project_id}")

def add_project(project_id,project_client,project_name,project_leader,project_type,project_start_date,project_end_date):
    utilities.validate_project_id(project_id)
    new_project = {
        "project_id": str(project_id),
        "project_client": project_client,
        "project_name": project_name,
        "project_leader": project_leader,
        "project_type": project_type,
        "project_start_date": project_start_date.strftime("%d/%m/%Y"),
        "project_end_date": project_end_date.strftime("%d/%m/%Y")
    }
    storage.append_data("proyectos.csv", new_project)
    return project_id

def modify_project(project_id, update_data):
    project = get_projects()
    project_id = str(project_id)

    modified = False
    for prj in project:
        if prj.get("project_id") == project_id:
            prj.update(update_data)
            modified = True
            break

    if not modified:
        raise Exception(f"No se encontró el ID del proyecto {project_id}")
    
    storage.delete_data("proyectos.csv", project)
    return True

def delete_project(project_id):
    project = get_projects()
    project_id = str(project_id)
    
    updated_list = [prj for prj in project if prj.get("project_id") != project_id]
    
    if len(updated_list) == len(project):
        raise Exception(f"No se encontró el proyecto con el ID {project_id}")

    storage.delete_data("proyectos.csv", updated_list)
    return True

def get_tasks():
    return storage.read_data("tareas.csv")

def get_task_by_id(task_id):
    tasks = get_tasks()
    for task in tasks:
        if task.get("task_id").upper() == task_id.upper():
            return task
    raise ValueError(f"No se encontró la Tarea {task_id}.")

def get_team_assignments():
    return storage.read_data("asignaciones.csv")

def generate_unique_assignment_id():
    assignments = storage.read_data("asignaciones_tareas.csv")
    existing_ids = {a.get("assignment_id") for a in assignments}
    while True:
        number = random.randint(0, 999)
        new_id = f"ASG{number:03d}"
        if new_id not in existing_ids:
            return new_id

def assign_task(project_id, employee_id, task_id):
    utilities.validate_employee_on_team(employee_id, project_id)
    utilities.validate_task_seniority(employee_id, task_id)
    utilities.validate_task_client(project_id, task_id)

    new_assignment_id = generate_unique_assignment_id()
    
    new_data = {
        "assignment_id": new_assignment_id,
        "task_id": task_id,
        "project_id": project_id,
        "employee_id": employee_id,
        "status": "Sin Empezar"
    }

    storage.append_data("asignaciones_tareas.csv", new_data)
    
    return new_assignment_id

def get_task_assignments():
    return storage.read_data("asignaciones_tareas.csv")

def get_assignment_by_id(assignment_id):
    all_assignments = get_task_assignments()
    assignment_id_upper = assignment_id.upper()
    
    for assignment in all_assignments:
        if assignment.get("assignment_id", "").upper() == assignment_id_upper:
            return assignment
            
    raise ValueError(f"No se encontró la Asignación {assignment_id}.")

def update_assignment_status(assignment_id, new_status):
    all_assignments = get_task_assignments()
    assignment_id_upper = assignment_id.upper()
    modified = False

    for assignment in all_assignments:
        if assignment.get("assignment_id", "").upper() == assignment_id_upper:
            assignment["status"] = new_status
            modified = True
            break
    
    if not modified:
        raise ValueError(f"No se pudo actualizar la Asignación {assignment_id}.")

    storage.delete_data("asignaciones_tareas.csv", all_assignments)
    return True

def modify_assigned_employee(assignment_id, new_employee_id):
    all_assignments = get_task_assignments()
    assignment_id_upper = assignment_id.upper()
    modified = False

    for assignment in all_assignments:
        if assignment.get("assignment_id", "").upper() == assignment_id_upper:
            assignment["employee_id"] = new_employee_id
            modified = True
            break
    
    if not modified:
        raise ValueError(f"No se pudo modificar la Asignación {assignment_id}.")

    storage.delete_data("asignaciones_tareas.csv", all_assignments)
    return True

def deassign_task(assignment_id):
    all_assignments = get_task_assignments()
    assignment_id_upper = assignment_id.upper()

    new_assignment_list = [assignment for assignment in all_assignments if assignment.get("assignment_id", "").upper() != assignment_id_upper]

    if len(all_assignments) == len(new_assignment_list):
        raise ValueError(f"No se pudo eliminar la Asignación {assignment_id}.")

    storage.delete_data("asignaciones_tareas.csv", new_assignment_list)
    return True

def add_task_template(task_data):
    storage.append_data("tareas.csv", task_data)
    return task_data["task_id"]

def modify_task_template(task_id, update_data):
    all_tasks = get_tasks()
    task_id_upper = task_id.upper()
    modified = False

    for task in all_tasks:
        if task.get("task_id", "").upper() == task_id_upper:
            task.update(update_data)
            modified = True
            break
    
    if not modified:
        raise ValueError(f"No se pudo modificar la Tarea {task_id}.")

    storage.delete_data("tareas.csv", all_tasks)
    return True

def delete_task_template(task_id):
    task_id_upper = task_id.upper()
    task_assignments = get_task_assignments()

    for assignment in task_assignments:
        if assignment.get("task_id", "").upper() == task_id_upper:
            raise ValueError(f"Error: La Tarea {task_id} está en uso "
                             f"(Asignación {assignment.get('assignment_id')}) "
                             "y no puede ser eliminada.")

    all_tasks = get_tasks()
    new_task_list = [task for task in all_tasks if task.get("task_id", "").upper() != task_id_upper]
    if len(all_tasks) == len(new_task_list):
        raise ValueError(f"No se pudo eliminar la Tarea {task_id}.")

    storage.delete_data("tareas.csv", new_task_list)
    return True

def get_system_statistics():
    employees = get_employees()
    projects = get_projects()
    assignments = get_task_assignments()
    total_tasks = len(assignments)
    
    if total_tasks == 0:
        tasks_done = 0
        completion_percentage = 0
    else:
        tasks_done = 0
        for task in assignments:
            if task.get("status") == "Terminada":
                tasks_done += 1
        completion_percentage = (tasks_done / total_tasks) * 100

    stats = {
        "total_employees": len(employees),
        "total_projects": len(projects),
        "total_tasks": total_tasks,
        "tasks_todo": sum(1 for t in assignments if t.get("status") == "Sin Empezar"),
        "tasks_inprogress": sum(1 for t in assignments if t.get("status") == "En Curso"),
        "tasks_done": tasks_done,
        "completion_percentage": completion_percentage
    }
    return stats

def get_master_report_data():
    employees = get_employees()
    projects = get_projects()
    team_assignments = get_team_assignments()
    tasks = get_tasks()
    task_assignments = get_task_assignments()
    
    project_dict = {p['project_id']: p for p in projects}
    task_dict = {t['task_id']: t for t in tasks}
    master_report = []

    for emp in employees:
        emp_entry = {
            "id": emp['employee_id'],
            "name": f"{emp['name']} {emp['last_name']}",
            "position": emp['position'],
            "seniority": emp['seniority'],
            "projects": []
        }
        emp_project_ids = [team_assign['project_id'] for team_assign in team_assignments if team_assign['employee_id'] == emp['employee_id']]
        
        for proj_id in emp_project_ids:
            if proj_id not in project_dict:
                continue
            proj_data = project_dict[proj_id]
            proj_entry = {
                "id": proj_id,
                "name": proj_data['project_name'],
                "tasks": []
            }
            
            for task_assign in task_assignments:
                if (task_assign['employee_id'] == emp['employee_id'] and task_assign['project_id'] == proj_id):
                    task_id = task_assign['task_id']
                    if task_id not in task_dict:
                        continue
                    
                    task_data = task_dict[task_id]
                    task_entry = {
                        "id": task_id,
                        "name": task_data['task_name'],
                        "status": task_assign['status']
                    }
                    proj_entry['tasks'].append(task_entry)
            
            emp_entry['projects'].append(proj_entry)
        
        master_report.append(emp_entry)
        
    return master_report