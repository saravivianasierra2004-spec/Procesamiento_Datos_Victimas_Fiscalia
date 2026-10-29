
# ==============================================
# FASE 3 - PROCESAMIENTO DE DATOS CON SPARK
# Estudiante: Sara Sierra
# Fecha: 28/10/2026
# ==============================================

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import matplotlib.pyplot as plt
import pandas as pd

# ==============================================
# PASO 1: INICIAR LA SESIÓN DE SPARK
# ==============================================
spark = SparkSession.builder \
    .appName("Procesamiento_Datos_Victimas") \
    .getOrCreate()

print("=" * 60)
print(" SESIÓN DE SPARK INICIADA CORRECTAMENTE")
print("=" * 60)

# ==============================================
# PASO 2: CARGAR EL CONJUNTO DE DATOS
# ==============================================
ruta_archivo = "DATOS_VICTIMAS_FISCALIA.csv"

df = spark.read.csv(
    ruta_archivo,
    header=True,
    sep=';',
    encoding='UTF-8',
    multiLine=True,
    quote='"',
    escape='"'
)


print(f"\n Archivo cargado: {ruta_archivo}")
print(f" Total de registros: {df.count()}")
print(f" Total de columnas: {len(df.columns)}")

# ==============================================
# PASO 3: EXPLORACIÓN INICIAL DE LOS DATOS
# ==============================================
print("\n" + "=" * 60)
print(" ESTRUCTURA DE LOS DATOS")
print("=" * 60)
df.printSchema()

print("\n" + "=" * 60)
print(" PRIMERAS 5 FILAS DEL CONJUNTO DE DATOS")
print("=" * 60)
df.show(5, truncate=False)

# ==============================================
# PASO 4: LIMPIEZA DE DATOS
# ==============================================
print("\n" + "=" * 60)
print("VERIFICACIÓN DE VALORES NULOS")
print("=" * 60)




# Eliminar filas con valores nulos
# df_limpio = df.na.drop(how="any")
df_limpio = df
print(f"\n Registros después de limpieza: {df_limpio.count()}")
# ==============================================
# PASO 5: ANÁLISIS EXPLORATORIO DE DATOS (EDA)
# ==============================================
# RESUMEN ESTADÍSTICO
print("\n" + "=" * 60)
print(" RESUMEN ESTADÍSTICO")
print("=" * 60)
print(" ⚠️ Todas las columnas son de tipo texto/categórico.")
print(" No hay cálculos numéricos disponibles para este conjunto de datos.")
print(f" Total de registros: {df_limpio.count()}")
print(f" Total de columnas: {len(df_limpio.columns)}")
# PASO 6: VISUALIZACIÓN DE RESULTADOS
print("\n" + "=" * 60)
print(" GENERANDO GRÁFICOS...")
print("=" * 60)

import matplotlib.pyplot as plt

# Convertir a Pandas para graficar
datos_pd = df_limpio.limit(100).toPandas()
print(" ✅ Datos convertidos a Pandas correctamente")

# Eliminar filas sin información
datos_filtrados = datos_pd[datos_pd['DEPARTAMENTO HECHO ORIGEN'] != 'Sin Información']

# Contar registros por Departamento
conteo_departamento = datos_filtrados['DEPARTAMENTO HECHO ORIGEN'].value_counts()

# Crear el gráfico real
plt.figure(figsize=(12, 6))
conteo_departamento.plot(kind='bar', color='#2E86AB')
plt.title('Cantidad de Registros por Departamento (Primeros 100)', fontsize=14, pad=20)
plt.xlabel('Departamento', fontsize=12)
plt.ylabel('Cantidad de Registros', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Guardar y mostrar
plt.savefig('grafica_departamentos.png', dpi=300, bbox_inches='tight')
print(" ✅ Gráfico guardado como: grafica_departamentos.png")
plt.show()

# =============================================
# FIN DEL PROCESAMIENTO EN BATCH
# =============================================
print("\n" + "=" * 60)
print(" PROCESAMIENTO EN BATCH FINALIZADO EXITOSAMENTE")
print("=" * 60)
print(f" Total de registros procesados: {df_limpio.count()}")
print(f" Total de columnas: {len(df_limpio.columns)}")