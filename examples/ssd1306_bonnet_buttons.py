# SPDX-FileCopyrightText: 2017 James DeVito for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!

import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from PIL import Image, ImageDraw
import adafruit_ssd1306

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)
# Create the SSD1306 OLED class.
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)


# Input pins:
button_A = DigitalInOut(board.D5)
button_A.direction = Direction.INPUT
button_A.pull = Pull.UP

button_B = DigitalInOut(board.D6)
button_B.direction = Direction.INPUT
button_B.pull = Pull.UP

button_L = DigitalInOut(board.D27)
button_L.direction = Direction.INPUT
button_L.pull = Pull.UP

button_R = DigitalInOut(board.D23)
button_R.direction = Direction.INPUT
button_R.pull = Pull.UP

button_U = DigitalInOut(board.D17)
button_U.direction = Direction.INPUT
button_U.pull = Pull.UP

button_D = DigitalInOut(board.D22)
button_D.direction = Direction.INPUT
button_D.pull = Pull.UP

button_C = DigitalInOut(board.D4)
button_C.direction = Direction.INPUT
button_C.pull = Pull.UP


# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)


while True:
    if button_U.value:  # button is released
        draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=0)  # Up
    else:  # button is pressed:
        draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=1)  # Up filled

    if button_L.value:  # button is released
        draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=0)  # left
    else:  # button is pressed:
        draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=1)  # left filled

    if button_R.value:  # button is released
        draw.polygon([(60, 30), (42, 21), (42, 41)], outline=255, fill=0)  # right
    else:  # button is pressed:
        draw.polygon(
            [(60, 30), (42, 21), (42, 41)], outline=255, fill=1
        )  # right filled

    if button_D.value:  # button is released
        draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=0)  # down
    else:  # button is pressed:
        draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=1)  # down filled

    if button_C.value:  # button is released
        draw.rectangle((20, 22, 40, 40), outline=255, fill=0)  # center
    else:  # button is pressed:
        draw.rectangle((20, 22, 40, 40), outline=255, fill=1)  # center filled

    if button_A.value:  # button is released
        draw.ellipse((70, 40, 90, 60), outline=255, fill=0)  # A button
    else:  # button is pressed:
        draw.ellipse((70, 40, 90, 60), outline=255, fill=1)  # A button filled

    if button_B.value:  # button is released
        draw.ellipse((100, 20, 120, 40), outline=255, fill=0)  # B button
    else:  # button is pressed:
        draw.ellipse((100, 20, 120, 40), outline=255, fill=1)  # B button filled

    if not button_A.value and not button_B.value and not button_C.value:
        catImage = Image.open("happycat_oled_64.ppm").convert("1")
        disp.image(catImage)
    else:
        # Display image.
        disp.image(image)

    disp.show()
