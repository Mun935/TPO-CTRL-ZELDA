import os
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_data_path(file_name):
    return os.path.join(BASE_DIR, "..", "data", file_name)

def validate_file(file_name):
    if not isinstance(file_name, str):
        raise TypeError(f"{file_name} debe ser un string.")
    if file_name.strip() == "":
        raise ValueError("El nombre del archivo no puede estar vacío.")

def read_data(file_name):
    validate_file(file_name)
    path = get_data_path(file_name)

    if not os.path.exists(path):
        raise FileNotFoundError(f"No se encontró el archivo {file_name}")
    
    with open(path, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        return list(reader)

def append_data(file_name, row):
    validate_file(file_name)
    path = get_data_path(file_name)

    if not os.path.exists(path):
        raise FileNotFoundError(f"No se encontró el archivo {file_name}")
    
    if not isinstance(row, dict):
        raise TypeError("Se esperaba un diccionario para escribir en el archivo.")

    with open(path, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        field_names = reader.fieldnames
    
    with open(path, "a", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writerow(row)

def delete_data(file_name, data):
    validate_file(file_name)
    path = get_data_path(file_name)

    if not os.path.exists(path):
        raise FileNotFoundError(f"No se encontró el archivo {file_name}")
    
    if not data or not isinstance(data, list) or not isinstance(data[0], dict):
        raise ValueError("Los datos a guardar deben ser una lista de diccionarios.")
    
    field_names = list(data[0].keys())

    with open(path, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)
    return True

