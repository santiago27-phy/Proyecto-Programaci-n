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

    while(encendido):
        with open('registro1.csv', 'a') as registro:
            for i in range(1):
                temperatura = random.uniform(21, 24)
                RH = random.uniform(60, 90)
                Ppm = random.uniform(600, 1600)
                Luz = random.uniform(0, 150)

                registro.write(f"{temperatura:.2f}"+"\t")
                registro.write(f"{RH:.2f}"+"\t")
                registro.write(f"{Ppm:.2f}"+"\t")
                registro.write(f"{Luz:.2f}"+"\n")

                print(f"hola")

                time.sleep(2)
        registro.close() 




