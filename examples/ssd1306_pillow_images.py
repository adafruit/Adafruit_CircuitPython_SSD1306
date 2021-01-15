# SPDX-FileCopyrightText: 2014 Tony DiCola for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!

from board import SCL, SDA
import busio
from PIL import Image
import adafruit_ssd1306

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Note you can change the I2C address, or add a reset pin:
# disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3c, reset=reset_pin)

# Clear display.
disp.fill(0)
disp.show()


# Load image based on OLED display height.  Note that image is converted to 1 bit color.
if disp.height == 64:
    image = Image.open("happycat_oled_64.ppm").convert("1")
else:
    image = Image.open("happycat_oled_32.ppm").convert("1")

# Alternatively load a different format image, resize it, and convert to 1 bit color.
# image = Image.open('happycat.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')

# Display image.
disp.image(image)
disp.show()
