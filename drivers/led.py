import RPi.GPIO as GPIO

class LED():
  def __init__(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22, GPIO.OUT)

  def turn(self,bool):
    GPIO.output(7,bool)
