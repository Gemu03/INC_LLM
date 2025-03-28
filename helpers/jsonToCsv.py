import json
import csv

# Ruta al archivo JSON
json_file = "structured_data.json"
csv_file = "structured_data.csv"

# Cargar datos desde el archivo JSON
with open(json_file, encoding='utf-8') as f:
    data = json.load(f)

# Obtener nombres de columnas desde la primera entrada
columnas = data[0].keys()

# Escribir datos al archivo CSV
with open(csv_file, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=columnas, delimiter=';')
    writer.writeheader()
    writer.writerows(data)

print(f"Archivo CSV generado exitosamente como '{csv_file}'")
