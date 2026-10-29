# Procesamiento de Datos en Batch — Datos de Víctimas de la Fiscalía de Colombia

##  Descripción del Proyecto
Este proyecto realiza el procesamiento en batch de un conjunto de datos abiertos de la Fiscalía General de la Nación de Colombia, utilizando Apache Spark con Python (PySpark). El programa carga, explora, limpia y visualiza la información contenida en el archivo CSV.

##  Información del Estudiante
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
- ## Procesamiento en Tiempo Real

### Descripción
Se simuló un flujo de datos en tiempo real utilizando Google Colab. En lugar de Apache Kafka, se realizó el envío secuencial de una muestra de 30 registros, procesándolos con Spark a medida que llegaban.

### Archivos adicionales
- procesamiento_tiempo_real.ipynb — Código completo de la simulación

###  Resultados obtenidos

#### Conteo por Departamento
| Departamento | Total Casos |
|---|---|
| Meta | 18 |
| Antioquia | 10 |
| Valle del Cauca | 2 |

#### Conteo por Tipo de Delito
| Tipo de Delito | Total Casos |
|---|---|
| Sin Información | 28 |
| Deportación, Expulsión, Traslado | 2 |

###  Nota técnica
Se utilizó Google Colab como entorno alternativo a la máquina virtual Ubuntu. Los análisis y resultados obtenidos son equivalentes. Se accedió a la interfaz web de Spark para monitorear Jobs, Stages, Environment y Executors durante la ejecución.

##  Cómo Ejecutar
```bash
pip install pyspark pandas matplotlib
python procesamiento_batch.py
