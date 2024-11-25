import time
import random

#from machine import Pin, I2C
#import dht
#from bh1750 import BH1750
#import network
#import urequests

'''
sensores:
- luminocidad
- ppm (partes por millon)/
- humedad
- temperatura
- ph(no está aun)

'''
# Solicita al usuario iniciar el sistema
encendido = int(input("Iniciar sistema si(1) no(0)"))
# Verifica la decisión del usuario
if(encendido == 1):
    encendido = True
else:
    encendido = False

# Si el sistema está encendido:
if(encendido):
    # Crea un archivo CSV para registrar los datos
    registro = open('registro1.csv', 'w')
    # Escribe los encabezados del archivo
    registro.write(f"Temperatura"+";")
    registro.write(f"RH"+";")
    registro.write(f"Ppm"+";")
    registro.write(f"Luxometro"+"\n")
# Inicia un bucle infinito mientras el sistema esté encendido
    while(encendido):
        # Abre el archivo en modo agregar ('a') para añadir datos sin borrar los anteriores
        with open('registro1.csv', 'a') as registro:
             # Aquí irían las lecturas de sensores reales (comentadas para simulación):
            '''temperatura = Pin(numero del pin)
            RH = input(numero del pin)
            Ppm = input(numero del pin)
            Luz = input(numero del pin)'''

             # Genera valores aleatorios que simulan las lecturas de los sensores
            temperatura = random.uniform(21, 24)
            RH = random.uniform(60, 90)
            Ppm = random.uniform(600, 1600)
            Luz = random.uniform(0, 150)

             # Escribe los datos simulados en el archivo CSV con dos decimales de precisión
            registro.write(f"{temperatura:.2f}"+";")
            registro.write(f"{RH:.2f}"+";")
            registro.write(f"{Ppm:.2f}"+";")
            registro.write(f"{Luz:.2f}"+"\n")

            # Mensaje de confirmación en la consola
            print(f"escritura confirmada")

             # Espera 2 segundos antes de registrar nuevos datos
            time.sleep(2)
        registro.close() 



