import pandas as pd
import matplotlib.pyplot as plt
import random
import time

# Configuración inicial
nombre_archivo = 'registro1.csv'
tamaño_lote = 100  # Número de filas recientes a analizar
modo_continuo = False  # Cambia a False para generar una cantidad fija de datos
cantidad_datos = 100  # Número de datos a generar si modo_continuo es False

# Inicialización del archivo CSV con encabezados
with open(nombre_archivo, 'w') as registro:
    registro.write("Temperatura;RH;Ppm;Luxometro\n")

def recolectar_datos():
    # Simulación de datos de sensores
    temperatura = random.uniform(21, 24)  # Temperatura simulada
    RH = random.uniform(60, 90)           # Humedad relativa simulada
    Ppm = random.uniform(600, 1600)       # Ppm simulada
    Luxometro = random.uniform(0, 150)    # Luminosidad simulada

    # Guardar los datos en el archivo CSV
    with open(nombre_archivo, 'a') as registro:
        registro.write(f"{temperatura:.2f};{RH:.2f};{Ppm:.2f};{Luxometro:.2f}\n")
    print("Datos recolectados y guardados en el archivo.")

def analizar_y_visualizar_datos():
    # Cargar solo el último lote de datos del archivo CSV
    df = pd.read_csv(nombre_archivo, sep=';').tail(tamaño_lote)

    # Crear un diccionario para almacenar los resultados
    resultados = {
        "Columna": [],
        "Media": [],
        "Mediana": [],
        "Moda": [],
        "Desviación Estándar": [],
        "Varianza": [],
        "Mínimo": [],
        "Máximo": []
    }

    # Calcular estadísticas para cada columna numérica
    for columna in df.select_dtypes(include='number').columns:
        media = df[columna].mean()
        mediana = df[columna].median()
        moda = df[columna].mode().values[0] if not df[columna].mode().empty else "N/A"
        desviacion_estandar = df[columna].std()
        varianza = df[columna].var()
        minimo = df[columna].min()
        maximo = df[columna].max()

        # Guardar resultados
        resultados["Columna"].append(columna)
        resultados["Media"].append(media)
        resultados["Mediana"].append(mediana)
        resultados["Moda"].append(moda)
        resultados["Desviación Estándar"].append(desviacion_estandar)
        resultados["Varianza"].append(varianza)
        resultados["Mínimo"].append(minimo)
        resultados["Máximo"].append(maximo)

        # Visualización en un histograma para cada columna
        plt.figure(figsize=(10, 6))
        plt.hist(df[columna], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
        plt.axvline(media, color='red', linestyle='dashed', linewidth=2, label=f'Media: {media:.2f}')
        plt.axvline(mediana, color='green', linestyle='dashed', linewidth=2, label=f'Mediana: {mediana:.2f}')
        plt.axvline(moda, color='blue', linestyle='dashed', linewidth=2, label=f'Moda: {moda:.2f}')
        plt.axvline(minimo, color='purple', linestyle='dotted', linewidth=2, label=f'Mínimo: {minimo:.2f}')
        plt.axvline(maximo, color='orange', linestyle='dotted', linewidth=2, label=f'Máximo: {maximo:.2f}')
        plt.axvspan(media - desviacion_estandar, media + desviacion_estandar, color='gray', alpha=0.2, label=f'Desviación estándar: ±{desviacion_estandar:.2f}')
        plt.xlabel('Valores')
        plt.ylabel('Frecuencia')
        plt.title(f'Distribución de la columna {columna} (Lote de {tamaño_lote} datos recientes)')
        plt.legend()
        plt.show()

    # Guardar los resultados del análisis en un archivo CSV
    resultados_df = pd.DataFrame(resultados)
    resultados_df.to_csv('analisis_columnas_lote.csv', index=False)
    print("Análisis y visualización completados. Resultados guardados en 'analisis_columnas_lote.csv'")

# Ciclo principal: recolección de datos y análisis en intervalos
if modo_continuo:
    # Generación en tiempo real
    while True:
        recolectar_datos()             # Recolecta y guarda los datos en CSV
        analizar_y_visualizar_datos()   # Analiza y visualiza el lote reciente de datos
        time.sleep(10)                  # Esperar 10 segundos antes del siguiente ciclo
else:
    # Generación de una cantidad fija de datos
    for _ in range(cantidad_datos):
        recolectar_datos()             # Recolecta y guarda los datos en CSV
    analizar_y_visualizar_datos()       # Analiza y visualiza el lote reciente de datos
