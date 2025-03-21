import pandas as pd

# Cargar el CSV
df = pd.read_csv('data/respuestaLocal.csv', dtype=str)

# Lista de columnas a procesar
columnas = [
    'id_paciente', 'prestacion', 'nodulos', 'morfologia_nodulos', 'margenes_nodulos',
    'densidad_nodulo', 'microcalcificaciones', 'calcificaciones_benignas',
    'calcificaciones_sospechosas', 'distribucion_calcificaciones', 'presencia_asimetrias',
    'tipo_asimetria', 'hallazgos_asociados', 'lateralidad_hallazgo', 'birads', 'edad'
]

# Reemplazar 'NULL' por cadenas vacías solo en las columnas especificadas
df[columnas] = df[columnas].replace('NULL', '')

# Guardar el archivo modificado
df.to_csv('archivo_limpio.csv', index=False)
