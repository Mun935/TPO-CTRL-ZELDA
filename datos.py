empleados = [
    ["104890", "Valentina", "Molina",    2020, "UX/UI",       "Junior"],
    ["105123", "Agustín",   "Silva",     2016, "QA",          "Senior"],
    ["105456", "Camila",    "Ríos",      2019, "Desarrollo",  "Semi Senior"],
    ["105789", "Nicolás",   "Moreno",    2017, "Infra",       "Junior"],
    ["106012", "Julieta",   "Castro",    2015, "Soporte",     "Senior"],
    ["106345", "Franco",    "Ortiz",     2021, "Desarrollo",  "Junior"],
    ["106678", "Carolina",  "Suárez",    2018, "UX/UI",       "Semi Senior"],
    ["114789", "Cristian",  "Paredes",   2019, "Soporte",     "Junior"],
]

tupla_empleados = {
    "legajo": 0,
    "nombre": 1,
    "apellido": 2,
    "año_ingreso": 3,
    "puesto": 4,
    "seniority": 5
}

tupla_proyectos = {
    "id": 0,
    "empresa_cliente": 1,
    "nombre_proyecto": 2,
    "team_leader": 3,
    "tipo_proyecto": 4,
    "fecha_inicio": 5,
    "fecha_fin": 6
}
proyectos = [
    ["PRJ001", "TechSolutions SA",  "Sistema de Inventario",        "Laura Benítez",   "Desarrollo Web",   "2021-03-01", "2021-12-15"],
    ["PRJ002", "AgroIndustria SRL", "Plataforma de Monitoreo",      "Fernando Rivas",  "IoT",              "2020-07-10", "2021-01-30"]
]

proyectos_asignados = [
    ["104890", "PRJ001"],
    ["104890", "PRJ002"],
    ["105123", "PRJ002"],
    ["105456", "PRJ001"],
    ["105789", "PRJ002"],
    ["106012", "PRJ001"],
    ["106345", "PRJ001"],
    ["106678", "PRJ002"],
    ["114789", "PRJ001"],
    ["114789", "PRJ002"]
]

tareas = [
    ["TAR011", "Actualizar inventario",        "TechSolutions SA",  "Junior", "Cargar manualmente los productos iniciales en la base de datos."],
    ["TAR012", "Diseñar API REST",             "AgroIndustria SRL", "Senior", "Crear servicios para exponer datos de sensores a aplicaciones externas."],
    ["TAR021", "Crear manual de usuario",      "TechSolutions SA",  "Junior", "Redactar guía básica para el sistema de inventario."],
    ["TAR022", "Entrenar modelo predictivo",   "AgroIndustria SRL", "Senior", "Desarrollar modelo de predicción de rendimiento agrícola."],
    ["TAR031", "Migrar datos antiguos",        "TechSolutions SA",  "Senior", "Importar registros históricos al nuevo sistema."],
    ["TAR032", "Calibrar sensores",            "AgroIndustria SRL", "Junior", "Revisar el correcto funcionamiento de sensores de humedad."],
    ["TAR042", "Desplegar app móvil",          "AgroIndustria SRL", "Senior", "Lanzar aplicación de monitoreo en Android y iOS."],
    ["TAR051", "Migrar sistema legado",        "TechSolutions SA",  "Senior", "Llevar funcionalidades del sistema viejo al nuevo entorno."],
    ["TAR052", "Capacitar personal agrícola",  "AgroIndustria SRL", "Junior", "Dar soporte en uso de la plataforma de monitoreo."],
]

usuarios = [
    ["rfernandez","1234"]
    ]
