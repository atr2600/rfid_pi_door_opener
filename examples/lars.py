import RPi.GPIO as GPIO
import time





def opendoor():
        servoPIN = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPIN, GPIO.OUT)

        p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
        p.start(2.5) # Initialization
        try:
                
                p.ChangeDutyCycle(4.7)
                time.sleep(2)
                p.ChangeDutyCycle(8)
                time.sleep(0.5)
        except KeyboardInterrupt:
                p.stop()
                GPIO.cleanup()