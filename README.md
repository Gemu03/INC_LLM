# Extracción de Datos de Notas Médicas

Este repositorio contiene dos aplicaciones basadas en FastAPI para extraer información estructurada de notas médicas en archivos CSV. 

- `app.py`: Utiliza la API de OpenAI para el procesamiento de texto.
- `local.py`: Utiliza un modelo alojado localmente a través de Ollama.

## Requisitos

Antes de ejecutar cualquiera de las aplicaciones, asegúrate de tener las siguientes dependencias instaladas:

Python v12 o superior con las siguientes librerías:

```bash
pip install -r requirements.txt
```

Si utilizas `local.py`, asegúrate de tener **Ollama** instalado y ejecutándose en tu máquina. Puedes descargarlo desde [Ollama](https://ollama.com/).

> Para ejecutar Ollama con el modelo Phi-4, utiliza el siguiente comando:
```bash
ollama serve --model phi4 
```

## Configuración

Debes crear un archivo `.env` en el directorio raíz del proyecto con las siguientes variables:

```ini
# Para app.py (requiere clave de API de OpenAI)
OPENAI_API_KEY=tu_clave_de_api

# Para local.py (requiere servidor Ollama)
OLLAMA_API_URL=http://localhost:11434/api
```

## Uso

### 1. Ejecutar con OpenAI (`app.py`)

Para iniciar el servidor FastAPI con OpenAI:

```bash
uvicorn app:app --reload
```

Esto iniciará un servidor en `http://127.0.0.1:8000`.

### 2. Ejecutar con OpenAI (`appd.py`)

Para iniciar el servidor FastAPI con DeepSeek:

```bash
uvicorn appd:app --reload
```

Esto iniciará un servidor en `http://127.0.0.1:8000`.

### 3. Ejecutar con Ollama (`local.py`)

Para usar el modelo Phi-4 de Ollama en local:

```bash
uvicorn local:app --reload
```

Asegúrate de que **Ollama está corriendo** en tu máquina antes de ejecutar este comando.

## Uso de la API

Ambas aplicaciones exponen un endpoint para procesar archivos CSV:

```
POST /process-medical-csv/
```

**Parámetros:**
- `file`: Archivo CSV (debe contener columnas `ID_DOCUMENTO`, `PRESTACION`, `EDAD_EN_FECHA_ESTUDIO`, `ESTUDIO`).
- `search_terms`: Términos clave para buscar en las notas médicas.
>search_terms: Por defecto está en "str".

Ejemplo de uso con `cURL`:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/process-medical-csv/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@archivo.csv' \
  -F 'search_terms="nodulos, calcificaciones"'
```

El resultado es un JSON con los datos extraídos.

Ejemplo de uso con `uvicorn local:app --reload`

- En la dirección **127.0.0.1:8000/docs** se encontrará la siguiente interfaz:
![alt text](/images/uvicorn.png)

- Se debe seleccior el endpoint POST de **/process-medical-csv/** y dar en la opción de **Try out**:
![alt text](/images/endpoint.png)

- Se de debe subir el archivo en csv con el formato solicitado y dar en execute:
![alt text](/images/upload%20file.png)

---

## Resultados

- **Precisión general (BIRADS):**
La clasificación BIRADS es crítica para determinar el manejo clínico de los hallazgos mamográficos:

![Precisión en clasificación BIRADS](/images/Imagen1.png)

 El modelo DeepSeek muestra la mayor precisión en la clasificación BIRADS (98.42%), seguido por Local (Phi4) (97.56%) y OpenAI (93.56%).

- **Tasa de alucinaciones (Menor es mejor):**
Las alucinaciones representan casos donde el modelo genera información incorrecta o no presente en la referencia:

![Tasa de alucinaciones](/images/Imagen2.png)

DeepSeek muestra la menor tasa de alucinaciones, seguido por OpenAI y Local (Phi4). Estos resultados indican que los modelos bajan la tasa de alucinaciones conforme aumenta su tamaño y complejidad.

- **Precisión por campo específico:**
Analizamos la precisión de cada modelo en la identificación de hallazgos radiológicos específicos, comparando todos los campos disponibles en los informes.


#### Comparativa de precisión entre modelos LLM en transcripción de historias clínicas

| **Campo clínico**                            | **DeepSeek** | **OpenAI** | **Phi4** |
|---------------------------------------------|--------------|------------|----------|
| Nódulos                                     | 81.36%       | 73.29%     | 33.37%   |
| Presencia Microcalcificaciones              | 70.25%       | 77.59%     | 29.68%   |
| Calcificaciones típicamente benignas        | 89.18%       | 74.91%     | 20.14%   |
| Calcificaciones morfología sospechosa       | 58.57%       | 52.58%     | 16.27%   |
| Distribución de las calcificaciones         | 81.80%       | 71.94%     | 28.93%   |
| Presencia de asimetrías                     | 75.50%       | 79.25%     | 43.80%   |
| Tipo de asimetría                           | 70.25%       | 22.03%     | 3.04%    |
| Hallazgos asociados                         | 74.34%       | 67.19%     | 40.41%   |
| Lateralidad hallazgo                        | 72.13%       | 63.55%     | 26.48%   |
| BIRADS                                      | 94.65%       | 92.56%     | 90.65%   |


- **Precios:**
Los precios de los modelos LLM varían según el proveedor y las características específicas de cada modelo. A continuación, se presentan los precios para cada modelo:

![Tasa de alucinaciones](/images/Imagen3.png)

Adicionalmente también se adjuntan otros posibles modelos a usar:

![Tasa de alucinaciones](/images/Imagen4.png)



## Contacto

Si tienes preguntas o sugerencias, abre un issue en este repositorio.
