# SPDX-FileCopyrightText: Tony DiCola
# SPDX-License-Identifier: CC0-1.0

# Basic example of using framebuf capabilities on a SSD1306 OLED display.
# This example and library is meant to work with Adafruit CircuitPython API.

# Import all board pins.
import time
import board
import busio
from digitalio import DigitalInOut

# Import the SSD1306 module.
import adafruit_ssd1306


# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)
# A reset line may be required if there is no auto-reset circuitry
reset_pin = DigitalInOut(board.D5)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
# The I2C address for these displays is 0x3d or 0x3c, change to match
# A reset line may be required if there is no auto-reset circuitry
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3C, reset=reset_pin)

print(
    "Framebuf capability test - these are slow and minimal but don't require"
    "a special graphics management library, only `adafruit_framebuf`"
)

print("Pixel test")
# Clear the display.  Always call show after changing pixels to make the display
# update visible!
display.fill(0)
display.show()

# Set a pixel in the origin 0,0 position.
display.pixel(0, 0, 1)
# Set a pixel in the middle position.
display.pixel(display.width // 2, display.height // 2, 1)
# Set a pixel in the opposite corner position.
display.pixel(display.width - 1, display.height - 1, 1)
display.show()
time.sleep(0.1)

print("Lines test")
# we'll draw from corner to corner, lets define all the pair coordinates here
corners = (
    (0, 0),
    (0, display.height - 1),
    (display.width - 1, 0),
    (display.width - 1, display.height - 1),
)

display.fill(0)
for corner_from in corners:
    for corner_to in corners:
        display.line(corner_from[0], corner_from[1], corner_to[0], corner_to[1], 1)
display.show()
time.sleep(0.1)

print("Rectangle test")
display.fill(0)
w_delta = display.width / 10
h_delta = display.height / 10
for i in range(11):
    display.rect(0, 0, int(w_delta * i), int(h_delta * i), 1)
display.show()
time.sleep(0.1)

print("Text test")
display.fill(0)
try:
    display.text("hello world", 0, 0, 1)
    display.show()
    time.sleep(1)
    display.fill(0)
    char_width = 6
    char_height = 8
    chars_per_line = display.width // 6
    for i in range(255):
        x = char_width * (i % chars_per_line)
        y = char_height * (i // chars_per_line)
        display.text(chr(i), x, y, 1)
    display.show()
except FileNotFoundError:
    print(
        "To test the framebuf font setup, you'll need the font5x8.bin file from "
        + "https://github.com/adafruit/Adafruit_CircuitPython_framebuf/tree/master/examples"
        + " in the same directory as this script"
    )
