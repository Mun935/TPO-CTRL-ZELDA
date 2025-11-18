from source.infrastructure import storage
import os


TEST_FILE = "test_empleados.csv"

def setup_module(module):
    with open(storage.get_data_path(TEST_FILE), "w", encoding="utf-8-sig") as f:
        f.write("employee_id,name,last_name,start_year,position,seniority\n")

def teardown_module(module):
    os.remove(storage.get_data_path(TEST_FILE))

def test_append_and_read_data():
    employee = {
        "employee_id": "100001",
        "name": "Ana",
        "last_name": "Pérez",
        "start_year": "2020",
        "position": "Analista",
        "seniority": "Junior"
    }

    storage.append_data(TEST_FILE, employee)
    data = storage.read_data(TEST_FILE)

    assert len(data) == 1
    assert data[0]["name"] == "Ana"
    assert data[0]["employee_id"] == "100001"
