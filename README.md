# Procesamiento de Datos en Batch — Datos de Víctimas de la Fiscalía de Colombia

## 📋 Descripción del Proyecto
Este proyecto realiza el procesamiento en batch de un conjunto de datos abiertos de la Fiscalía General de la Nación de Colombia, utilizando Apache Spark con Python (PySpark). El programa carga, explora, limpia y visualiza la información contenida en el archivo CSV.

## 👩‍🎓 Información del Estudiante
- *Nombre:* Sara Sierra
- *Fecha:* 28/10/2026
- *Asignatura:* Procesamiento de Datos

##  Archivos del Proyecto
- procesamiento_batch.py — Código principal del procesamiento
- DATOS_VICTIMAS_FISCALIA.csv — Conjunto de datos original
- grafica_departamentos.png — Visualización: registros por departamento

##  Información del Conjunto de Datos
- *Fuente:* Datos abiertos de la Fiscalía de Colombia
- *Registros:* 186,472
- *Columnas:* 43
- *Formato:* CSV separado por punto y coma (;)

##  Requisitos
- Python 3.x
- PySpark, Pandas, Matplotlib

##  Cómo Ejecutar
```bash
pip install pyspark pandas matplotlib
python procesamiento_batch.py