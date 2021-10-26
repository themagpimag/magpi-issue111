from gpiozero import Button

flame = Button(21)
msg1 = ""

while True:
    if flame.value == 1:
        msg1 = "Fire!  "
    else:
        msg1 = "No fire"
    print(msg1, end = "\r")