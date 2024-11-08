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

encendido = int(input("Iniciar sistema si(1) no(0)"))
if(encendido == 1):
    encendido = True
else:
    encendido = False


if(encendido):
    registro = open('registro1.csv', 'w')
    registro.write(f"Temperatura"+";")
    registro.write(f"RH"+";")
    registro.write(f"Ppm"+";")
    registro.write(f"Luxometro"+"\n")

    while(encendido):
        with open('registro1.csv', 'a') as registro:
            '''temperatura = Pin(numero del pin)
            RH = input(numero del pin)
            Ppm = input(numero del pin)
            Luz = input(numero del pin)'''

            temperatura = random.uniform(21, 24)
            RH = random.uniform(60, 90)
            Ppm = random.uniform(600, 1600)
            Luz = random.uniform(0, 150)

            registro.write(f"{temperatura:.2f}"+";")
            registro.write(f"{RH:.2f}"+";")
            registro.write(f"{Ppm:.2f}"+";")
            registro.write(f"{Luz:.2f}"+"\n")

            print(f"hola")

            time.sleep(2)
        registro.close() 



