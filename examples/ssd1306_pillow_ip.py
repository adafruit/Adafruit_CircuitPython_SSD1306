# SPDX-FileCopyrightText: Melissa LeBlanc-Williams for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!
#
# Ported to Pillow by Melissa LeBlanc-Williams for Adafruit Industries from Code available at:
# https://learn.adafruit.com/adafruit-oled-displays-for-raspberry-pi/programming-your-display

# Imports the necessary libraries...
import fcntl
import socket
import struct

import board
import digitalio
from PIL import Image, ImageDraw, ImageFont

import adafruit_ssd1306


# This function allows us to grab any of our IP addresses
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(
        fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack("256s", str.encode(ifname[:15])),
        )[20:24]
    )


# Setting some variables for our reset pin etc.
RESET_PIN = digitalio.DigitalInOut(board.D4)
TEXT = ""

# Very important... This lets py-gaugette 'know' what pins to use in order to reset the display
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.
# Change these to the right size for your display!
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Note you can change the I2C address, or add a reset pin:
# oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3D, reset=RESET_PIN)

# This sets TEXT equal to whatever your IP address is, or isn't
try:
    TEXT = get_ip_address("wlan0")  # WiFi address of WiFi adapter. NOT ETHERNET
except OSError:
    try:
        TEXT = get_ip_address("eth0")  # WiFi address of Ethernet cable. NOT ADAPTER
    except OSError:
        TEXT = "NO INTERNET!"

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Load a font in 2 different sizes.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

# Draw the text
intro = "Hello!"
ip = "Your IP Address is:"
draw.text((0, 46), TEXT, font=font2, fill=255)
draw.text((0, 0), intro, font=font, fill=255)
draw.text((0, 30), ip, font=font2, fill=255)

# Display image
oled.image(image)
oled.show()
