from gpiozero import Button, LED, Buzzer
from time import sleep

flame = Button(21)
gas = Button(14)
led = LED(16)
buzzer = Buzzer(25)

def fire_alarm():
    print("Fire!    ", end = "\r")
    for i in range (10):
        led.toggle()
        buzzer.toggle()
        sleep(0.5)
    
def gas_alarm():
    print("Gas leak!", end = "\r")
    for i in range (10):
        led.toggle()
        buzzer.toggle()
        sleep(0.5)
        
while True:
    if flame.value == 1:
        fire_alarm()
    elif gas.value == 1:
        gas_alarm()
    else:
        print ("All OK   ", end = "\r")
        led.off()
        buzzer.off()