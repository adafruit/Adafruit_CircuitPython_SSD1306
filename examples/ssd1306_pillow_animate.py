# SPDX-FileCopyrightText: 2014 Tony DiCola for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!

import math
import time
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.
# Change these to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Note you can change the I2C address, or add a reset pin:
# disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3c, reset=reset_pin)

# Get display width and height.
width = disp.width
height = disp.height

# Clear display.
disp.fill(0)
disp.show()

# Create image buffer.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (width, height))

# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as this python script!
# Some nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)

# Create drawing object.
draw = ImageDraw.Draw(image)

# Define text and get total width.
text = (
    "SSD1306 ORGANIC LED DISPLAY. THIS IS AN OLD SCHOOL DEMO SCROLLER!!"
    + "GREETZ TO: LADYADA & THE ADAFRUIT CREW, TRIXTER, FUTURE CREW, AND FARBRAUSCH"
)
maxwidth, unused = draw.textsize(text, font=font)

# Set animation and sine wave parameters.
amplitude = height / 4
offset = height / 2 - 4
velocity = -2
startpos = width

# Animate text moving in sine wave.
print("Press Ctrl-C to quit.")
pos = startpos
while True:
    # Clear image buffer by drawing a black filled box.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    # Enumerate characters and draw them offset vertically based on a sine wave.
    x = pos
    for i, c in enumerate(text):
        # Stop drawing if off the right side of screen.
        if x > width:
            break
        # Calculate width but skip drawing if off the left side of screen.
        if x < -10:
            char_width, char_height = draw.textsize(c, font=font)
            x += char_width
            continue
        # Calculate offset from sine wave.
        y = offset + math.floor(amplitude * math.sin(x / float(width) * 2.0 * math.pi))
        # Draw text.
        draw.text((x, y), c, font=font, fill=255)
        # Increment x position based on chacacter width.
        char_width, char_height = draw.textsize(c, font=font)
        x += char_width

    # Draw the image buffer.
    disp.image(image)
    disp.show()

    # Move position for next frame.
    pos += velocity
    # Start over if text has scrolled completely off left side of screen.
    if pos < -maxwidth:
        pos = startpos

    # Pause briefly before drawing next frame.
    time.sleep(0.05)
