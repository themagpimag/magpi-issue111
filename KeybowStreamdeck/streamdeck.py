# SPDX-FileCopyrightText: 2021 Sandy Macdonald
#
# SPDX-License-Identifier: MIT

# Modifications by Rob Zwetsloot

# You'll need to connect Keybow 2040 to a computer, as you would with a regular
# USB keyboard.

# Drop the keybow2040.py file into your `lib` folder on your `CIRCUITPY` drive.

# NOTE! Requires the adafruit_hid CircuitPython library also!

import board
from keybow2040 import Keybow2040

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Set up Keybow
i2c = board.I2C()
keybow = Keybow2040(i2c)
keys = keybow.keys

# Set up the keyboard and layout
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# A map of keycodes that will be mapped sequentially to each of the keys, 0-15
keymap =    [Keycode.KEYPAD_ZERO,
             Keycode.KEYPAD_ONE,
             Keycode.KEYPAD_TWO,
             Keycode.KEYPAD_THREE,
             Keycode.KEYPAD_FOUR,
             Keycode.KEYPAD_FIVE,
             Keycode.KEYPAD_SIX,
             Keycode.KEYPAD_SEVEN,
             Keycode.KEYPAD_EIGHT,
             Keycode.KEYPAD_NINE,
             Keycode.KEYPAD_PERIOD,
             Keycode.GRAVE_ACCENT,
             Keycode.KEYPAD_MINUS,
             Keycode.KEYPAD_PLUS,
             Keycode.KEYPAD_FORWARD_SLASH,
             Keycode.KEYPAD_ASTERISK]

# The colour to set the keys when pressed

rgb1 = (0, 255, 0) # green
rgb2 = (255, 255, 0) # yellow
rgb3 = (255, 0, 0) # red

keybow.set_all(*rgb1)

# Key on/off list

keytoggle = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# Attach handler functions to all of the keys
for key in keys:
    # A press handler that sends the keycode
    @keybow.on_press(key)
    def press_handler(key):
        if key.number == 9:
            key.set_led(*rgb2)
        keycode = keymap[key.number]
        keyboard.send(Keycode.LEFT_CONTROL, keycode)

    # A release handler that changes the colour of the keys
    @keybow.on_release(key)
    def release_handler(key):
        keystate = keytoggle[key.number]
        if key.number == 0 or key.number == 8:
            if keystate == 0:
                key.set_led(*rgb3)
                keytoggle[key.number] = 1
            else:
                key.set_led(*rgb1)
                keytoggle[key.number] = 0
        elif key.number >= 1 and key.number <= 3:
            key.set_led(*rgb2)
            keytoggle[key.number] = 1
            if key.number != 1:
                keys[1].set_led(*rgb1)
                keytoggle[1] = 0
            if key.number != 2:
                keys[2].set_led(*rgb1)
                keytoggle[2] = 0
            if key.number != 3:
                keys[3].set_led(*rgb1)
                keytoggle[3] = 0
        elif key.number == 9:
            key.set_led(*rgb1)
        else:
            if keystate == 0:
                key.set_led(*rgb2)
                keytoggle[key.number] = 1
            else:
                key.set_led(*rgb1)
                keytoggle[key.number] = 0

while True:
    # Always remember to call keybow.update()!
    keybow.update()