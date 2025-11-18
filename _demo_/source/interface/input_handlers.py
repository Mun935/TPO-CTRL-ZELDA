from interface import read_console
from shared import utilities

def input_user_login():
    user = read_console.input_user()
    password = read_console.input_password()
    return {
        "user": user,
        "password": password
    }

def input_new_user(users):
    while True:
        new_user = input("Elija un nombre de usuario: ").lower()
        if not new_user.isalpha():
            print("\nEl nombre de usuario debe contener solo letras.\n")
            continue

        if any(u.get("user", "").strip().lower() == new_user for u in users):
            print("\nEl usuario ya se encuentra registrado.\n")
            continue
        break

    new_password = read_console.input_hide(
        "Elija una contraseña. Debe contener entre 8 y 12 caracteres e incluir letras, números y al menos un símbolo: "
    )
    
    while not utilities.validate_password(new_password):
        print("\nLa contraseña debe tener entre 8 y 12 caracteres,")
        print("e incluir letras, números y al menos un símbolo.\n")
        new_password = read_console.input_hide("Ingrese su contraseña: ")

    return {
        "user": new_user,
        "password": new_password
    }

def input_new_employee():
    return {
        "employee_id": read_console.input_employee_id(),
        "name": read_console.input_name(),
        "last_name": read_console.input_last_name(),
        "start_year": read_console.input_start_year(),
        "position": read_console.input_position(),
        "seniority": read_console.input_seniority()
    }

def input_delete_employee():
    return read_console.input_delete_employee()

def input_employee_id_for_modification():
    return read_console.input_delete_employee()

def input_employee_fields_to_modify(current_data):
    updated_data = {}

    name = read_console.input_field_modification("Nombre", current_data["name"])
    if name:
        utilities.validate_name(name)
        updated_data["name"] = name

    last_name = read_console.input_field_modification("Apellido", current_data["last_name"])
    if last_name:
        utilities.validate_last_name(last_name)
        updated_data["last_name"] = last_name

    start_year = read_console.input_field_modification("Año de ingreso", current_data["start_year"])
    if start_year:
        updated_data["start_year"] = str(utilities.validate_start_year(start_year))

    position = read_console.input_field_modification("Puesto", current_data["position"])
    if position:
        updated_data["position"] = utilities.validate_position(position)

    seniority = read_console.input_field_modification("Seniority", current_data["seniority"])
    if seniority:
        updated_data["seniority"] = utilities.validate_seniority(seniority)

    return updated_data

def input_new_project():
    project_id = read_console.input_project_id()
    project_client = read_console.input_project_client()
    project_name = read_console.input_project_name()
    project_leader = read_console.input_project_leader()
    project_type = read_console.input_project_type()
    start_date, end_date = read_console.input_project_dates()
    
    return {
        "project_id": project_id,
        "project_client": project_client,
        "project_name": project_name,
        "project_leader": project_leader,
        "project_type": project_type,
        "project_start_date": start_date,
        "project_end_date": end_date
    }

def input_project_id_for_modification():
    return read_console.input_list_project()

def input_project_fields_to_modify(current_data):
    updated_data = {}

    client = read_console.input_project_field_modification("Cliente", current_data["project_client"])
    if client:
        utilities.validate_project_client(client)
        updated_data["project_client"] = client

    project_name = read_console.input_project_field_modification("Nombre del proyecto", current_data["project_name"])
    if project_name:
        utilities.validate_project_name(project_name)
        updated_data["project_name"] = project_name

    leader = read_console.input_project_field_modification("Líder del proyecto", current_data["project_leader"])
    if leader:
        utilities.validate_project_leader(leader)
        updated_data["project_leader"] = leader

    project_type = read_console.input_project_field_modification("Tipo de proyecto", current_data["project_type"])
    if project_type:
        updated_data["project_type"] = utilities.validate_project_type(project_type)

    prompt_start_date = current_data["project_start_date"]
    prompt_end_date = current_data["project_end_date"]
    
    while True:
        project_start_date = read_console.input_project_field_modification("Fecha de inicio del proyecto", prompt_start_date)
        project_end_date = read_console.input_project_field_modification("Fecha de fin del proyecto", prompt_end_date)

        new_project_start_date = project_start_date if project_start_date else current_data["project_start_date"]
        new_project_end_date = project_end_date if project_end_date else current_data["project_end_date"]

        try:
            start_date, end_date = utilities.validate_project_dates(new_project_start_date, new_project_end_date, is_modification=True)
            if project_start_date:
                updated_data["project_start_date"] = start_date.strftime("%d/%m/%Y")
            if project_end_date:
                updated_data["project_end_date"] = end_date.strftime("%d/%m/%Y")
            break 

        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Por favor, reingrese las fechas.")
            print("(Presione Enter en ambos campos para mantener los valores originales sin cambios)\n")
            
            prompt_start_date = current_data["project_start_date"]
            prompt_end_date = current_data["project_end_date"]

    return updated_data

def input_delete_project():
    return read_console.input_delete_project()

def input_new_assignment():
    project_id = input_project_id_for_modification() 
    employee_id = input_delete_employee() 
    task_id = read_console.input_existing_task_id()
    
    return {
        "project_id": project_id,
        "employee_id": employee_id,
        "task_id": task_id
    }

def input_new_task_template():
    return {
        "task_id": read_console.input_new_task_id(),
        "task_name": read_console.input_task_name(),
        "client": read_console.input_task_client(),
        "seniority": read_console.input_task_seniority(),
        "description": read_console.input_task_description()
    }

def input_task_fields_to_modify(current_data):
    updated_data = {}

    name = read_console.input_project_field_modification("Nombre", current_data["task_name"])
    if name:
        updated_data["task_name"] = utilities.validate_project_name(name)

    client = read_console.input_project_field_modification("Cliente", current_data["client"])
    if client:
        updated_data["client"] = utilities.validate_project_client(client)
    
    seniority = read_console.input_project_field_modification("Seniority", current_data["seniority"])
    if seniority:
        updated_data["seniority"] = utilities.validate_seniority(seniority)
        
    desc = read_console.input_project_field_modification("Descripción", current_data["description"])
    if desc:
        updated_data["description"] = utilities.validate_task_description(desc)

    return updated_data