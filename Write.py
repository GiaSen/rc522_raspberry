#!/usr/bin/env python3

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

# Buzzer pin
buzzer = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer,GPIO.OUT,initial=GPIO.LOW)

reader = SimpleMFRC522()

text = input('Inserisci qualcosa:')
print("Now place your tag to write")
reader.write(text)
print("Written")
GPIO.output(buzzer,GPIO.HIGH)
sleep(0.2)
GPIO.output(buzzer,GPIO.LOW)
GPIO.cleanup()