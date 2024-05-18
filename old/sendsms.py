#!/usr/bin/python3
import serial
#import RPi.GPIO as GPIO
import time
# Activation du port série
phone = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)
phone.write(b'AT\r\n')
time.sleep(2)
phone.write(b'AT+CPIN=1248\r\n')
time.sleep(10)
phone.write(b'AT+CMGF=1\r\n')
time.sleep(3)
phone.write(b'AT+CNMI=2,1,0,0,0\r\n')
time.sleep(2)
phone.write(b'AT+CMGS=\"+33651691412\"\r\n')
time.sleep(2)
phone.write(b'Hello cher utilisateur, je suis ton Raspberry Pi\r\n') #message
time.sleep(2)
phone.write(b'\x1A') #Envoi du SMS
time.sleep(2)
#phone.write(b'ATD+33644757223;\r"); #appel téléphonique
