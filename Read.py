#!/usr/bin/env python3

from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
from time import sleep

# Use Bradcom PIN setmode
GPIO.setmode(GPIO.BCM)

# Pins
buzzer = 0
RelayPin = 7
RedLed = 14

reader = SimpleMFRC522()

def setup():

    # set Pin's mode to output, and initial level to LOW(0V)
    GPIO.setup(RelayPin,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(RedLed,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(buzzer,GPIO.OUT,initial=GPIO.LOW)

def main():

    while True:

        print("Avvicina la carta al lettore NFC")

        text = reader.read()
        print(text)
        name = str(text)

        if name == "(114855542987, 'angelo                                          ')":
            
            print("Accesso autorizzato")
            # Blink green led once and turn on buzzer for 0.1s
            GPIO.output(RelayPin,GPIO.HIGH)
            GPIO.output(buzzer,GPIO.HIGH)
            sleep(0.1)
            GPIO.output(buzzer,GPIO.LOW)
            sleep(1)
            GPIO.output(RelayPin,GPIO.LOW)

        else:
            print("ERRORE, ACCESSO NON AUTORIZZATO")
            # Blink RED led three times and turn on buzzer as alarm
            GPIO.output(RedLed,GPIO.HIGH)
            GPIO.output(buzzer,GPIO.HIGH)
            sleep(0.3)
            GPIO.output(RedLed,GPIO.LOW)
            GPIO.output(buzzer,GPIO.LOW)
            sleep(0.3)
            GPIO.output(RedLed,GPIO.HIGH)
            GPIO.output(buzzer,GPIO.HIGH)
            sleep(0.3)
            GPIO.output(RedLed,GPIO.LOW)
            GPIO.output(buzzer,GPIO.LOW)
            sleep(0.3)    
            GPIO.output(RedLed,GPIO.HIGH)
            GPIO.output(buzzer,GPIO.HIGH)
            sleep(0.3)
            GPIO.output(RedLed,GPIO.LOW)
            GPIO.output(buzzer,GPIO.LOW)
            sleep(0.3)

def destroy():
    # release resources
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
            main()
    # when 'Ctrl+C' is pressed, destroy() will be executed.
    except KeyboardInterrupt:
        destroy()
