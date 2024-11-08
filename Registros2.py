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
def warning(temperatura, RH, Ppm, Luz):
    if(temperatura>23 or temperatura<20):
        print("Error de tamperatura")
    if(RH>80 or RH< 70):
        print("Error de RH")
    if(Ppm>800 or Ppm< 1200):
        print("Error de Ppm")
    if(Luz>50 or Luz< 120):
        print("Error de Luz")


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

            temperatura = random.uniform(21, 22)
            RH = random.uniform(60, 90)
            Ppm = random.uniform(600, 1600)
            Luz = random.uniform(0, 150)

            warning(temperatura, RH, Ppm, Luz)


            registro.write(f"{temperatura:.2f}"+";")
            registro.write(f"{RH:.2f}"+";")
            registro.write(f"{Ppm:.2f}"+";")
            registro.write(f"{Luz:.2f}"+"\n")



            print(f"hola")

            time.sleep(2)
        registro.close()
