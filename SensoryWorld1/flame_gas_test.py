from gpiozero import Button

flame = Button(21)
gas = Button(14)
msg1 = ""
msg2 = ""

while True:
    if flame.value == 1:
        msg1 = "Fire!   "
    else:
        msg1 = "No fire "
    if gas.value == 1:
        msg2 = "Gas leak!"
    else:
        msg2 = "No gas   "
    print(msg1, msg2, end = "\r")


        



    
        
        